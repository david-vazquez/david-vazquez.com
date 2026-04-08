# David Vazquez Personal Website Kit
## For use with Claude Code + Hugo + HugoBlox Academic

## Quick Start with Claude Code

Open Claude Code in a new directory and give it these instructions:

```
Build my personal academic website using Hugo and the HugoBlox Academic theme.
Use all the content files in this kit as the source material.
Deploy to GitHub Pages at david-vazquez.com.

Steps:
1. Initialize a new Hugo site with HugoBlox Academic theme
2. Copy all content from this kit into the appropriate directories
3. Import publications from the publications.bib file
4. Configure the site with my branding (dark theme, blue accents)
5. Set up GitHub Actions for automatic deployment
6. Test locally before pushing

Reference: https://docs.hugoblox.com/getting-started/install-hugo/
```

## File Structure

```
website-kit/
  README.md                          <- This file
  CLAUDE_CODE_PROMPT.md              <- Full prompt to paste into Claude Code
  config/
    _default/
      hugo.yaml                      <- Main Hugo config
      params.yaml                    <- Theme parameters
      menus.yaml                     <- Navigation menu
  content/
    _index.md                        <- Homepage
    authors/david-vazquez/_index.md  <- Author profile
    project/                         <- Research projects
    publication/                     <- Generated from BibTeX
    teaching/                        <- Teaching section
    talk/                            <- Selected talks
    news/                            <- News updates
  data/
    publications.bib                 <- Master BibTeX file
  assets/media/                      <- Profile photo, banner, etc.
```

## Maintenance Workflow

When a new paper is published:
1. Add the BibTeX entry to data/publications.bib
2. Run: `academic import --bibtex data/publications.bib`
3. Commit and push (GitHub Actions handles deployment)

## Domain Setup

Point david-vazquez.com DNS to GitHub Pages:
- A record: 185.199.108.153
- A record: 185.199.109.153
- A record: 185.199.110.153
- A record: 185.199.111.153
- CNAME: www -> david-vazquez.github.io
