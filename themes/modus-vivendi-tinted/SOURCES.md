# Modus Vivendi Tinted: sources and prompts

The palette derives from [Modus themes by Protesilaos Stavrou](https://github.com/protesilaos/modus-themes/tree/782743415b3eedac0b99db2342fb35703deb752f), pinned revision `782743415b3eedac0b99db2342fb35703deb752f`. The constant `modus-themes-vivendi-tinted-palette` in `modus-themes.el` supplies the colors; upstream's `fg-term-*` semantic mapping supplies ANSI identities.

Grove roles map to `bg-main`, `bg-dim`, `fg-main`, `fg-dim`, `blue-warmer`, and `magenta-cooler` respectively. This is a Mango Grove adaptation, not an official upstream release. Palette/configuration adaptations use GPL-3.0-or-later; the upstream license is retained in `LICENSE.palette`. Upstream code is copyright Free Software Foundation, Inc.; Protesilaos Stavrou is its author and maintainer.

The four original wallpapers were created for this collection with the built-in OpenAI imagegen tool on 2026-11-12, one independent generation call per image, without reference images. Native files are 1672 × 941 PNGs, copied byte-for-byte without resizing, retouching, or cropping. All were visually reviewed: foliage detail and spacious center, restrained sea/architecture, sparse orbital composition, and tactile study interior; no visible text, logos, or watermarks. Olive, thyme, landscape, and the study are an understated ode to Prot's Greek surroundings and philosophical curiosity, not depictions of his actual home or a claimed endorsement. To the extent rights can be granted, the generated assets are supplied under the repository's GPL-3.0-or-later terms.

## Violet Herbarium

File: `wallpapers/01-violet-herbarium.png`

Full generation prompt:

> Use case: stylized-concept. Asset type: original desktop wallpaper, wide landscape 16:9, at least 1672 by 941 pixels. Create an exquisite nocturnal botanical cyanotype-like still life: translucent olive leaves and wild thyme shadows scattered sparsely across a vast deep midnight indigo field. A few sculptural silvery olive branches enter from the lower left and upper right, leaving the large central two thirds calm and dark. Color palette anchored in Modus Vivendi Tinted: almost-black indigo #0d0e1c, slate indigo #1d2235, restrained lavender #b6a0ff and ice-blue #79a8ff highlights. Fine paper grain and dimensional leaf veins, sophisticated luminous photographic detail with matte shadow. Meditative, intellectually quiet, a subtle ode to Greek landscape and philosopher/coder Protesilaos Stavrou. No portrait, no letters, no text, no logo, no watermark, no frame, no UI. Full-bleed single finished wallpaper.

## Dusk Amphitheatre

File: `wallpapers/02-dusk-amphitheatre.png`

Full generation prompt:

> Use case: stylized-concept. Asset type: original wide 16:9 desktop wallpaper, native at least 1672 by 941 pixels. A minimalist ancient Greek open-air amphitheatre carved into a small remote island hillside, viewed from high above at the last indigo dusk. Only the lower right third contains curved pale limestone seating terraces, softened by shadows and tiny thyme plants, while the center and upper left open into quiet hazy midnight-blue sea and sky. A thin lavender dusk line on the far horizon. Modus Vivendi Tinted palette: deep indigo #0d0e1c, slate #1d2235, muted violet #b6a0ff, cool blue #79a8ff in soft reflected light, subdued stone. Rich believable mineral texture and cinematic atmospheric depth, elegant photoreal conceptual landscape with spacious negative space. Contemplation and philosophy rather than tourism; no people, no words, no logos, no artificial neon, no watermark, no frame. Single full-bleed finished wallpaper.

## Stellar Dialogue

File: `wallpapers/03-stellar-dialogue.png`

Full generation prompt:

> Use case: stylized-concept. Asset type: original wide landscape 16:9 desktop wallpaper, native at least 1672 by 941 pixels. Create a poetic astronomical still life: two very slender elliptical brushed-silver orbital rings, one tilted, suspended low at opposite edges in a deep indigo twilight void. Between them a handful of tiny distant stars form a delicate unstated dialogue, without literal constellation lines. Low on the horizon is a barely visible plum mountain ridge. Let the central expanse remain dark, spacious and tranquil, asymmetrical restrained composition. Modus Vivendi Tinted palette deep indigo #0d0e1c, slate #1d2235, lavender #b6a0ff and cool blue #79a8ff only on faint polished rims, natural soft atmospheric scattering. Tactile elegant museum installation meets astronomical photography, high detail, no excessive nebula noise. An understated philosophical ode to curiosity, no visible text, no logos, no UI, no watermark, no frame. Single full-bleed finished wallpaper.

## Plum Scriptorium

File: `wallpapers/04-plum-scriptorium.png`

Full generation prompt:

> Use case: stylized-concept. Asset type: original wide landscape 16:9 desktop wallpaper, native at least 1672 by 941 pixels. A quiet philosopher's stone writing alcove at blue hour, seen from within, with a low unpainted oak desk at lower right holding a closed indigo linen notebook, a small unlit ceramic oil lamp, and one olive sprig. A simple broad arched opening at left reveals distant layered indigo hills under a few stars. Rich plum-tinted plaster walls and gently cool reflected light, no active computer or screens. Keep upper center and central wall spacious and very dark for desktop legibility. Modus Vivendi Tinted colors: almost-black indigo #0d0e1c, slate #1d2235, restrained muted lavender #b6a0ff and ice-blue #79a8ff reflected at edges, tiny natural wood warmth. Cinematic editorial interior photography with tactile stone, linen and grain, subtle shadows, luxurious quiet. Subtle ode to Protesilaos Stavrou through study and Greek countryside, no likeness or portrait. No text anywhere, no writing, no logo, no watermark, no UI, no frame. Single finished full-bleed wallpaper.

## Wallpaper revision — 2026-11-13

Final bundle path: `wallpapers/03-stellar-dialogue.png`. Replaces the original artwork above; the earlier prompt is retained as history. Built-in image_gen, native landscape PNG, no resizing.

SHA-256: `ab8c83b3fe0cc532305cd1380c7395c18c55f7f83c54eaee8c47836782fc547d`.

Reference/edit input: modus-vivendi-tinted/wallpapers/03-stellar-dialogue.png.

Complete final prompt:

```text
Use case: precise-object-edit. Edit this desktop wallpaper. Remove BOTH large metallic elliptical rings completely, reconstruct uninterrupted natural night sky and distant mountains behind them. Preserve the dark indigo and plum palette, sparse delicate stars, low mountain silhouettes, dim lavender horizon, wide calm negative space, landscape composition and overall restrained style. Make sky seamless and natural with no circles, rings, orbital paths, devices or new objects. Output landscape 1672x941.
```
