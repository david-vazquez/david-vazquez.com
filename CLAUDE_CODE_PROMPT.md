# Claude Code Prompt: Build David Vazquez Personal Website

## Context
I am David Vazquez, Research Director of the Foundational AI Research (FAR) team at ServiceNow Research in Montreal. I need a personal academic website at david-vazquez.com built with Hugo and HugoBlox Academic theme. All content files are provided in this kit.

## Requirements

### Technical Stack
- Hugo static site generator
- HugoBlox Academic theme (formerly Wowchemy)
- GitHub Pages hosting with custom domain (david-vazquez.com)
- GitHub Actions for CI/CD
- BibTeX import for publications using the `academic` CLI tool

### Design Preferences
- Dark theme with blue accents (similar to my LinkedIn banner: #0a0e1a background, #60a5fa accent)
- Clean, minimal, professional
- Fast loading, mobile responsive
- No dashes of any kind (em dashes, en dashes, or hyphens used as punctuation) in any text content

### Site Sections (navigation order)
1. Home (hero + brief bio + recent news)
2. Research (current projects)
3. Publications (full list from BibTeX, filterable)
4. Team (current + alumni)
5. Teaching
6. Talks (selected)
7. Contact

### Build Steps
1. `hugo new site david-vazquez-site`
2. Initialize HugoBlox Academic module
3. Copy all content files from this kit
4. Import publications: `academic import --bibtex data/publications.bib`
5. Configure theme, colors, fonts
6. Set up GitHub repository and Actions workflow
7. Test with `hugo server`
8. Deploy

### Important Notes
- Never use dashes as punctuation in any content
- Use the provided content files as the source of truth
- Profile photo will be added manually to assets/media/avatar.jpg
- Banner image will be added manually to assets/media/hero-banner.png
- Google Analytics can be added later
- Open Graph / Twitter cards should be configured for social sharing
