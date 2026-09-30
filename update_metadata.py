#!/usr/bin/env python3
"""Render project.json into index.html. Optional maintenance tool; no site build needed."""
import html
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
config = json.loads((ROOT / "project.json").read_text())
escape = lambda value: html.escape(str(value), quote=True)

def url(value):
    if not value or urlparse(value).scheme not in ("https", "http"):
        raise ValueError(f"Expected a public HTTP(S) URL, got {value!r}")
    return escape(value)

def resource(key, label, description, compact=False):
    destination = config.get(key)
    if compact:
        if destination:
            return f'<a class="button secondary" href="{url(destination)}">{label}<span aria-hidden="true">↗</span></a>'
        return f'<span class="button unavailable" aria-disabled="true" aria-label="{label}: coming soon">{label}<small>Coming soon</small></span>'
    if destination:
        return f'<a class="resource-card" href="{url(destination)}"><strong>{label}</strong><p>{description}</p><span class="resource-arrow" aria-hidden="true">↗</span></a>'
    return f'<div class="resource-card unavailable" aria-disabled="true"><strong>{label} · Coming soon</strong><p>{description}</p></div>'

resources = [
    ("paperUrl", "Paper", "The paper will be available here." if not config["paperUrl"] else "Read the arXiv preprint and technical appendices."),
    ("codeUrl", "Flow-NLA code", "Code will be available here." if not config["codeUrl"] else "Public Flow-NLA project repository."),
    ("evaluationUrl", "NLA Evaluations", "Evaluation framework for activation explanations." + (" Repository availability to be confirmed; the supplied URL currently returns 404." if config.get("pending", {}).get("evaluationUrl") else "")),
    ("originalNlaUrl", "Original NLA", "The original Natural Language Autoencoder work."),
    ("githubProfile", "Sumxiaa on GitHub", "More projects and code.")
]

def author_markup(author):
    name = escape(author["name"])
    label = f'<a href="{url(author["url"])}">{name}</a>' if author.get("url") else name
    references = author.get("affiliations", [])
    if any(not isinstance(ref, int) or not 1 <= ref <= len(config["affiliations"]) for ref in references):
        raise ValueError(f'Invalid affiliation number for {author["name"]}')
    if references:
        numbers = ",".join(str(ref) for ref in references)
        label += f'<sup aria-label="affiliation {numbers}">{numbers}</sup>'
    return f'<span class="author">{label}</span>'

def bibtex_escape(value):
    chars = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#"}
    return "".join(chars.get(char, char) for char in str(value))

title = escape(config["paperTitle"])
description = escape(config["description"])
authors = config["authors"]
author_text = ", ".join(map(author_markup, authors))
affiliations = " · ".join(f'<span class="affiliation"><sup>{number}</sup> {escape(name)}</span>' for number, name in enumerate(config["affiliations"], 1))
manuscript = config.get("citationStatus") == "manuscript"
preprint = config.get("citationStatus") == "preprint"
if preprint and not all(config.get(field) for field in ("paperUrl", "paperPdfUrl", "arxivId", "arxivVersion", "arxivPrimaryClass", "paperDate", "citationYear")):
    raise ValueError("arXiv preprints need complete paper and citation metadata.")
if config.get("arxivId") and not re.fullmatch(r"\d{4}\.\d{4,5}", config["arxivId"]):
    raise ValueError("Invalid arXiv identifier.")
if config["citationType"] not in ("misc", "article", "inproceedings") or not re.fullmatch(r"[A-Za-z0-9_:-]+", config["citationKey"]):
    raise ValueError("Use a valid BibTeX type and citation key.")
citation_authors = " and ".join(bibtex_escape(a.get("bibtexName", a["name"])) for a in authors)
bibtex_fields = [f'  title = {{{bibtex_escape(config["paperTitle"])}}}', f'  author = {{{citation_authors}}}']
if config.get("citationYear"):
    bibtex_fields.append(f'  year = {{{bibtex_escape(config["citationYear"])}}}')
