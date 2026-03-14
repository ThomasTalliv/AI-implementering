#!/usr/bin/env python3
"""Show all %% CLAUDE: %% comments across book chapters."""

from pathlib import Path
import re

BOOK_DIR = Path("/home/user/AI-implementering/book")

def main():
    files = sorted(BOOK_DIR.glob("*.md"))
    total = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        comments = re.findall(r'%%\s*(.*?)\s*%%', text, flags=re.DOTALL)
        if comments:
            print(f"\n### {path.name}")
            for c in comments:
                print(f"  - {c.strip()}")
            total += len(comments)
    if total == 0:
        print("Ingen %% kommentarer fundet.")
    else:
        print(f"\n{total} kommentar(er) i alt.")

if __name__ == "__main__":
    main()
