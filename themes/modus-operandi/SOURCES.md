# Modus Operandi sources

## Palette and license

The palette is by **Protesilaos (Prot) Stavrou**, from
[protesilaos/modus-themes](https://github.com/protesilaos/modus-themes), pinned to commit
`782743415b3eedac0b99db2342fb35703deb752f`.
The source is [`modus-themes.el`](https://github.com/protesilaos/modus-themes/blob/782743415b3eedac0b99db2342fb35703deb752f/modus-themes.el), constant
`modus-themes-operandi-palette`, and its common terminal mappings. Upstream copyright and
GPL-3.0-or-later terms are preserved in `LICENSE.palette`; the repository's GPL license
also applies to this port. This is an independent adaptation, without an endorsement claim.

| Grove role | Upstream role |
| --- | --- |
| background | bg-main |
| surface | bg-dim |
| foreground | fg-main |
| muted | fg-dim |
| accent | blue-warmer |
| secondary | magenta-cooler |

ANSI slots reproduce upstream `fg-term-*`: black, red, green, yellow, blue, magenta,
cyan, white, followed by their bright variants. ANSI white remains intentionally white;
it can be invisible when applications explicitly print white on the white background.
This port preserves that upstream semantic mapping rather than silently remapping it.
The primary text and semantic accents are the legible defaults; no universal AAA claim
is made for arbitrary ANSI foreground/background combinations or arbitrary wallpaper overlays.

## Original wallpapers

Generated on 2026-11-12 with OpenAI's built-in **image_gen** tool, one fresh generation
per image, with no input references. All four PNGs are native **1672 × 941** output;
none were enlarged, cropped, or recolored. The four images were visually inspected.
The generated assets are distributed under the repository's GPL-3.0-or-later terms to
the extent rights apply. No third-party photographs are included.

The limestone, olive trees, and quiet study form a small visual ode to Prot's thoughtful
craft. These are imagined scenes, not depictions of his actual home or property.

### Courtyard of clarity — `wallpapers/01-courtyard.png`

Complete generation prompt:

> Use case: stylized-concept. Asset type: original desktop wallpaper for Modus Operandi, landscape 16:9, 3840x2160 if possible. Primary request: a quiet Mediterranean limestone courtyard, an architectural meditation on clarity and thoughtful simplicity, a subtle tribute to philosopher and theme author Protesilaos Stavrou. Style: refined tactile architectural photography with sculptural composition, realistic chalk-white limestone and white plaster, crisp deep graphite shadows, a single restrained ultramarine-blue doorway, tiny violet wildflowers. Composition: wide view, one off-center arch, open calm pale space over most of the frame, believable material microtexture, no clutter, balanced shadow planes. Lighting: clean late-morning sunlight, white balance neutral, no sepia or beige cast, primary impression white and cool silver-gray with sparse blue. No people, no text, no letters, no logos, no watermarks, no desktop UI. Make a polished single full-frame wallpaper, not a collage or contact sheet.

### Paper and thought — `wallpapers/02-paper-relief.png`

Complete generation prompt:

> Use case: stylized-concept. Asset type: original landscape 16:9 desktop wallpaper for the Modus Operandi light theme, 3840x2160 if possible. Primary request: a meditative sculptural paper relief composed of folded white handmade paper forming one elegant continuous wave and a thin ultramarine blue cut-paper arc, as an ode to clear thought and careful craft. Style: gallery-grade macro still life, photoreal tactile cotton rag paper fibers, refined minimalist design with real dimensional folds and soft contact shadows. Composition: full-frame wide horizontal, visual detail concentrated in the lower-right third, broad calm white space, occasional cool graphite shadows, a tiny violet paper edge is the only second accent. Lighting: neutral clean daylight, bright white and pale silver gray, no cream, no yellow cast. Avoid clutter. No text, no lettering, no books, no logos, no watermarks, no people, no UI. One finished wallpaper image, not a collage.

### Olive paths — `wallpapers/03-olive-paths.png`

Complete generation prompt:

> Use case: photorealistic-natural. Asset type: original 16:9 landscape desktop wallpaper for Modus Operandi light theme, 3840x2160 if possible. Primary request: a serene Cypriot olive grove on a pale limestone hillside beneath a nearly white high bright sky, a subtle place-based ode to Protesilaos Stavrou and reflective walks. Style: refined fine-art landscape photography, natural and quiet, tactile silver olive leaves and dark graphite trunks, chalk-white stone terraces, distant hazy blue sea. Composition: wide, low horizon, few carefully spaced olive trees, broad sky and gentle open negative space, rolling contours, understated detail. Color: mostly crisp whites and cool silver grays, restrained olive green, a sliver of ultramarine horizon, no golden beige tint. Lighting: soft clear late-morning Mediterranean daylight, gentle realistic shadows. No people, no buildings, no text, no letters, no logos, no watermarks, no UI; one continuous polished landscape, not a collage.

### A place to think — `wallpapers/04-study.png`

Complete generation prompt:

> Use case: stylized-concept. Asset type: original landscape 16:9 desktop wallpaper for Modus Operandi light theme, 3840x2160 if possible. Primary request: a sunlit philosopher's study, a quiet white plaster room with a simple pale stone writing desk, one closed unmarked graphite cloth notebook, a fountain pen, a small ultramarine ceramic cup, and a single olive twig. A modest ode to the care and clarity of Protesilaos Stavrou's work, without depicting a real person's actual home. Style: polished photoreal editorial interior still life, tactile limestone, linen, handmade ceramic, clean refined geometry. Composition: wide uncluttered view, desk in lower right, open white wall over most of the image, soft diagonal window shadow, distant tiny violet flower. Lighting: pure neutral daylight and cool gray shadows, predominantly white, black and restrained blue, no beige wash. No people, no visible writing, no lettering, no logos, no watermarks, no desktop UI, no collage.
