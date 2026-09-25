# PHINDER concept implementation

The local redesign uses a single midnight navy palette with violet, gold and white accents. Outfit is self-hosted under `static/fonts/`; its SIL Open Font License is included alongside the font. The navigation logo is a recoloured, tightly framed version of the repository's existing SVG, saved as `static/media/phinder-nav.svg`. The original is unchanged.

## Illustrations

Generated using the built-in imagegen tool. These are conceptual illustrations, not photographs of a developed device or validated clinical results. The originals remain in the image-generation output directory; the website copies are optimised WebP assets:

- `static/media/chip-hero.webp`
- `static/media/particle.webp`
- `static/media/proton.webp`
- `static/media/chemistry.webp`

### Hero prompt

Create one standalone website hero illustration, no text, no typography, no logo, no UI. Wide cinematic 3D scientific concept render of a photonic neuromorphic chip: slightly tilted rectangular dark indigo silicon platform in perspective with delicate circuit traces, gold metallic nanoscale components, two ring-shaped resonator arrangements, brilliant violet and electric lavender optical paths flowing in from left and through chip to right. Nearly black midnight navy #060e23 background, restrained violet atmospheric particles, highly polished realistic scientific visualization, crisp details, elegant premium editorial lighting. Chip fills right two thirds, left third dark negative space. Landscape 1536x1024. This is conceptual illustrative art, not an engineering diagram. Save output for website project.

### Particle physics prompt

Wide scientific concept illustration of a cylindrical particle detector with a brilliant gold collision at its center and fine violet and gold particle tracks radiating outward, midnight navy background, elegant cinematic 3D render, no text or labels, landscape.

### Proton imaging prompt

Wide scientific concept illustration of proton imaging: translucent abstract human torso cross section with a small violet and gold focused beam region, sophisticated medical visualization, midnight navy and muted silver with restrained violet glow, no text or labels, no claims of a real scan, landscape.

### Chemistry prompt

Wide scientific concept illustration of a molecular structure with glasslike violet spheres and slender bonds, shallow depth of field, midnight navy background, lavender highlights, elegant polished scientific 3D render, no text or labels, landscape.

## Editing map

- Homepage and destination layout: `layouts/partials/ph-page.html`.
- Shared navigation and footer: `layouts/partials/components/headers/navbar.html`, `layouts/partials/site_footer.html`.
- Responsive styling: `assets/scss/custom.scss`.
- Destination copy: `content/science/`, `content/technology/`, `content/use-cases/`, `content/consortium/`.
- Use-case cards: `data/usecases.yaml` and `layouts/partials/ph-usecases.html`.
- Menu: `config/_default/menus.yaml`.

Existing publication and people URLs are retained. Clearly obsolete demo pages and the inherited MODE submission form are draft-only. MODE-related scientific material remains for editorial review. Internal member resources have no configured portal URL; the Consortium page directs members to the project manager.

The homepage now displays the user-approved concept targets: <100 ps temporal resolution and <1 fJ/spike ultra-low energy. The highlights section is labelled as project research objectives.


## Nanowire illustration revision

The homepage and Technology page now use `static/media/chip-nanowires.webp`, edited with the built-in imagegen tool. The previous `chip-hero.webp` is preserved. The revised concept includes flat transfer-printed nanowires in two radial clusters, an input nanowire array, and programmable InP photonic waveguide connections.

The favicon uses only the first three vector groups of the existing PHINDER logo, with no lettering, on a navy rounded square. Editable source: `static/media/phinder-symbol.svg`. Raster outputs: `assets/media/icon.png`, `static/media/icon.png`, and `static/favicon.ico`. Hugo generates the browser and touch-icon sizes from the asset.

The News LinkedIn section links to the user-provided `https://www.linkedin.com/company/123084153/`. LinkedIn blocked direct verification of that numeric ID (HTTP 999). A public PHINDER EIC kickoff post confirms the project account's human-readable address as `https://www.linkedin.com/company/phinder-eic/`, but its public HTML did not expose a matching numeric company ID.


## MZI and cylindrical nanowire refinement

The current illustration is `static/media/chip-mzi.webp`, refined from the previous nanowire illustration with the built-in imagegen tool. The requested features are an evenly spaced input antenna array with systematically varied in-plane orientations, cylindrical nanowires, discrete incoming photon pulses, MZI-inspired waveguide interconnects and more realistic wafer surface detail. The edit prompt is recorded in `docs/chip-mzi-prompt.md`. Previous artwork variants are preserved.

The homepage eyebrow is removed. The integration highlight reads “III-V + InP” / “HETEROGENEOUS INTEGRATION”; the hero caption reads “PHOTONIC NEUROMORPHIC DETECTOR CONCEPT”.

EISMEA remains in the footer disclaimer. The [official EISMEA communication toolkit](https://eismea.ec.europa.eu/communication-toolkit_en), checked 22 September 2026, explicitly names European Innovation Council and SMEs Executive Agency (EISMEA) in its recommended disclaimer.


## Y-shaped inputs and electronic readout

The current homepage and Technology illustration is `static/media/chip-y-nanowires.webp`, edited with the built-in imagegen tool. It shows one row of Y-shaped cylindrical nanowire triples, left-facing receiving arms and right-facing emitter stems coupled to InP waveguides, photon exchange across the centres of both radial clusters, and gold electrical interconnects to a small output IC. The previous versions remain available. The final edit prompt is in `docs/chip-y-nanowires-prompt.md`.

The integration highlight now reads “III-V NWs + InP”.


## Radial photon propagation and selected background

The current artwork on both pages is `static/media/chip-radial-pulses.webp`. This built-in imagegen edit aligns photon trajectories through the cluster centres with the axes of emitting and receiving nanowires. Prompt: `docs/chip-radial-pulses-prompt.md`.

The publication collection and both BibTeX files now contain exactly seven user-selected background references: arXiv 2603.26613, arXiv 2601.07859, 10.1016/j.revip.2025.100120, and 10.3390/particles8020052, 10.3390/particles8020058, 10.3390/particles8020040, 10.3390/particles8020047. The other 50 page bundles (including one duplicate of a retained DOI) were removed. Science and the publication archive use the heading “Relevant background”.


## Optical and electrical readout

The landing-page illustration is `static/media/chip-poster-original-waves.webp`. It preserves the original transparent chip artwork embedded in `PHINDER_rollup_v1.pptx` and places it unchanged over a new wide light-wave background inspired by the poster. Prompt and provenance: `docs/chip-poster-original-waves-prompt.md`. The preceding interpretation remains available as `static/media/chip-rollup-guided.webp` for rollback.

The previous `static/media/chip-dual-readout.webp` remains available as a rollback asset. Its output IC was replaced by two banks of flat square electrical contact pads and three central fibre-optic outputs. Prompt: `docs/chip-optical-electrical-output-prompt.md`.
