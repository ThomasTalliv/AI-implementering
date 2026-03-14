#!/usr/bin/env python3
"""Compile all book chapters into a single clean .md file."""

from pathlib import Path
import re

BOOK_DIR = Path("/home/user/AI-implementering/book")
OUTPUT = Path("/home/user/AI-implementering/AI_i_Praksis_KOMPLET.md")

DEL_TITLES = {
    1: "Del 1: Fundamentet",
    2: "Del 2: De fire niveauer",
    3: "Del 3: Identifikation og igangsætning",
    4: "Del 4: Den svære samtale",
}

CHAPTERS = [
    (1, 1, "AI-landskabet i dag"),
    (2, 1, "De fire niveauer: En ramme for AI-adoption"),
    (3, 2, "Bestyrelsen: AI som digital tvilling"),
    (4, 2, "Strategisk ledelse: Kan AI erstatte afdelingsprocesser?"),
    (5, 2, "Mellemledelse: Kan AI automatisere medarbejderopgaver?"),
    (6, 2, "Medarbejdere: Kan jeg bruge AI i mit daglige arbejde?"),
    (7, 3, "Find dine AI-initiativer"),
    (8, 3, "Prioritering: Hvad skal I gøre først?"),
    (9, 3, "Den evolutionære tvilling"),
    (10, 3, "Koordinering på tværs"),
    (11, 4, "Forandringsledelse og AI"),
    (12, 4, "AI i alle typer virksomheder"),
    (13, 4, "Fremtiden: Hvad kommer efter?"),
]


def find_h1_positions(lines: list[str]) -> list[int]:
    """Return line indices of all H1 headings."""
    return [i for i, l in enumerate(lines) if re.match(r'^# ', l)]


def extract_chapter_body(text: str) -> tuple[str, str]:
    """
    Return (editor_intro, main_body) from a chapter file.

    Chapter file structure:
      H1 (outer wrapper)          <- skip
      *Del X* + ---               <- skip
      H1 (editor intro heading)   <- skip heading, keep text below
      [editor intro text]
      --- (separators)
      H1 (main content heading)   <- skip
      ---
      [main content]
    """
    lines = text.splitlines()
    h1_pos = find_h1_positions(lines)

    if len(h1_pos) < 2:
        # Simple structure — return everything after first H1 as body
        start = h1_pos[0] + 1 if h1_pos else 0
        return "", "\n".join(lines[start:]).strip()

    # Editor intro: lines between 2nd H1 and 3rd H1 (or end)
    intro_start = h1_pos[1] + 1
    intro_end = h1_pos[2] if len(h1_pos) >= 3 else len(lines)

    editor_intro_lines = lines[intro_start:intro_end]
    # Trim trailing separators
    while editor_intro_lines and editor_intro_lines[-1].strip() in ('', '---'):
        editor_intro_lines.pop()

    editor_intro = "\n".join(editor_intro_lines).strip()

    # Main body: lines after 3rd H1 (skip the heading line itself)
    if len(h1_pos) >= 3:
        body_start = h1_pos[2] + 1
        # Skip leading separator
        while body_start < len(lines) and lines[body_start].strip() in ('', '---'):
            body_start += 1
        main_body = "\n".join(lines[body_start:]).strip()
    else:
        main_body = ""

    return editor_intro, main_body


def extract_front_matter(text: str) -> str:
    """Extract forord + intro, stripping the title-page block."""
    lines = text.splitlines()
    # Find first ## Forord or # Forord
    start = 0
    for i, line in enumerate(lines):
        if re.match(r'^#+\s+Forord', line):
            start = i
            break
    return "\n".join(lines[start:]).strip()


