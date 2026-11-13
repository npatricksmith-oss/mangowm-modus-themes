# Worker validation

Validated against the installed Mango Grove CLI on 2026-11-12, using isolated root
`/tmp/grove-operandi-worker`, without `--reload`. No real desktop configuration changed.

- `mango-grove validate themes/modus-operandi`: **Valid: Modus Operandi (4 wallpapers)**.
- `mango-grove --root /tmp/grove-operandi-worker import themes/modus-operandi`: imported.
- Preview and apply selected precisely
  `ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker`.
  Both succeeded, producing all eleven components' expected files.
- Initial undo succeeded. Four subsequent apply/undo cycles selected desktop wallpapers
  0, 1, 2, and 3; lock selection was `(desktop + 1) % 4`, login selection was
  `(desktop + 2) % 4`. SHA-256 checks confirmed each of the three installed wallpaper
  files matched the selected original. Undo removed newly created configuration files.
- `foot --check-config --config /tmp/grove-operandi-worker/config/foot/foot.ini`
  passed while the initial apply was present.
- The initial Ghostty check used an unsupported `--config-default-files=false` flag;
  that invocation was replaced during final audit. After creating an empty isolated
  configuration directory with `mkdir -p /tmp/modus-operandi-ghostty-config`, the exact
  successful native check was:
  `XDG_CONFIG_HOME=/tmp/modus-operandi-ghostty-config ghostty +validate-config --config-file=/tmp/modus-operandi/themes/modus-operandi/apps/ghostty.conf`.
  It exited **0** with no diagnostics.
- GTK3 `Gtk.CssProvider.load_from_path` parsed `apps/waybar.css` without errors;
  GTK4 parsed `apps/regreet.css` without errors. Neither parser requires launching the app.
- Python `tomllib` parsed the installed Alacritty TOML and confirmed `window.opacity = 1.0`.
  Alacritty and Kitty binaries were not installed, so live/native parser checks for them
  were not available. Hyprlock was not launched because that would lock the real desktop.
- All PNG chunk CRCs, IDAT decompression, dimensions, and four distinct SHA-256 values
  passed. All four images were visually inspected in imagegen results.
- Direct comparison with pinned upstream source confirmed all six palette fields and
  all sixteen ANSI values exactly match the mapping documented in `SOURCES.md`.
- Applied `current.json` picker and power palettes exactly matched `theme.toml`;
  no Chrome or T3 Code outputs were created.
- `git diff --check` passed.

Contrast ratios (WCAG relative luminance):

| Text role | White background | Pale-gray surface |
| --- | ---: | ---: |
| foreground | 21.0000:1 | 18.7585:1 |
| muted | 7.0047:1 | 6.2570:1 |
| accent | 7.0486:1 | 6.2962:1 |
| secondary | 9.5845:1 | 8.5615:1 |

The intended check is >=7:1 on the main white background and >=4.5:1 on the pale-gray
surface. An initial exploratory assertion of >=7:1 for every role on both surfaces
was too strict for the exact upstream palette; the final check preserves source fidelity
and reports the measured ratios rather than claiming universal AAA contrast.
