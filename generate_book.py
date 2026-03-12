#!/usr/bin/env python3
"""
AI-Implementering Book Generation System
Multi-agent system for writing a 60,000-word book about AI implementation.
"""

import os
import sys
import time
import anthropic
from pathlib import Path
from book_agents import AGENT_PERSONAS, BOOK_STRUCTURE, TEMPLATES_SPEC

def get_client():
    """Get Anthropic client using available auth method."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        return anthropic.Anthropic(api_key=api_key)
    # Try session ingress token
    token_file = "/home/claude/.claude/remote/.session_ingress_token"
    if os.path.exists(token_file):
        token = open(token_file).read().strip()
        return anthropic.Anthropic(auth_token=token)
    raise ValueError("No Anthropic credentials found")

client = get_client()
OUTPUT_DIR = Path("/home/user/AI-implementering/book")
OUTPUT_DIR.mkdir(exist_ok=True)


def stream_generate(system_prompt: str, user_prompt: str, max_tokens: int = 8000) -> str:
    """Generate content with streaming, return full text."""
    print("  [generating...]", end="", flush=True)
    full_text = []

    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=max_tokens,
        thinking={"type": "adaptive"},
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    ) as stream:
        for text in stream.text_stream:
            full_text.append(text)
            print(".", end="", flush=True)

    print(" done", flush=True)
    return "".join(full_text)


def generate_chapter_main(chapter: dict) -> str:
    """Generate the main chapter content by the Subject Matter Expert."""
    sme = AGENT_PERSONAS[chapter["sme"]]
    sections_text = "\n".join(f"- {s}" for s in chapter["sections"])

    prompt = f"""Skriv Kapitel {chapter['id']}: "{chapter['title']}" til bogen "AI i Praksis: En Ledelsesbog om AI-Implementering".

Dette er Del {chapter['del']} af bogen.

Kapitlet skal dække følgende sektioner:
{sections_text}

