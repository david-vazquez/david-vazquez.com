#!/usr/bin/env python3
"""Enrich Hugo publication pages with metadata from ServiceNow research pages.

This script:
1. Builds a mapping of ServiceNow publication URLs to local Hugo publication folders
2. Downloads featured images
3. Updates index.md with abstracts, PDF links, code links, video links

Usage:
    python3 scripts/enrich_publications.py metadata.jsonl

Where metadata.jsonl has one JSON object per line with fields:
  title, abstract, url_pdf, url_code, url_video, image_url, folder_name
"""

import json, os, sys, re, glob, urllib.request, time, unicodedata

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "publication")


def normalize(s):
    """Lowercase, strip punctuation, normalize unicode for fuzzy matching."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9\s]", "", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def load_local_publications():
    """Load all local publication folders and their titles."""
    pubs = {}
    for md_path in glob.glob(os.path.join(CONTENT_DIR, "*/index.md")):
        folder = os.path.basename(os.path.dirname(md_path))
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Extract title from front matter (handles multiline YAML)
        m = re.search(r"title:\s*['\"](.+?)['\"]", content, re.DOTALL)
        if not m:
            # Try unquoted title
            m = re.search(r"title:\s*(.+?)(?:\n\w|\n---)", content, re.DOTALL)
        if m:
            title = m.group(1).replace("''", "'").replace("\n", " ").strip()
            title = re.sub(r"\s+", " ", title)
            pubs[normalize(title)] = {"folder": folder, "path": md_path, "content": content, "title": title}
    return pubs


def download_image(url, dest_path):
    """Download an image from URL to dest_path."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 1000:  # sanity check
                with open(dest_path, "wb") as f:
                    f.write(data)
                return True
    except Exception as e:
        print(f"  Warning: could not download image: {e}")
    return False


def update_frontmatter(md_path, updates):
    """Update specific fields in the YAML front matter of a publication index.md."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split front matter and body
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
    fm = parts[1]
    body = parts[2]

    # Update abstract
    if updates.get("abstract"):
        abstract = updates["abstract"].replace("'", "''")
        fm = re.sub(r"abstract:\s*''", f"abstract: '{abstract}'", fm)

    # Add url_pdf if not present
    if updates.get("url_pdf") and "url_pdf:" not in fm:
        fm += f"\nurl_pdf: '{updates['url_pdf']}'"

    # Add url_code if not present
    if updates.get("url_code") and "url_code:" not in fm:
        fm += f"\nurl_code: '{updates['url_code']}'"

    # Add url_video if not present
    if updates.get("url_video") and "url_video:" not in fm:
        fm += f"\nurl_video: '{updates['url_video']}'"

    # Add links section for arXiv if we have a PDF
    if updates.get("url_pdf") and "links:" not in fm:
        arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d+\.\d+)", updates["url_pdf"])
        if arxiv_match:
            arxiv_id = arxiv_match.group(1)
            fm += f"\nlinks:"
            fm += f"\n  - name: arXiv"
            fm += f"\n    url: 'https://arxiv.org/abs/{arxiv_id}'"

    # Add image config if we downloaded one
    if updates.get("has_image") and "image:" not in fm:
        fm += "\nimage:"
        fm += "\n  focal_point: ''"
        fm += "\n  preview_only: false"

    # Ensure fm ends with newline
    if not fm.endswith("\n"):
        fm += "\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"---{fm}---{body}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 enrich_publications.py metadata.jsonl")
        sys.exit(1)

    metadata_file = sys.argv[1]
    local_pubs = load_local_publications()

    enriched = 0
    images_downloaded = 0

    with open(metadata_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            meta = json.loads(line)

            title_norm = normalize(meta.get("title", ""))

            # Try to find matching local publication
            matched_key = None
            for key in local_pubs:
                # Fuzzy match: check if one contains the other (titles may be truncated)
                if title_norm[:40] == key[:40] or key[:40] == title_norm[:40]:
                    matched_key = key
                    break
                # Also try substring match
                if len(title_norm) > 20 and title_norm[:30] in key:
                    matched_key = key
                    break

            if not matched_key:
                # Try matching by folder_name if provided
                if meta.get("folder_name"):
                    for key, val in local_pubs.items():
                        if val["folder"] == meta["folder_name"]:
                            matched_key = key
                            break

            if not matched_key:
                print(f"  No match for: {meta.get('title', '?')[:60]}")
                continue

            pub = local_pubs[matched_key]
            folder_path = os.path.join(CONTENT_DIR, pub["folder"])
            md_path = pub["path"]

            updates = {}

            # Abstract
            if meta.get("abstract"):
                updates["abstract"] = meta["abstract"]

            # PDF
            if meta.get("url_pdf"):
                updates["url_pdf"] = meta["url_pdf"]

            # Code
            if meta.get("url_code"):
                updates["url_code"] = meta["url_code"]

            # Video
            if meta.get("url_video"):
                updates["url_video"] = meta["url_video"]

            # Image
            if meta.get("image_url"):
                img_dest = os.path.join(folder_path, "featured.jpg")
                if not os.path.exists(img_dest):
                    if download_image(meta["image_url"], img_dest):
                        updates["has_image"] = True
                        images_downloaded += 1
                else:
                    updates["has_image"] = True

            if updates:
                update_frontmatter(md_path, updates)
                enriched += 1
                print(f"  Enriched: {pub['title'][:60]}")

    print(f"\nDone: {enriched} enriched, {images_downloaded} images downloaded.")


if __name__ == "__main__":
    main()
