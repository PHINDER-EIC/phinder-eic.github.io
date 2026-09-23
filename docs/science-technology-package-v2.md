# Science and Technology content integration

Source: `~/Downloads/PHINDER_science_technology_content_package_v2.zip`, received 23 September 2026. Extracted review copy: `.local-dev/content-package-v2/`.

## Editorial changes

Science follows the package narrative: local optical processing, the published nanowire-neuron experiment, a planned calorimeter demonstrator, application directions and co-design. Technology explains devices and direct optical links, heterogeneous InP integration and the surrogate-assisted optimisation loop. The landing-page concept illustration remains on the landing page and is removed from Technology.

Published experiments, simulations and project objectives are distinguished in the copy. The picowatt statement refers specifically to the published neuron experiment. The author-supplied 440 × 550 micrograph is copied byte-for-byte and displayed at no more than 440 CSS pixels, without cropping or alteration. It follows its text on mobile.

Five figures are displayed: the supplied micrograph, the unaltered ACS Photonics Figure 1, and explanatory redraws of the calorimeter, InP-network and AIDO-workflow sketches. Original publication figures remain accessible. Credits and CC BY links appear with each relevant figure. Full prompt records are in `research-figure-prompts.md`; the package's source/rights notes are retained in `research-image-attribution.md`.

The package names Mia Tosi as WP1 lead, conflicting with the user's prior explicit assignment to Tommaso Dorigo. No team roles were changed in this content update.

## References

All 17 references in the package catalog are represented in the background collection. Four already existed; 13 were added, bringing the collection to 20 while retaining all seven previously selected references. Six featured papers on Science follow the package recommendation. Both BibTeX collections are rebuilt from the same 20 bundles.

Titles, authors, journal/conference names and dates for new records were checked against publisher-deposited Crossref metadata. Raw metadata is saved in `.local-dev/package-references/`. Where the package's wording differs from the deposited title, the publication record uses the deposited title. No unrelated inherited publication bundles were restored.

New entries:

- 10.1038/s41467-026-71446-4 — nanowire neuron
- 10.1021/acsphotonics.4c01375 — on-chip optical communication
- 10.1515/nanoph-2025-0035 — optical broadcasting connectivity
- 10.1088/2634-4386/acf684 — nanophotonic neuron with memory
- 10.1063/5.0066350 — InP multilayer networks
- 10.1016/j.revip.2023.100085 — differentiable instrument design
- 10.1016/j.mee.2025.112363 — multi-nanowire fabrication
- 10.1109/JSTQE.2019.2945548 — InP SOA cross-connect
- 10.3389/fnins.2020.00150 — synaptic delays
- 10.1364/OE.588175 — robust photonic tensor cores
- 10.1364/CLEO_AT.2024.ATu3J.1 — optical tensor decomposition
- 10.1088/2632-2153/ad52e7 — TomOpt
- 10.22323/1.476.1022 — AI-assisted experiment design

`/publications/` aliases the existing `/publication/` archive. Hugo HTML aliases are enabled: the inherited configuration previously disabled them in favour of host-specific redirects, which do not work in the local preview or ordinary GitHub Pages hosting.

## Editing map

- Page text: `content/science/index.md`, `content/technology/index.md`.
- Figures, captions and credits: `data/research_figures.yaml`.
- Featured papers: `data/research_publications.yaml`.
- Layout: `layouts/shortcodes/research-block.html`, `layouts/shortcodes/research-figure.html`, `layouts/partials/ph-research-figure.html`.
- Responsive appearance: `assets/scss/custom.scss`.
- New assets and source images: `static/media/research/`.
