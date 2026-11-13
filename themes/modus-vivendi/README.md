# Modus Vivendi

A faithful black-and-white Modus Vivendi palette with blue focus and lavender
secondary accents, adapted for Mango Grove. Four original nocturnes explore an
olive grove, an armillary sculpture, an ink archipelago, and an unwritten study.
They are a quiet tribute to Protesilaos Stavrou's themes and thoughtful work.

## Import and apply

```sh
mango-grove validate themes/modus-vivendi
mango-grove import themes/modus-vivendi
mango-grove preview modus-vivendi --components ghostty,foot,alacritty,kitty,mango,waybar,fuzzel,hyprlock,regreet,picker,wallpaper
mango-grove apply modus-vivendi --components ghostty,foot,alacritty,kitty,mango,waybar,fuzzel,hyprlock,regreet,picker,wallpaper --wallpaper 0
```

Choose only the applications you use. Chrome and T3 Code are excluded from these
commands. In the picker, leave those two components unchecked. Grove generates
its own interface and Mango Power Menu state from the same palette when `picker`
and `mango` are selected. The power menu must already be configured to read Grove.

Wallpaper indices 0–3 are Moonlit grove, Celestial reason, Ink archipelago, and
The unwritten study. Set `--lock-wallpaper` and `--login-wallpaper` independently
if desired. Live reload is opt-in (`--reload`). Existing Grove greeter setup is
required for a real ReGreet apply; no setup or desktop changes are made by importing.

All four terminal fragments set opacity to 1 to preserve contrast. Foot fragments
target modern Foot's `colors-dark` and `colors-light` sections. Hyprlock sets the
standard `$grove_*` variables, including opaque input-surface and text roles;
the user's existing lock layout controls which variables it uses. ReGreet uses
opaque input surfaces and text roles. Existing layouts are retained by Grove's
merge behavior. Wallpapers favor dark centers, but text over arbitrary imagery
still depends on the lock/greeter layout.

## Verification

Validated with the installed Mango Grove: import, preview, and apply/undo for all
eleven selected components in an isolated `--root /tmp/vivendi-check`, without
reload. All four wallpaper indices were applied to desktop, lock, and login
surfaces; output bytes matched each selected original. Picker and power palettes
matched the manifest. Undo restored the exact original config files, including a
seeded Ghostty setting. Native Foot, Ghostty, and Fuzzel configuration checks
passed after each apply. GTK4 parsed the ReGreet stylesheet without errors.
Alacritty TOML and Foot INI were parsed separately; Kitty and Alacritty binaries
were unavailable for native validation.

The four PNGs passed Grove decoding, independent PNG chunk CRC checks, minimum
dimensions, and unique SHA-256 checks. Their native size is 1672 × 941. All four
were visually reviewed. Primary foreground contrast is 21:1 against black and
16.67:1 against the surface; muted/surface is 5.78:1, accent/surface 7.03:1,
and secondary/surface 7.51:1. These measured palette pairs do not guarantee
contrast for arbitrary terminal ANSI combinations or transparent user layouts.

See [SOURCES.md](SOURCES.md) for the pinned upstream palette, complete image
generation prompts, provenance, and hashes. License: GPL-3.0-or-later; see
[LICENSE.palette](LICENSE.palette).
