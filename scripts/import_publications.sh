#!/bin/bash
# Import publications from BibTeX file into Hugo content
# Requires: pip install academic (the Hugo Academic CLI)
#
# Usage: ./scripts/import_publications.sh
#
# This script:
# 1. Reads data/publications.bib
# 2. Generates Hugo content pages in content/publication/
# 3. Each publication gets its own directory with index.md

set -e

echo "Importing publications from BibTeX..."

# Check if academic CLI is installed
if ! command -v academic &> /dev/null; then
    echo "Installing academic CLI..."
    pip install academic --break-system-packages
fi

# Import from BibTeX
academic import --bibtex data/publications.bib --publication-dir content/publication --overwrite

echo "Done. Publications imported to content/publication/"
echo "Run 'hugo server' to preview."
