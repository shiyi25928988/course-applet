# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

This repo has a single working area: **`courseware/`** — a pure static HTML site (Chinese K-12 + exam-prep courseware library; ~1,100 HTML files, no framework, no build tools).

- **`courseware/CLAUDE.md`** — full guidance for this codebase (architecture, conventions, how to add chapters/exams). Read it before making changes.
- **`courseware/.claude/skills/`** — project skills for generating content pages (`create-chapter`, `create-exercises`, `create-exam`, `create-special-topic`, `create-subject-index`). Prefer these when adding content.
- **`.github/workflows/`** — pushes to `main` auto-deploy to GitHub Pages (site entry: `courseware/index.html`).
- `courseware/雅思阅读new最全题库.pdf` is deliberately git-ignored (source data for the IELTS exam generator).

## Working in the site

All edits happen under `courseware/`. Every page is a standalone HTML file linked by relative `<a href>` — no router, no bundler. After adding/renaming pages, validate links with:

```bash
cd courseware && python check_links.py
```

There is no build, lint, or test step.
