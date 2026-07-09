# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **pure static HTML website** — a Chinese K-12 courseware library covering math, physics, chemistry, and Chinese for junior/senior high school, plus competition math (AMC, CPhO), IELTS, and CAIE A-Level. ~1,600 HTML files, no framework, no build tools, no package manager.

## How to View / Run

- **View locally:** Open `index.html` in any browser, or serve with any static file server (e.g., `python -m http.server` or `npx serve`).
- **Check broken links:** `python check_links.py` or `python check_all_links.py` from the project root.
- There are no build, lint, test, or type-check commands. No `package.json`, no `tsconfig`, no `Makefile`.

## Architecture

### File-based routing with relative links

Every page is a standalone HTML file. Navigation is pure `<a href>` — no client-side router, no SPA, no JS framework. Links between subjects use relative paths (e.g., `../physics/index.html`).

Navigation hierarchy:
```
index.html                          # Homepage
  └── subject/index.html            # Subject landing page (sidebar + chapter grid)
        └── subject/ch01_topic.html # Chapter content page
        └── subject/exam_YYYY.html  # Yearly exam paper
```

Some subjects have sub-topics (e.g., `math/algebra/`, `math/geometry/`) with their own `index.html` and chapter files.

### Page layout pattern

Most content pages use a two-column layout:
- `<aside class="sidebar">` — sticky 280px left sidebar with chapter navigation (numbered circles, subsection links, back-home button). Uses `data-section` attributes + `IntersectionObserver` for scroll-based active highlighting.
- `<main class="main">` — centered content area (max 960px).
- `<div class="topbar">` — optional sticky top bar with breadcrumbs and subject-switching tabs.

### Shared assets

- **`assets/css/common.css`** — single global stylesheet (~280 lines). CSS custom properties on `:root` for theming (colors, shadows, radius). Responsive breakpoint at 768px. Defines the component classes below.
- **`assets/js/common.js`** — single global script (~60 lines). Three functions: `showAnswer(id)` (toggles answer visibility + checks correctness via `data-correct`), `switchTab(evt, tabGroup, tabContent)`, and `DOMContentLoaded` handlers for tab init and `IntersectionObserver` sidebar highlighting.
- **`assets/svg/`** — empty directory, reserved for SVG assets.

### Content component classes (defined in common.css)

| Class | Purpose |
|---|---|
| `.kp` | Knowledge point card — bordered box with heading, explanation, and `.formula` inline |
| `.exercise` | Interactive question — radio options, `.answer-btn` calling `showAnswer()`, hidden `.answer` div with `data-correct` attribute |
| `.card` | Generic content card with `.card-title` |
| `.anim-container` | Canvas/SVG animation wrapper with `.anim-controls` buttons |
| `.tabs` | Tab bar with `data-tab-group` / `data-tab-content` driven by `switchTab()` |
| `.keypoints-grid` | Responsive grid of knowledge point cards |
| `.chapter-list` | Sidebar navigation list with numbered `.ch-num` circle indicators |

### Exercise/answer mechanism

The answer system is client-side only:
1. Each question has radio inputs named `q{id}` and a hidden `<div id="answer-{id}" data-correct="A">`.
2. Clicking "Show Answer" calls `showAnswer(id)`, which toggles `.show` on the answer div.
3. If the user has selected a radio option, it compares against `data-correct` and adds `.correct` (green) or `.wrong` (red).

### File naming conventions

- **Chapters:** `ch##_topic.html` (e.g., `ch01_sound.html`, `ch03_motion_force.html`)
- **Chapter exercises:** `ch##_topic_exercises.html`
- **Yearly exams:** `exam_YYYY.html` (e.g., `exam_2024.html`)
- **Special topics:** `*_special.html` (e.g., `electricity_special.html`)
- **Subject landing:** `index.html`
- **Sub-topic chapters:** `{letter}##_topic.html` (e.g., `a01_numbers.html`, `g03_triangles.html`)

### Subject-specific patterns

- **Math:** Sub-topics `algebra/` and `geometry/` with prefixed chapter files (`a##`, `g##`).
- **Chinese:** Organized by grade (`grade7/`, `grade8/`, `grade9/`) and category (`classical/`, `poetry/`, `reading/`, `writing/`).
- **CAIE A-Level:** Organized by subject (`math/`, `physics/`, etc.), with exam papers following the pattern `{subject}_{paper}_{series}_{year}.html` (May/June + Oct/Nov, 2022-2026).
- **IELTS:** Contains `create_exams.py` and `generate_all_exams.py` — Python scripts that generate reading exam HTML files from `pdf_raw_text.txt` (~5MB source data).
- **Competition:** AMC 8/10/12 (2020-2024, A and B sets) and CPhO (preliminary/semifinal/final, 2015-2024).

### Canvas animations

Some chapter pages (e.g., `physics/ch01_sound.html`) embed inline `<canvas>` elements with inline JavaScript for physics animations. These are not extracted to shared JS files — each page self-contains its animation code.

### Encoding and language

- All files use UTF-8 encoding.
- All pages use `<html lang="zh-CN">`.
- Content follows Shanghai Education Press (沪教版) for junior high and People's Education Press (人教版) for senior high.

## Python utilities

- `check_links.py` / `check_all_links.py` — Walk all HTML files, extract `href`/`src` links, and validate they point to existing files. Run from project root.
- `ielts/create_exams.py` / `ielts/generate_all_exams.py` — Generate IELTS reading exam HTML files from metadata.

## Common tasks

### Adding a new chapter page

1. Copy an existing chapter file (e.g., `physics/ch01_sound.html`) as a template.
2. Update the `<title>`, sidebar chapter list (add the new entry, mark it `.active`), and content sections.
3. Update the parent `index.html` to include a card linking to the new chapter.
4. Run `python check_links.py` to validate all links.

### Adding a new exam paper

1. Copy an existing exam file (e.g., `physics/exam_2024.html`) as a template.
2. Update the year tabs, question content, and `data-correct` attributes.
3. Ensure each question has a unique `id` suffix for `showAnswer()` to target.

### Creating a new subject area

1. Create a new directory with an `index.html` (copy from `physics/index.html`).
2. Add the subject card to the root `index.html`.
3. Create chapter files following the naming conventions above.