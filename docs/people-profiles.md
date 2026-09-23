# PHINDER people profiles

Updated 22 September 2026 for local review. Roles supplied by the project coordinator: Fredrik Sandin (coordinator), Tommaso Dorigo (WP1), Wolfger Peelaers (WP2), Anders Mikkelsen (WP3), Patty Stabile (WP4), Pablo Martínez Ruiz del Árbol (WP5), Pietro Vischia (WP6), Lama Alkhaled (project manager).

Each author page links its biographical sources. Wolfger's optical-computing publication and Stony Brook dissertation substantiate the summary; the supplied claims about prior postdoctoral appointments and quantum optical processing were omitted because they were not independently confirmed. Pietro's existing profile was retained in substance and aligned with his current research homepage. Lama's university profile confirms her institutional affiliation and project-management role; public LinkedIn posts provided additional context and a portrait because the main LinkedIn profile blocked automated access.

## Portrait sources

| Person | Original photograph |
|---|---|
| Fredrik Sandin | https://www.ltu.se/images/200.1290fc0918d8763190a30891/1707892510557/Fredrik%20Sandin.jpg |
| Anders Mikkelsen | https://portal.research.lu.se/files-asset/166253140/AndersMikkelsen_01.jpg |
| Tommaso Dorigo | https://userswww.pd.infn.it/~dorigo/tdcrop.jpg |
| Patty Stabile | https://assets.w3.tue.nl/w/fileadmin/research_import/8de4d5d70dfcc747464fd34178166d99.jpg |
| Pietro Vischia | https://vischia.github.io/assets/avatar.jpeg |
| Pablo Martínez Ruiz del Árbol | https://ifca.unican.es/PublishingImages/FotosPersonal/PABLOMARTINEZ.jpg |
| Wolfger Peelaers | https://i.ytimg.com/vi/brO2YjjEpfM/maxresdefault.jpg (user-specified lecture thumbnail) |
| Lama Alkhaled | Author avatar from https://www.linkedin.com/posts/lama-alkhaled-6a7032257_spring-school-2026-activity-7439949236407934976-o7i8 |

The built-in imagegen tool removed backgrounds from these photographs. These are AI-assisted cutouts of source portraits, not newly commissioned photographs. Small original images, especially Pablo's and Pietro's, limit detail. Source downloads remain in `.local-dev/portraits/` for comparison; final transparent PNGs are in each author bundle. `portrait.png` serves the custom cards and profiles; `avatar.png` supports the existing People listing. Hugo creates appropriately sized WebP derivatives.

## Shared edit prompt

Remove ONLY the photographic background from the supplied portrait. Produce a clean professional head-and-shoulders cutout on a genuinely transparent RGBA background. Preserve this exact person's identity, facial features, expression, hairstyle, glasses if present, skin texture, original clothing, original colour or black-and-white treatment, and pose. Do not beautify, retouch the face, invent facial detail, change clothing, change expression or reconstruct missing anatomy. Crop to head and upper torso where necessary, keep the full head and hair, leave a small transparent margin. Remove background cleanly around hair, shoulders and glasses; no solid colour backdrop, no added shadow, no halo, no text. For low-resolution input preserve the photographic likeness rather than inventing detail. This is background removal from an existing real photograph, not creation of a new portrait.

Lama's edit additionally preserves her sunglasses and orange clothing and removes other people and signage. A second pass explicitly requested true alpha transparency because the first output had a white background.

## Layout

`/consortium/#members` now targets the eight leadership cards; internal resources use `#for-members`. `layouts/authors/list.html` supplies a matching profile layout for these eight people and preserves the theme fallback for other authors. Styling is in `assets/scss/custom.scss`.


## Collaborator portraits and leadership order

The Consortium leadership grid uses an explicit `leadership_order` field: Fredrik and Lama, WP1 and WP2, WP3 and WP4, WP5 and WP6. Collaborator cards remain text-only. The five supplied collaborator profiles now use the same author-page layout and link their biographical sources. Magnus Borgström’s affiliation is corrected to Lund University / NanoLund. Their existing author URL slugs are explicit to preserve links.

Original portraits:

- Magnus: https://portal.research.lu.se/files-asset/8129101/MagnusBorgstr_m.jpg
- Thomas: https://ieeephotonics.org/wp-content/uploads/2025/12/Thomas-Van-Vaerenbergh.webp
- Irene: https://www.ltu.se/images/200.372fd09d19c98b67b0c9bbc5/1773406329366/IMG_20260313_134730_435.jpg
- Mia: https://userswww.pd.infn.it/~tosi/mia.jpg
- Foteini: https://www.ltu.se/images/200.64257e3118d877d8daf1c4b/1707402795430/FoteiniSimistiraLiwicki.png

Portrait backgrounds were removed with the built-in imagegen tool, preserving the source faces, clothing and poses. Original downloads are in `.local-dev/collaborators/`.

Edit prompt: Remove only the background from this real person’s photograph. Preserve exactly the original face, expression, glasses, hairstyle, pose and clothing. No beautification, no changed features, no invented anatomy. Keep the original crop if the head is already cropped. Output a clean photographic cutout on genuine transparent RGBA alpha, NOT a white or checkerboard background. Remove scenery around hair and shoulders carefully, no halos, no added shadows. Head and upper torso composition suitable for a professional research profile.
