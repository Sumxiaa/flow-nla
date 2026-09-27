# Flow-NLA project website

Static source for [Sumxiaa/flow-nla](https://github.com/Sumxiaa/flow-nla), hosted at [sumxiaa.github.io/flow-nla/](https://sumxiaa.github.io/flow-nla/). No frontend build or backend is needed. KaTeX and its fonts are included locally.

## Repository layout

This directory is the Git repository root. Publish its contents directly; do not nest them inside another `website/` directory and do not include the manuscript sources.

```text
index.html
styles.css
script.js
project.json
update_metadata.py
.nojekyll
DEPLOY.md
SOURCES.md
QA.md
assets/
  figures/
  icons/favicon.svg
  vendor/katex/
```

## Local preview

From the repository root:

```sh
python3 -m http.server 8000 --bind 0.0.0.0
```

Open [the HTTP root](http://127.0.0.1:8000/). Keep the server running while reviewing; stop it with Ctrl+C when finished. The correct path is `/`, not `/website/`. Relative asset paths also work under the GitHub Pages project prefix `/flow-nla/`.

`project.json` is a metadata source, not a runtime fetch dependency. The page is statically rendered, and `/project.json` is available for inspection over HTTP.

## Metadata and citation updates

Edit `project.json`, then run:

```sh
python3 update_metadata.py
```

This refreshes the static HTML, author-affiliation superscripts, search/social metadata, resource links, and BibTeX. It is an optional maintenance tool, not a hosting build step.

The verified author order is Gert Lek¹, Zixuan Xia², Pin-Yu Chen³, Lydia Chen¹, with ¹ Université de Neuchâtel, ² Universität Bern, and ³ International Business Machines (IBM). Author objects contain a `name`, `bibtexName`, and one-based `affiliations` references.

The public code/project URL is `https://github.com/Sumxiaa/flow-nla`. Keep `paperUrl` null until the public manuscript URL is available; the Paper control then displays “Coming soon.” Add the confirmed `citationYear` and publication details when available. The current valid `@misc` entry uses real authors and a manuscript note, omitting unknown fields. Do not infer publication or acceptance from the manuscript template.

The supplied evaluation repository remains linked at `https://github.com/Gertlek/nla-evaluations`. If its recorded availability issue is resolved, remove `pending.evaluationUrl` and regenerate metadata to remove the availability note.

## GitHub Pages

Use the existing `origin` remote `https://github.com/Sumxiaa/flow-nla.git` and branch `main`. Preview and review changes, then commit and push from this directory:

```sh
git status
git add index.html styles.css script.js project.json update_metadata.py assets .nojekyll DEPLOY.md SOURCES.md QA.md
git commit -m "Update Flow-NLA project website"
git push origin main
```

In the repository, choose **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**. The included `.nojekyll` serves the static files directly. Once the Pages build completes, the site is available at the project URL above. No custom Actions workflow is required.

See [GitHub’s publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) for these settings. Page availability depends on a successful push and Pages configuration; the URL alone does not indicate deployment status.

## Maintaining scientific content

Edit prose and captions in `index.html`, equations and interactions in `script.js`, and visual styles in `styles.css`. Preserve the figure sources and definitions listed in `SOURCES.md`. Check mobile and desktop layouts, resource paths, the browser console, and citation copying before pushing changes.
