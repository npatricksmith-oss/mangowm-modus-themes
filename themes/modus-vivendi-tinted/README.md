# Modus Vivendi Tinted

A dark Indigo desktop built from Protesilaos Stavrou's Modus Vivendi Tinted palette. White text, cool blue focus, and lavender accents sit on opaque indigo surfaces. Four original wallpapers explore botanical observation, Greek dusk, astronomy, and a quiet place for thought.

| Wallpaper | Study |
| --- | --- |
| Violet herbarium | Translucent olive leaves and thyme on indigo paper. |
| Dusk amphitheatre | Limestone seating above a still sea at violet dusk. |
| Stellar dialogue | Two silver orbital forms in a sparse night sky. |
| Plum scriptorium | A stone writing alcove overlooking layered hills. |

All four are native 1672 × 941 PNGs. Source attribution and the complete built-in imagegen prompts are in [SOURCES.md](SOURCES.md).

Validate the portable folder before importing it:

```sh
mango-grove validate themes/modus-vivendi-tinted
mango-grove import themes/modus-vivendi-tinted
```

After import, choose **Modus Vivendi Tinted** in Grove. For an isolated CLI trial:

```sh
mango-grove --root /tmp/modus-vivendi-tinted-demo import themes/modus-vivendi-tinted
mango-grove --root /tmp/modus-vivendi-tinted-demo preview modus-vivendi-tinted --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove --root /tmp/modus-vivendi-tinted-demo apply modus-vivendi-tinted --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker --wallpaper 0 --lock-wallpaper 1 --login-wallpaper 2
mango-grove --root /tmp/modus-vivendi-tinted-demo undo
```

Use a fresh isolated root if a previous import already exists. These commands omit live reload. The theme includes terminal, Waybar, Fuzzel, Hyprlock, and ReGreet fragments. Grove generates MangoWM colors and its own interface from the palette; Mango Power Menu reads Grove's saved power palette. Chrome and T3 Code are excluded from the component selection.

All four terminals are forced opaque, including both Foot color modes, to preserve text contrast over every wallpaper. ANSI slot identities follow upstream, so software that hard-codes black or white text may need its own configuration. Hyprlock receives the usual `$grove_*` roles with opaque colors and a surface-colored input fill. Grove preserves your Hyprlock layout; that layout must use the roles to benefit, and any hard-coded alpha or transparent input styles remain under your layout's control. ReGreet uses opaque inputs and local text backplates. Login integration requires Grove's existing greeter setup, and terminal applications read the palette when their configuration reloads.

Palette/configuration adaptations are GPL-3.0-or-later. See [LICENSE.palette](LICENSE.palette) and [SOURCES.md](SOURCES.md). This adaptation is not an official Modus release and implies no endorsement by Prot.
