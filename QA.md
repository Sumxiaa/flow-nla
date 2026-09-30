# Initial publication verification — 2026-09-27

## Public metadata

- Exact ordered authors: Gert Lek¹, Zixuan Xia², Pin-Yu Chen³, Lydia Chen¹.
- Exact affiliations: ¹ Université de Neuchâtel; ² Universität Bern; ³ International Business Machines (IBM).
- Visible author-affiliation superscripts, general author metadata, citation author/institution metadata, and BibTeX agree with `project.json`.
- Public project/code link: `https://github.com/Sumxiaa/flow-nla`.
- Canonical and OpenGraph URLs use `https://sumxiaa.github.io/flow-nla/`.
- The paper control is disabled and says “Coming soon.” No paper URL or publication year is invented. The valid manuscript BibTeX entry includes the four real authors and omits unknown fields.
- No visible author placeholders or review-only wording remain.

## Scientific integrity

The initial site was checked against the active manuscript and included appendix, including all 36 numerical cells in the selected-checkpoint results table. This publication update changes metadata and affiliation presentation only: HTML outside the generated metadata blocks is byte-identical to the initial website commit, equations are unchanged, and figure assets are unchanged. An independent read-only audit confirmed author order, Unicode affiliation names, scientific preservation, and metadata regeneration consistency.

## HTTP and browser checks

The website is served directly at `http://127.0.0.1:8000/`. A second local preview at `http://127.0.0.1:8001/flow-nla/` reproduces the GitHub Pages project prefix.

- All 46 tracked website files returned HTTP 200 and byte-matched their disk contents at both URL roots. This includes CSS, JavaScript, JSON, six inline figures, full-size figure targets, favicon, and all local math fonts.
- At both paths, the root response is `index.html`; no repository directory listing or `website/` nesting is required.
- The in-app browser displayed the final desktop and 390px mobile layouts correctly. Author and affiliation groups wrap without splitting their superscripts from their names.
- The mobile page has no horizontal page overflow. Wide scientific figures and tables retain their existing internal scrolling behavior.
- All seven KaTeX expressions render. The browser console reported no warnings or errors during the release check.
- The BibTeX copy action succeeds and displays “Manuscript BibTeX copied.” Its manual-selection fallback remains available when clipboard access is unavailable.
- JavaScript syntax and Git whitespace checks pass. Regenerating metadata produces consistent static HTML.
- `project.json` is available over HTTP; the page has no runtime metadata fetch dependency.
- The initial complete-site QA also covered 1440px desktop, 768px tablet, 320px mobile, expanded technical disclosures, keyboard navigation, disabled JavaScript, reduced motion, 200% text size, and blocked external asset requests.

## External links

| Resource | Verified response |
| --- | --- |
| Flow-NLA repository | HTTP 200 |
| Sumxiaa GitHub profile | HTTP 200 |
| Original NLA | HTTP 200 |
| NLA evaluation repository | HTTP 404; the exact supplied URL is retained with an availability note |

## Repository layout

The standalone repository root is the local website directory, with branch `main` and origin `https://github.com/Sumxiaa/flow-nla.git`. Its tracked tree contains only website files and documentation; no LaTeX manuscript files or enclosing `website/` directory are included. `.nojekyll` is present. GitHub Pages should serve `main` from `/(root)` as documented in `DEPLOY.md`. This verification report records source readiness; live deployment status is reported separately after the push.

## arXiv preprint update — 2026-09-30

The site's Paper links now lead to `https://arxiv.org/abs/2609.33702v1`. The preprint's submission date, `cs.CL` category, and arXiv identifier were checked against the public arXiv record. The versioned PDF URL returned HTTP 200. The generated BibTeX and citation metadata now identify the 2026 arXiv preprint; the obsolete “Coming soon” paper state is gone.

The website loaded in the browser at both `http://127.0.0.1:8000/` and `http://127.0.0.1:8001/flow-nla/`. The browser showed the linked paper and preprint citation, the Copy BibTeX button reported “BibTeX copied,” and the browser console had no warnings or errors at either path. The root, `project.json`, and all 17 relative CSS, JavaScript, image, and favicon paths referenced by the HTML returned HTTP 200 at both URLs. Regenerating `index.html` from `project.json` and the Git whitespace check passed. Scientific sections, figure assets, styles, and relative paths were unchanged by this update.
