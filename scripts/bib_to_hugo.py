#!/usr/bin/env python3
"""Convert a BibTeX file into Hugo Blox publication folders.

Usage:
    python3 scripts/bib_to_hugo.py path/to/file.bib

Each BibTeX entry becomes a folder under content/publication/ with:
  - index.md  (YAML front matter)
  - cite.bib  (original BibTeX entry)
"""

import sys, os, re, unicodedata, textwrap
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "publication")

# Map BibTeX entry types to Hugo Blox publication_types
TYPE_MAP = {
    "article": "article-journal",
    "inproceedings": "paper-conference",
    "incollection": "paper-conference",
    "book": "book",
    "phdthesis": "thesis",
    "mastersthesis": "thesis",
    "misc": "manuscript",
    "patent": "patent",
}


def clean_latex(s):
    """Remove LaTeX braces and common accent commands."""
    if not s:
        return s
    # Handle \' \` \" \~ \^ \c accents
    accent_map = {
        "\\'": "", "\\`": "", '\\"': "", "\\~": "", "\\^": "", "\\c": "",
    }
    for cmd, repl in accent_map.items():
        s = s.replace(cmd, repl)
    s = s.replace("{", "").replace("}", "")
    s = s.replace("~", " ")
    # Normalize unicode
    s = unicodedata.normalize("NFC", s)
    return s.strip()


def parse_authors(raw):
    """Return a list of 'First Last' strings from BibTeX author field."""
    authors = []
    for a in raw.split(" and "):
        a = clean_latex(a.strip())
        if not a:
            continue
        if "," in a:
            parts = [p.strip() for p in a.split(",", 1)]
            a = f"{parts[1]} {parts[0]}"
        authors.append(a)
    return authors


def slugify(text):
    """Simple ASCII slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-")


def make_folder_name(entry):
    """first-author-year-firstword."""
    authors = parse_authors(entry.get("author", "Unknown"))
    first_last = authors[0].split()[-1] if authors else "unknown"
    year = entry.get("year", "0000")
    title_word = slugify(entry.get("title", "untitled")).split("-")[0]
    return slugify(f"{first_last}-{year}-{title_word}")


def entry_to_md(entry):
    """Generate YAML front matter for a single BibTeX entry."""
    title = clean_latex(entry.get("title", ""))
    authors = parse_authors(entry.get("author", ""))
    year = entry.get("year", "2000")
    etype = entry.get("ENTRYTYPE", "misc")
    pub_type = TYPE_MAP.get(etype, "manuscript")

    # Venue
    venue = entry.get("booktitle") or entry.get("journal") or entry.get("publisher") or ""
    venue = clean_latex(venue)

    # Date
    date = f"{year}-01-01"

    # Escape title for YAML
    safe_title = title.replace("'", "''")

    lines = [
        "---",
        f"title: '{safe_title}'",
        f"date: '{date}'",
        "draft: false",
        "authors:",
    ]
    for a in authors:
        lines.append(f"  - {a}")
    lines.append(f"publication_types:")
    lines.append(f"  - '{pub_type}'")
    lines.append(f"publication: '*{venue}*'")
    lines.append("abstract: ''")
    lines.append("featured: false")

    # Add url_pdf if we can guess an arXiv link from the entry
    if "arxiv" in entry.get("publisher", "").lower() or "arxiv" in entry.get("note", "").lower():
        arxiv_id = re.search(r"(\d{4}\.\d{4,5})", entry.get("publisher", "") + entry.get("note", ""))
        if arxiv_id:
            lines.append(f"url_pdf: 'https://arxiv.org/pdf/{arxiv_id.group(1)}'")
            lines.append(f"links:")
            lines.append(f"  - name: arXiv")
            lines.append(f"    url: 'https://arxiv.org/abs/{arxiv_id.group(1)}'")

    lines.append("---")
    return "\n".join(lines) + "\n"


def entry_to_bib(entry, raw_entries):
    """Return the raw BibTeX string for this entry."""
    key = entry.get("ID", "")
    # Try to find in raw text
    for raw in raw_entries:
        if key in raw:
            return raw.strip() + "\n"
    # Fallback: reconstruct
    etype = entry.get("ENTRYTYPE", "misc")
    fields = []
    skip = {"ID", "ENTRYTYPE"}
    for k, v in entry.items():
        if k not in skip:
            fields.append(f"  {k} = {{{v}}}")
    return f"@{etype}{{{key},\n" + ",\n".join(fields) + "\n}\n"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bib_to_hugo.py <bibfile>")
        sys.exit(1)

    bibfile = sys.argv[1]
    with open(bibfile, "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Split raw entries for faithful cite.bib reproduction
    raw_entries = re.split(r"\n(?=@)", raw_text)

    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_db = bibtexparser.loads(raw_text, parser=parser)

    os.makedirs(CONTENT_DIR, exist_ok=True)

    created = 0
    skipped = 0
    for entry in bib_db.entries:
        folder_name = make_folder_name(entry)
        folder_path = os.path.join(CONTENT_DIR, folder_name)

        if os.path.exists(folder_path):
            skipped += 1
            continue

        os.makedirs(folder_path, exist_ok=True)

        # Write index.md
        with open(os.path.join(folder_path, "index.md"), "w", encoding="utf-8") as f:
            f.write(entry_to_md(entry))

        # Write cite.bib
        with open(os.path.join(folder_path, "cite.bib"), "w", encoding="utf-8") as f:
            f.write(entry_to_bib(entry, raw_entries))

        created += 1

    print(f"Done: {created} created, {skipped} skipped (already exist).")


if __name__ == "__main__":
    main()