if preprint:
    bibtex_fields.extend([
        f'  eprint = {{{bibtex_escape(config["arxivId"])}}}',
        '  archivePrefix = {arXiv}',
        f'  primaryClass = {{{bibtex_escape(config["arxivPrimaryClass"])}}}'
    ])
if config.get("paperUrl"):
    bibtex_fields.append(f'  url = {{{bibtex_escape(config["paperUrl"])}}}')
if manuscript:
    bibtex_fields.append('  note = {Manuscript}')
bibtex = f'@{config["citationType"]}{{{config["citationKey"]},\n' + ",\n".join(bibtex_fields) + "\n}"
author_metadata = ""
for author in authors:
    author_metadata += f'\n  <meta name="citation_author" content="{escape(author["name"])}">'
    for reference in author.get("affiliations", []):
        author_metadata += f'\n  <meta name="citation_author_institution" content="{escape(config["affiliations"][reference - 1])}">'
if preprint:
    author_metadata += (
        f'\n  <meta name="citation_date" content="{escape(config["paperDate"])}">'
        f'\n  <meta name="citation_arxiv_id" content="{escape(config["arxivId"])}">'
        f'\n  <meta name="citation_pdf_url" content="{url(config["paperPdfUrl"])}">'
    )
if manuscript:
    citation_note = '<p class="citation-note">Manuscript citation. Publication details will be added when available.</p>'
elif preprint:
    citation_note = f'<p class="citation-note">arXiv:{escape(config["arxivId"] + config["arxivVersion"])} · {escape(config["citationYear"])}</p>'
else:
    citation_note = ''
blocks = {
    "head": f'''<title>{escape(config["projectTitle"])} — {title}</title>
  <meta name="description" content="{description}">
  <meta name="author" content="{escape(", ".join(a["name"] for a in authors))}">
  <link rel="canonical" href="{url(config["siteUrl"])}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{escape(config["projectTitle"])}">
  <meta property="og:title" content="{escape(config["projectTitle"])} — {title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url(config["siteUrl"])}">
  <meta property="og:image" content="{url(config["siteUrl"].rstrip('/') + '/assets/figures/trajectories.png')}">
  <meta property="og:image:alt" content="Paper figure comparing utility, source support, and writing defects for Flow-NLA and point NLA.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="citation_title" content="{title}">''' + author_metadata,
    "identity": f'<p class="paper-title">{title}</p>\n      <p class="authors">{author_text}</p>\n      <p class="affiliations">{affiliations}</p>',
    "hero-links": '<div class="resource-buttons" aria-label="Project resources">' + "".join(resource(k, "Code" if k == "codeUrl" else label, desc, True) for k, label, desc in resources[:4]) + '</div>',
    "resources": '<div class="resources-grid">' + "".join(resource(*item) for item in resources) + '</div>',
    "citation": citation_note + f'<pre><code id="bibtex" data-citation-status="{escape(config["citationStatus"])}">{escape(bibtex)}</code></pre>',
    "footer-title": f'<p>{title}</p>',
    "footer-link": f'<a href="{url(config["githubProfile"])}">Sumxiaa / GitHub <span aria-hidden="true">↗</span></a>'
}
document = (ROOT / "index.html").read_text()
for key, content in blocks.items():
    pattern = rf"(<!-- metadata:{key}:start -->).*?(<!-- metadata:{key}:end -->)"
    document, count = re.subn(pattern, lambda m: m[1] + "\n  " + content + "\n  " + m[2], document, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected exactly one metadata block for {key}")
document = re.sub(r'(data-link="originalNlaUrl" href=")[^"]*(")', lambda m: m[1] + url(config["originalNlaUrl"]) + m[2], document)
(ROOT / "index.html").write_text(document)
print("Updated index.html from project.json. Citation metadata updated.")
