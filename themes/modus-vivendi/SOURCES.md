# Modus Vivendi sources and artwork

## Palette and license

Palette author: **Protesilaos Stavrou**. This port uses the original Modus Vivendi colors from [protesilaos/modus-themes](https://github.com/protesilaos/modus-themes), pinned to commit `782743415b3eedac0b99db2342fb35703deb752f`.

Source: [`modus-themes.el`, `modus-themes-vivendi-palette`](https://github.com/protesilaos/modus-themes/blob/782743415b3eedac0b99db2342fb35703deb752f/modus-themes.el). Copyright (C) 2019–2026 Free Software Foundation, Inc.; author and maintainer Protesilaos Stavrou. Source and this derivative bundle use GPL-3.0-or-later; the complete license is included in `LICENSE.palette` and at the repository root.

Grove role mapping: `background=bg-main`, `surface=bg-dim`, `foreground=fg-main`, `muted=fg-dim`, `accent=blue-warmer`, `secondary=magenta-cooler`. The ANSI sequence follows the upstream `fg-term-*` mappings: black, red, green, yellow, blue, magenta, cyan, white, followed by their bright forms. Fixed grayscale roles are `#000000`, `#a6a6a6`, `#595959`, `#ffffff`; semantic colors resolve through this theme's palette.

Terminal overrides retain exact ANSI colors and force opaque backgrounds. Hyprlock uses fully opaque semantic text roles and an opaque `$grove_glass` input surface when the user's layout uses it. ReGreet uses opaque input surfaces and explicit text colors. MangoWM, Waybar, Fuzzel, Grove's picker, and the power-menu palette use Grove's native generators from the same palette. Chrome and T3 Code are intentionally excluded from the recommended component selection. They have no bundle overrides.

The pure black terminal role remains black for upstream fidelity; terminal applications that explicitly request black text on black backgrounds need their own semantic handling. Upstream Modus accessibility goals are not a blanket WCAG guarantee for arbitrary applications or transparent desktop layouts.

## Four original nocturnes

These images were generated on 2026-11-12 with the built-in **image_gen** tool, one new-image call per image, without reference images. All final files are original native **1672 × 941 PNGs**, approximately 16:9, with no resizing or postprocessing. No third-party photo or illustration was used. The olive grove, blank notebook, and quiet geometry are an affectionate conceptual ode to contemplation and to Prot's work, not a depiction of a real private place or person. This is an independent port, not an upstream endorsement.

All four were visually inspected for coherent composition, palette, clean edges, absence of text/watermarks, and dark central negative space. They were also decoded by Grove's bundle validation; PNG chunk checksums and dimensions were independently verified.

### 1. Moonlit grove

Final bundle path: `wallpapers/01-moonlit-grove.png`.

SHA-256: `9472149a09e04f17831d5aa1b5838d5b080054adf8a094e6b8be770a898f2ebf`.

Complete generation prompt:

```text
Use case: stylized-concept
Asset type: wide 16:9 desktop wallpaper, preferably 2560 by 1440 or the highest native landscape resolution.
Primary request: a moonlit Mediterranean olive grove, a quiet ode to contemplation and the Greek philosopher and free-software author Protesilaos Stavrou, for the Modus Vivendi dark desktop theme.
Scene: ancient olive trunks and delicate silver leaves at the far left and right edges, a low rocky path vanishing into distant hills, one tiny pale moon high off center. The entire middle third is deep nearly black open night, softly textured and unobstructed so pale lock-screen type remains readable.
Style: tactile fine-art nocturne, layered ink wash and subtle photographic material detail, sophisticated and restrained, no cartoon effects.
Color palette: mostly pure black #000000 and charcoal #1e1e1e, muted silver #a6a6a6, very restrained icy blue #2fafff, cyan #00d3d0 and pale lavender #b6a0ff reflections on leaves. No vivid warm glow.
Composition: panoramic landscape, low horizon, asymmetrical trees framing broad negative space, subtle depth, restful usable wallpaper rather than a busy illustration.
Constraints: full-bleed image, no text, no letters, no logos, no watermark, no people, no collage, no frames. Keep the middle third dark and even.
```

### 2. Celestial reason

Final bundle path: `wallpapers/02-celestial-reason.png`.

SHA-256: `de98d37c913ccdd06e71d93a50e1b0dcd1fe2ab9ad0da18d24e06bfea59fa521`.

Complete generation prompt:

```text
Use case: stylized-concept
Asset type: full-bleed wide 16:9 desktop wallpaper, highest native landscape resolution.
Primary request: Celestial Reason, a restrained abstract astronomical sculpture for the Modus Vivendi dark desktop theme.
Scene: a delicate armillary sphere made of charcoal ceramic rings with thin polished silver and faint cyan edges, suspended in immense black space. Place the sculpture in the rightmost third; two distant pinprick stars toward the upper left, the center stays almost black and open. No literal zodiac or writing.
Style: museum-quality tactile 3D still life with fine-grained ink-black background, soft grazing light, architectural elegance and believable materials rather than neon sci-fi.
Color palette: black #000000, charcoal #1e1e1e, silver #a6a6a6 and white #ffffff, narrow accents of icy blue #2fafff and lavender #b6a0ff; mostly darkness.
Composition: panoramic, small asymmetrical orbital form in right third, ample negative space across center and left. Rich depth from subtle ring shadows and barely visible black-on-black arcs.
Constraints: a single unified image, no text, no symbols, no labels, no logos, no watermark, no people, no border, no collage. Keep central third dark and visually quiet for lock-screen typography.
```

### 3. Ink archipelago

Final bundle path: `wallpapers/03-ink-archipelago.png`.

SHA-256: `d57c464973ab7c89db3911587a081258b0d0198df9fbb1f884d559c2609f73d0`.

Complete generation prompt:

```text
Use case: stylized-concept
Asset type: wide 16:9 desktop wallpaper, highest native landscape resolution.
Primary request: Ink Archipelago, an atmospheric imaginary Mediterranean island landscape in near-black ink, for the Modus Vivendi dark desktop theme.
Scene: deep charcoal islands rising from a still black sea, layered mineral ridges and a few narrow silver shorelines. The land lies along the lowest quarter and the left edge; broad dark mist and empty night occupy the central third and most of the upper half. A hairline icy-blue reflection far to the right supplies a restrained accent. No sun, no bright central moon.
Style: contemporary fine-art ink landscape with tactile paper grain, subtle embossed geological depth, delicate diluted ink edges and slow luminous fog. Richly dimensional yet restrained.
Color palette: black #000000, charcoal #1e1e1e, cool gray #535353, silver #a6a6a6; tiny accents of blue #2fafff and cyan #00d3d0, no warm colors.
Composition: panoramic and spacious; very low horizon, sculpted forms near edges, uninterrupted dark middle area suitable for pale lock-screen text.
Constraints: no typography, no characters, no logos, no watermark, no frames, no collage, no people, no buildings. One cohesive polished artwork.
```

### 4. The unwritten study

Final bundle path: `wallpapers/04-unwritten-study.png`.

SHA-256: `f4665d97a1159d23af9ada2c2b3b2596ff1b2804a12061408e8f783176bb78eb`.

Complete generation prompt:

```text
Use case: stylized-concept
Asset type: full-bleed wide 16:9 desktop wallpaper, highest native landscape resolution.
Primary request: The Unwritten Study, a quiet imaginary philosopher's desk at night, an ode to thoughtful writing and free software, for Modus Vivendi.
Scene: a low dark basalt desk across the lowest quarter of the frame; at the lower right a small closed linen notebook, an unmarked ivory sheet with no writing, a slender silver fountain pen and one cut olive twig. At the far left a sliver of a charcoal stone window jamb. Beyond it are distant night hills with a faint blue horizon. The center and upper two thirds remain deep nearly black, softly textured empty wall and night. No bright lamp, no obvious computer.
Style: cinematic tactile still-life photography with painterly restraint, exquisite matte stone and linen surfaces, carefully controlled soft moonlight from the left, meditative and minimal.
Color palette: black #000000, charcoal #1e1e1e, subdued silver #a6a6a6 and small ivory highlights, minute icy blue #2fafff and muted lavender #b6a0ff reflections. No warm pools of light.
Composition: panoramic, small objects along the lower right margin, vast quiet central negative space for white lock-screen typography.
Constraints: no writing, no letters, no logos, no watermark, no people, no monitor UI, no frames, no collage. A cohesive polished artwork, rich depth but predominantly dark.
```
