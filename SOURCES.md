# Scientific provenance

Scientific content was verified against the manuscript’s `main.tex` and its included appendix, `sections/appendix/main_supporting_details.tex`, on 2026-09-27. Those LaTeX sources are maintained separately and are not part of this website repository. Historical section drafts were excluded. Line numbers below refer to that inspected manuscript revision.

## Copy, equations, and results

| Website content | Current manuscript source |
| --- | --- |
| Paper title | `main.tex:35–37` |
| TL;DR and three-model finding | Abstract, `main.tex:48–55`; results, `main.tex:618–625` |
| NLA pipeline, unit activation, reconstruction reward | `main.tex:164–179` |
| Utility tasks, judge inputs, hard-negative separation | `main.tex:243–257` |
| Assertion Risk and Confabulated Token Coverage | `main.tex:261–267` |
| Writing defect definitions | `main.tex:269–275` |
| Training observation, coupling not established as necessary | `main.tex:314–321` |
| Optimal normalized point loss and equal-mean example | `main.tex:405–460` |
| Flow architecture and standardization/noising | `main.tex:468–515` |
| Noise prediction, likelihood bound and integrated reward | `main.tex:539–581` |
| Joint verbalizer updates | `main.tex:583–592` |
| Late-training averaging definition | `main.tex:598–602` |
| Writing-defect changes +0.23–0.32 vs +0.71–1.00, baseline confabulation rises up to 11 pp | `main.tex:618–625` |
| Empirical/theoretical limitations | `main.tex:642` |
| Exact target model identities, including Gemma-3-12B-it | Included appendix, lines 94–96 |
| Absolute selected-checkpoint table | Included appendix, lines 27–64 |
| Checkpoint selection (highest mean utility among updates 1300–1600) | Included appendix, lines 210–220 |
| Excluded source-support claims and token-span union | Included appendix, lines 197–203 |
| Hard-negative separation is benefit plus mismatch penalty | Included appendix, lines 173–179, 258–268 |

The absolute scores in the expandable table are not substituted for the late-training averaged changes. The website does not estimate numbers from pixels, imply elimination of confabulation, or claim mechanistic faithfulness. The unit-norm condition is retained in the point-loss equation. The reward is presented as a likelihood-bound term, not an exact likelihood.

## Figure mapping

| Website output | Original manuscript file under `figures/` | Treatment |
| --- | --- | --- |
| `training-trends.webp` / `.png` | `posthoc/nla_fve_combined_defects_risk_annotated.pdf` | Direct high-resolution PDF rendering, lossless WebP |
| `hard-negative.webp` / `.png` | `posthoc/hard_negative_separation_annotated.pdf` | Direct high-resolution PDF rendering, lossless WebP |
| `same-mean.webp` / `.png` | `equal_mean_reconstruction.pdf` | Direct high-resolution PDF rendering, lossless WebP |
| `architecture.webp` / `.svg` | `introfig_flownla.drawio.svg` | Preserved vector export, editor metadata removed; light color scheme fixed; faithful browser-rendered WebP for predictable inline display |
| `trajectories.webp` / `.png` | `six_panels_smoothed.pdf` | Direct high-resolution PDF rendering, lossless WebP |
| `late-training.webp` / `.png` | `flow_vs_nla_dumbbell_cropped.pdf` | Direct high-resolution PDF rendering, lossless WebP |

No PDF-page screenshots are used: these are direct conversions of standalone figure files. No original manuscript assets were changed. WebP raster copies were verified pixel-identical to their PNG renders. Architecture remains available as SVG through its full-size link. Figure dimensions and file sizes are recorded in `assets/figures/manifest.json`.

The evaluation overview from `figures/evaluation_overview.tex` is reconstructed as accessible HTML cards preserving each judge’s inputs, task, and metrics. The initial NLA pipeline is an HTML diagram of the pipeline described in the manuscript. No invented qualitative comparison is included: local examples do not establish a paired point-NLA versus Flow-NLA comparison.

All figure files, including unused variants and `image.png`, were inspected. The unreferenced `image.png`, older `NLA-Flow` architecture, unannotated alternatives, and historical results plots are deliberately not used. The active full-results figure is `six_panels_smoothed.pdf`, not the nonexistent `full_results.pdf` mentioned in an older section draft.

## Metadata and external resources

Public metadata was supplied by the project owner: Gert Lek (Université de Neuchâtel), Zixuan Xia (Universität Bern), Pin-Yu Chen (International Business Machines (IBM)), and Lydia Chen (Université de Neuchâtel), in that order. The public project repository is `https://github.com/Sumxiaa/flow-nla`. The paper URL and publication details are not yet available; the page labels the paper “Coming soon” and provides a manuscript BibTeX entry without inventing a publication year or URL.

The supplied project links are retained exactly:

- [Original NLA](https://transformer-circuits.pub/2026/nla/)
- [NLA Evaluations](https://github.com/Gertlek/nla-evaluations)
- [Sumxiaa](https://github.com/Sumxiaa)

The original NLA page was inspected for research presentation. The supplied MISHAP-Bench reference returned `folder_not_supported` during retrieval and could not be visually inspected. The page uses an independent editorial layout.

KaTeX 0.16.22 is vendored with its MIT license. The favicon is a simple typographic project mark. No third-party photographs, generated scientific images, or fabricated citations were added.