def build_toc() -> str:
    lines = [
        "## Indholdsfortegnelse",
        "",
        "**Forord**  ",
        "**Introduktion: Sådan bruger du denne bog**",
        "",
        "---",
        "",
    ]
    current_del = None
    for ch_id, del_id, title in CHAPTERS:
        if del_id != current_del:
            current_del = del_id
            lines.append(f"### {DEL_TITLES[del_id]}")
            lines.append("")
        lines.append(f"- **Kapitel {ch_id}** — {title}")
    lines += [
        "",
        "---",
        "",
        "### Appendiks: Praktiske Redskaber og Skabeloner",
        "",
        "- AI Governance Readiness Score",
        "- Digital Twin Modenhedsvurdering",
        "- Afdelingsproces-audit",
        "- AI Impact × Feasibility Matrix",
        "- Opgave-dekomponerings-skabelon",
        "- Change Readiness Scorecard",
        "- Personlig AI-audit",
        "- Prompt Readiness Test",
        "- AI Modenhedstrappe",
        "- Prioriteringsmatrix: Impact × Feasibility × Strategisk Alignment",
        "- Handlingsplan-skabelon",
        "",
        "---",
    ]
    return "\n".join(lines)


def main():
    parts = []

    # ── Title page ────────────────────────────────────────────────────────────
    parts.append("""\
# AI i Praksis
## En Ledelsesbog om AI-Implementering
### Fra strategi til handling — på alle niveauer i organisationen

---

*"Den virksomhed der venter på den perfekte AI-strategi, taber terræn til den virksomhed der begynder med det ufuldkomne."*

---
""")

    # ── Table of contents ─────────────────────────────────────────────────────
    parts.append(build_toc())
    parts.append("\n\n")

    # ── Front matter ──────────────────────────────────────────────────────────
    fm_path = BOOK_DIR / "00_forord_og_indhold.md"
    if fm_path.exists():
        fm = extract_front_matter(fm_path.read_text(encoding="utf-8"))
        parts.append(fm)
        parts.append("\n\n---\n\n")

    # ── Chapters ──────────────────────────────────────────────────────────────
    current_del = None
    for ch_id, del_id, title in CHAPTERS:
        ch_path = BOOK_DIR / f"kapitel_{ch_id:02d}.md"
        if not ch_path.exists():
            print(f"  MANGLER: {ch_path}")
            continue

        # Del separator
        if del_id != current_del:
            current_del = del_id
            parts.append(f"\n\n---\n\n# {DEL_TITLES[del_id]}\n\n---\n\n")

        # Canonical chapter heading
        parts.append(f"# Kapitel {ch_id}: {title}\n\n")
        parts.append(f"*{DEL_TITLES[del_id]}*\n\n---\n\n")

        # Parse and clean chapter content
        raw = ch_path.read_text(encoding="utf-8")
        editor_intro, main_body = extract_chapter_body(raw)

        if editor_intro:
            parts.append(editor_intro)
            parts.append("\n\n---\n\n")

        parts.append(main_body)
        parts.append("\n\n---\n\n")

        words = len((editor_intro + " " + main_body).split())
        print(f"  Kapitel {ch_id:2d}: {words:,} ord")

    # ── Appendix ──────────────────────────────────────────────────────────────
    app_path = BOOK_DIR / "appendiks_skabeloner.md"
    if app_path.exists():
        app_raw = app_path.read_text(encoding="utf-8")
        app_lines = app_raw.splitlines()
        # Remove the first H1 heading (outer wrapper) and its trailing separator
        h1_positions = [i for i, l in enumerate(app_lines) if re.match(r'^# ', l)]
        if len(h1_positions) >= 2:
            # Skip first H1 block, start from second H1
            app_lines = app_lines[h1_positions[1]:]
        elif h1_positions:
            app_lines = app_lines[h1_positions[0] + 1:]
        parts.append("\n\n---\n\n")
        parts.append("\n".join(app_lines))

    # ── Write output ──────────────────────────────────────────────────────────
    full = "\n".join(parts)
    # Strip Obsidian %% comments %% (including CLAUDE: instructions)
    full = re.sub(r'%%.*?%%', '', full, flags=re.DOTALL)
    # Collapse 4+ blank lines into 2
    full = re.sub(r'\n{4,}', '\n\n\n', full)

    OUTPUT.write_text(full, encoding="utf-8")
    total_words = len(full.split())
    print(f"\n✅ Kompileret: {OUTPUT}")
    print(f"   Ordantal:   {total_words:,}")
    print(f"   Filstørrelse: {OUTPUT.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