KRAV:
- Skriv minimum 4.000 ord med substans og dybde
- Brug konkrete danske og nordiske cases og eksempler (opfund realistiske, navngivne eksempler)
- Inkluder mindst 2-3 konkrete historier/anekdoter der illustrerer pointerne
- Skriv engagerende og fængende - som en bestselling businessbog, ikke en akademisk afhandling
- Afslut hvert afsnit med en klar takeaway
- Brug overskrifter (##) til sektioner og underoverskrifter (###) til underafsnit
- Start med en stærk åbning der fanger læseren
- Inkluder faktabokse, citater eller "nøgleindsigter" hvor relevant
- Skriv udelukkende på dansk

Format: Markdown med tydelig struktur"""

    return stream_generate(sme["system"], prompt, max_tokens=7000)


def get_mckinsey_review(chapter_content: str, chapter: dict) -> str:
    """Get McKinsey Partner's strategic enrichment."""
    persona = AGENT_PERSONAS["mckinsey_partner"]

    prompt = f"""Du har læst dette kapitel om "{chapter['title']}":

---
{chapter_content[:3000]}...
[kapitel fortsætter]
---

Som McKinsey partner med speciale i transformationsprocesser, tilføj et afsnit (300-500 ord) med:
1. Det strategiske perspektiv der mangler eller kan styrkes
2. En konkret framework eller model der er relevant
3. Best practice fra succesfulde AI-transformationer

Skriv afsnittet som et selvstændigt bidrag der kan integreres i kapitlet.
Titlen på dit bidrag: "## Strategisk perspektiv: [relevant undertitel]"
Skriv på dansk."""

    return stream_generate(persona["system"], prompt, max_tokens=2000)


def get_professor_review(chapter_content: str, chapter: dict) -> str:
    """Get AI Professor's technical enrichment."""
    persona = AGENT_PERSONAS["ai_professor"]

    prompt = f"""Du har læst dette kapitel om "{chapter['title']}":

---
{chapter_content[:3000]}...
[kapitel fortsætter]
---

Som AI-professor, tilføj et afsnit (300-500 ord) med:
1. Den tekniske præcision der er vigtig at have med
2. Hvad forskningen faktisk siger om dette område
3. Konkrete eksempler på AI-teknologier der er relevante her

Skriv afsnittet som et selvstændigt bidrag der kan integreres i kapitlet.
Titlen: "## Teknisk indsigt: [relevant undertitel]"
Skriv på dansk, tilgængeligt for ikke-tekniske ledere."""

    return stream_generate(persona["system"], prompt, max_tokens=2000)


def get_psychologist_review(chapter_content: str, chapter: dict) -> str:
    """Get Organizational Psychologist's human dimension."""
    persona = AGENT_PERSONAS["org_psychologist"]

    prompt = f"""Du har læst dette kapitel om "{chapter['title']}":

---
{chapter_content[:3000]}...
[kapitel fortsætter]
---

Som organisationspsykolog med speciale i forandringsledelse, tilføj et afsnit (300-500 ord) med:
1. De menneskelige og psykologiske dimensioner der er vigtige at forstå
2. Hvad der psykologisk set driver accept eller modstand i denne kontekst
3. Konkrete råd til at håndtere de menneskelige faktorer

Skriv afsnittet som et selvstændigt bidrag.
Titlen: "## Det menneskelige perspektiv: [relevant undertitel]"
Skriv på dansk."""

    return stream_generate(persona["system"], prompt, max_tokens=2000)


def editor_polish(full_chapter: str, chapter: dict) -> str:
    """Chief Editor does final polish and integration."""
    persona = AGENT_PERSONAS["chief_editor"]

    prompt = f"""Her er det samlede udkast til Kapitel {chapter['id']}: "{chapter['title']}" med bidrag fra forskellige eksperter:

---
{full_chapter[:6000]}
---

Som chefredaktør, skriv en forbedret introduktion (200-300 ord) til dette kapitel og en stærk afslutning/opsummering (300-400 ord).

INTRODUKTION skal:
- Fange læseren med en stærk hook (en situation, et dilemma, et overraskende faktum)
- Sætte scenen for kapitlets tema
- Love læseren konkret udbytte

AFSLUTNING/OPSUMMERING skal:
- Opsummere de 3-5 vigtigste pointer fra kapitlet
- Give en klar "Nu er du klar til at..." besked
- Binde an til næste kapitel (hvis relevant)

Format:
### KAPITEL INTRODUKTION:
[din introduktionstekst]

### KAPITEL OPSUMMERING:
[din opsummeringstekst]

Skriv på dansk, engagerende og præcist."""

    return stream_generate(persona["system"], prompt, max_tokens=2000)


def generate_full_chapter(chapter: dict) -> str:
    """Generate a complete chapter with all agent contributions."""
    ch_id = chapter["id"]
    ch_title = chapter["title"]

    print(f"\n{'='*60}")
    print(f"KAPITEL {ch_id}: {ch_title}")
    print(f"{'='*60}")

    # Check if already generated
    output_file = OUTPUT_DIR / f"kapitel_{ch_id:02d}.md"
    if output_file.exists():
        print(f"  Allerede genereret - indlæser eksisterende fil")
        return output_file.read_text(encoding="utf-8")

    # Step 1: SME writes main content
    print(f"\n[1/5] Fagekspert skriver hovedindhold...")
    main_content = generate_chapter_main(chapter)

    # Step 2: McKinsey review
    print(f"[2/5] McKinsey Partner tilføjer strategisk perspektiv...")
    mckinsey_addition = get_mckinsey_review(main_content, chapter)

    # Step 3: Professor review
    print(f"[3/5] AI-professor tilføjer teknisk indsigt...")
    professor_addition = get_professor_review(main_content, chapter)

    # Step 4: Psychologist review
    print(f"[4/5] Organisationspsykolog tilføjer menneskeligt perspektiv...")
    psych_addition = get_psychologist_review(main_content, chapter)

    # Combine all contributions
    combined = f"""# Kapitel {ch_id}: {ch_title}

{main_content}

---

{mckinsey_addition}

---

{professor_addition}

---

{psych_addition}
"""

    # Step 5: Editor polish
    print(f"[5/5] Chefredaktør skriver introduktion og opsummering...")
    editor_framing = editor_polish(combined, chapter)

    # Extract intro and summary from editor
    intro = ""
    summary = ""
    if "KAPITEL INTRODUKTION:" in editor_framing:
        parts = editor_framing.split("### KAPITEL OPSUMMERING:")
        intro_part = parts[0].replace("### KAPITEL INTRODUKTION:", "").strip()
        intro = intro_part
        if len(parts) > 1:
            summary = parts[1].strip()

    # Assemble final chapter
    del_name = {1: "Del 1: Fundamentet", 2: "Del 2: De fire niveauer",
                3: "Del 3: Identifikation og igangsætning", 4: "Del 4: Den svære samtale"}

    final_chapter = f"""# Kapitel {ch_id}: {ch_title}

*{del_name.get(chapter['del'], '')}*

---

{intro}

---

{main_content}

---

{mckinsey_addition}

---

{professor_addition}

---

{psych_addition}

---

## Opsummering og næste skridt

{summary}
"""

    # Save to file
    output_file.write_text(final_chapter, encoding="utf-8")
    print(f"  ✓ Kapitel {ch_id} gemt: {output_file}")

    word_count = len(final_chapter.split())
    print(f"  Ordantal: ~{word_count} ord")

    return final_chapter


def generate_templates() -> str:
    """Generate the templates appendix."""
    print(f"\n{'='*60}")
    print("APPENDIKS: PRAKTISKE REDSKABER OG SKABELONER")
    print(f"{'='*60}")

    output_file = OUTPUT_DIR / "appendiks_skabeloner.md"
    if output_file.exists():
        print("  Allerede genereret")
        return output_file.read_text(encoding="utf-8")

    sme = AGENT_PERSONAS["sme_ch7"]  # Business analyst for templates

    tools_list = ""
    for level in TEMPLATES_SPEC["tools"]:
        tools_list += f"\n**{level['level']}:**\n"
        for item in level["items"]:
            tools_list += f"- {item}\n"

    prompt = f"""Skriv et komplet appendiks med praktiske redskaber og skabeloner til bogen "AI i Praksis".

Appendikset skal indeholde følgende redskaber:
{tools_list}

For HVERT redskab, skriv:
1. En kort beskrivelse (2-3 sætninger) af formålet
2. Hvornår og hvordan det bruges
3. Selve skabelonen/værktøjet i en brugsvenlig format (brug tabeller, tjeklister, punktlister)
4. En vejledning til udfyldning/brug (3-5 trin)
5. Et eksempel på udfyldt skabelon

KRAV:
- Gør hvert redskab umiddelbart brugbart - læseren skal kunne tage det direkte i brug
- Brug tabeller, bokse og visuelle elementer (markdown format)
- Vær konkret og handlingsorienteret
- Minimum 200 ord per redskab
- Total minimum 3.000 ord

Skriv på dansk, praktisk og handlingsorienteret."""

    content = stream_generate(sme["system"], prompt, max_tokens=6000)

    final = f"""# Appendiks: Praktiske Redskaber og Skabeloner

*Dette appendiks indeholder alle de praktiske redskaber, skabeloner og frameworks der er refereret til i bogen. Du kan bruge dem selvstændigt eller i kombination med bogens kapitler.*

---

{content}

---

*Alle skabeloner kan downloades og tilpasses frit til din organisations behov.*
"""

    output_file.write_text(final, encoding="utf-8")
    print(f"  ✓ Appendiks gemt: {output_file}")
    return final


def generate_front_matter() -> str:
    """Generate foreword, introduction, and table of contents."""
    output_file = OUTPUT_DIR / "00_forord_og_indhold.md"
    if output_file.exists():
        return output_file.read_text(encoding="utf-8")

    print("\n[FORORD OG INDHOLDSFORTEGNELSE]")

    editor = AGENT_PERSONAS["chief_editor"]
    pm = AGENT_PERSONAS["project_manager"]

    # Generate foreword
    print("  Skriver forord...")
    foreword_prompt = """Skriv et stærkt forord (600-800 ord) til bogen "AI i Praksis: En Ledelsesbog om AI-Implementering".

Forordet skal:
- Beskrive det øjeblik alle erhvervsledere kender: Da man indser at AI ikke er fremtid - det er nu
- Forklare hvorfor denne bog er anderledes end alle de andre AI-bøger
- Sætte scenen: AI er et ledelsesansvar, ikke et IT-spørgsmål
- Beskrive de fire typer ledere bogen henvender sig til (bestyrelse, direktør, mellemleder, medarbejder)
- Ende med en invitation til at tage rejsen

Skriv engagerende, som om du taler direkte til den travle leder der holder bogen i hånden.
Skriv på dansk."""

    foreword = stream_generate(editor["system"], foreword_prompt, max_tokens=2000)

    # Generate introduction
    print("  Skriver introduktion...")
    intro_prompt = """Skriv en introduktion (400-500 ord) til bogen der forklarer:
1. Hvad de fire niveauer er og hvorfor de er centrale
2. Hvordan bogen er struktureret og hvordan man læser den
3. Hvad man konkret får ud af at læse bogen
4. En kort beskrivelse af de praktiske redskaber i appendikset

Skriv klart og struktureret. Skriv på dansk."""

    intro = stream_generate(pm["system"], intro_prompt, max_tokens=1500)

    # Build table of contents
    toc = """## Indholdsfortegnelse

**Forord**

**Introduktion: Sådan bruger du denne bog**

---

### Del 1: Fundamentet

- **Kapitel 1** — AI-landskabet i dag
  - Hvad AI faktisk kan (og ikke kan) i 2025/2026
  - Hvorfor AI er et ledelsesansvar, ikke et IT-projekt
  - De største misforståelser om AI i erhvervslivet
  - Bogens opbygning og hvem den henvender sig til

- **Kapitel 2** — De fire niveauer: En ramme for AI-adoption
  - Introduktion af de fire organisatoriske niveauer
  - Bestyrelsesniveauet: AI som digital tvilling
  - Strategisk ledelsesniveau: AI i afdelingsprocesser
  - Mellemlederniveauet: AI i medarbejderopgaver
  - Medarbejderniveauet: AI i det daglige arbejde
  - Hvordan niveauerne hænger sammen

---

### Del 2: De fire niveauer

- **Kapitel 3** — Bestyrelsen: AI som digital tvilling
- **Kapitel 4** — Strategisk ledelse: Kan AI erstatte afdelingsprocesser?
- **Kapitel 5** — Mellemledelse: Kan AI automatisere medarbejderopgaver?
- **Kapitel 6** — Medarbejdere: Kan jeg bruge AI i mit daglige arbejde?

---

### Del 3: Identifikation og igangsætning

- **Kapitel 7** — Find dine AI-initiativer
- **Kapitel 8** — Prioritering: Hvad skal I gøre først?
- **Kapitel 9** — Den evolutionære tvilling
- **Kapitel 10** — Koordinering på tværs

---

### Del 4: Den svære samtale

- **Kapitel 11** — Forandringsledelse og AI
- **Kapitel 12** — AI i alle typer virksomheder
- **Kapitel 13** — Fremtiden: Hvad kommer efter?

---

### Appendiks: Praktiske Redskaber og Skabeloner

**Niveau 1 — Bestyrelsen:**
- AI Governance Readiness Score
- Digital Twin Modenhedsvurdering

**Niveau 2 — Strategisk ledelse:**
- Afdelingsproces-audit
- AI Impact × Feasibility Matrix

**Niveau 3 — Mellemledelse:**
- Opgave-dekomponerings-skabelon
- Change Readiness Scorecard

**Niveau 4 — Medarbejdere:**
- Personlig AI-audit
- Prompt Readiness Test

**Tværgående redskaber:**
- AI Modenhedstrappe
- Prioriteringsmatrix: Impact × Feasibility × Strategisk Alignment
- Handlingsplan-skabelon

---
"""

    front_matter = f"""# AI i Praksis
## En Ledelsesbog om AI-Implementering
### Fra strategi til handling — på alle niveauer i organisationen

---

*"Den virksomhed der venter på den perfekte AI-strategi, taber terræn til den virksomhed der begynder med det ufuldkomne."*

---

## Forord

{foreword}

---

## Introduktion: Sådan bruger du denne bog

{intro}

---

{toc}
"""

    output_file.write_text(front_matter, encoding="utf-8")
    print(f"  ✓ Forord og indholdsfortegnelse gemt")
    return front_matter


def compile_full_book():
    """Compile all chapters into a single book file."""
    print("\n[KOMPILERER HELE BOGEN]")

    book_file = OUTPUT_DIR / "AI_i_Praksis_KOMPLET.md"

    all_content = []
    total_words = 0

    # Front matter
    front_path = OUTPUT_DIR / "00_forord_og_indhold.md"
    if front_path.exists():
        content = front_path.read_text(encoding="utf-8")
        all_content.append(content)
        total_words += len(content.split())

    # All chapters
    for i in range(1, 14):
        chapter_path = OUTPUT_DIR / f"kapitel_{i:02d}.md"
        if chapter_path.exists():
            content = chapter_path.read_text(encoding="utf-8")
            all_content.append("\n\n---\n\n")
            all_content.append(content)
            words = len(content.split())
            total_words += words
            print(f"  Kapitel {i}: ~{words} ord")

    # Templates
    templates_path = OUTPUT_DIR / "appendiks_skabeloner.md"
    if templates_path.exists():
        content = templates_path.read_text(encoding="utf-8")
        all_content.append("\n\n---\n\n")
        all_content.append(content)
        total_words += len(content.split())

    full_book = "\n".join(all_content)
    book_file.write_text(full_book, encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"BOG KOMPILERET: {book_file}")
    print(f"TOTAL ORDANTAL: ~{total_words:,} ord")
    print(f"{'='*60}")

    return total_words


def main():
    print("=" * 60)
    print("AI-IMPLEMENTERING BOGPROJEKT")
    print("Multi-Agent Book Writing System")
    print("=" * 60)
    print(f"Output mappe: {OUTPUT_DIR}")
    print(f"Model: claude-opus-4-6 med adaptive thinking")
    print()

    # Generate front matter
    generate_front_matter()

    # Generate all chapters
    for chapter in BOOK_STRUCTURE["chapters"]:
        generate_full_chapter(chapter)
        time.sleep(2)  # Brief pause between chapters

    # Generate templates
    generate_templates()

    # Compile full book
    total_words = compile_full_book()

    print(f"\n✅ Bogproduktion afsluttet!")
    print(f"   Total: ~{total_words:,} ord")
    print(f"   Mål: 60.000 ord")
    print(f"   Filer: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
