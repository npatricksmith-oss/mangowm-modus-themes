# Modus for Mango Grove

Four desktop themes based on [Protesilaos Stavrou's Modus themes](https://github.com/protesilaos/modus-themes):

| Bundle | Appearance | Wallpapers |
| --- | --- | --- |
| `themes/modus-vivendi` | Black, white type, luminous accents | Four original images |
| `themes/modus-operandi` | White, black type, deep accents | Four original images |
| `themes/modus-vivendi-tinted` | Midnight blue, white type, luminous accents | Four original images |
| `themes/modus-operandi-tinted` | Warm ochre paper, black type, deep accents | Four original images |

Each directory is a portable version-1 Grove bundle. It includes `theme.toml`, native application overrides, four original generated landscape wallpapers, and `SOURCES.md` with palette attribution and complete image prompts. The landscapes, quiet studies, Mediterranean materials, and restrained geometry are an ode to Prot's care for clarity and thoughtful work; they do not imply his endorsement.

Coverage: Ghostty, Foot, Alacritty, Kitty, MangoWM, Waybar, Fuzzel, Hyprlock, ReGreet, desktop wallpaper, Grove's interface, and the Mango Power Menu palette. Chrome and T3 Code are excluded. Grove's component list must be supplied explicitly when applying these bundles.

## Import and apply

```sh
mango-grove validate themes/modus-vivendi
mango-grove import themes/modus-vivendi
mango-grove preview modus-vivendi --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove apply modus-vivendi --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
```

Use the other bundle directory and ID to import a different variant. Import refuses existing IDs rather than overwriting them. In the GUI, leave Chrome and T3 Code unchecked. Terminal color overrides are opaque so the wallpaper cannot reduce text contrast.

ReGreet requires Grove's existing one-time greeter setup; inspect `mango-grove greeter-setup`. Omit `regreet` until it is configured. Hyprlock requires the existing layout to source `~/.config/hypr/hyprlock-colors.conf` and use its `$grove_*` variables. These bundles provide color fragments, not replacement compositor, panel, or lock-screen layouts. Mango Power Menu reads Grove's `current.json` palette after the `mango` component is applied.

`mango-grove wallpapers modus-vivendi` lists zero-based wallpaper indices. Theme-local images come first. Select separate surfaces with `--wallpaper 0 --lock-wallpaper 1 --login-wallpaper 2`. Add `--reload` only when you want Grove to reload running applications and set the live wallpaper. `mango-grove undo` restores the last transaction.

## Verify in isolation

Requires Python 3.11+ and the installed `mango-grove` CLI. The validator uses Python's standard library. Grove performs image decoding and application rendering; no API key or image generation dependency is needed to use or test a bundle.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate-themes.py
```

The full command requires all four bundles and sixteen unique wallpapers. It creates temporary Grove roots, exercises every included component, preserves representative existing settings and excluded-app files, rotates all four wallpapers across desktop/lock/login, checks repeated apply, and compares bytes and permissions after undo. It never requests live reload or writes to your desktop.

During integration, test an explicit subset:

```sh
python3 scripts/validate-themes.py --themes modus-vivendi
```

`--static-only` checks manifests, provenance, PNG structure, exact palette values, and selected contrast pairs. It is a quick check, not final acceptance. Image aesthetics and actual desktop layouts still require visual inspection. See [palette and verification notes](docs/palette-and-verification.md).

The palette and port are distributed under the repository's [GPL-3.0 license](LICENSE). See [attribution](ATTRIBUTION.md) and each bundle's `SOURCES.md` for origins and image-generation records.
