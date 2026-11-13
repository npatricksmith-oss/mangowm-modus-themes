# Palette mapping and verification

Upstream: <https://github.com/protesilaos/modus-themes/tree/782743415b3eedac0b99db2342fb35703deb752f>.

The palette constants are in `modus-themes.el` at that revision. Theme-specific `.el` files select those constants. `docs/modus-palettes.json` records the selected values and their names so validation is independent of later upstream changes.

| Grove role | Upstream role |
| --- | --- |
| background | bg-main |
| surface | bg-dim |
| foreground | fg-main |
| muted | fg-dim |
| accent | blue-warmer |
| secondary | magenta-cooler |

ANSI slots follow upstream's `fg-term-*` semantic mapping: black, red, green, yellow, blue, magenta, cyan, white, then their bright variants. Upstream fixes black to `#000000`, bright black to `#595959`, white to `#a6a6a6`, and bright white to `#ffffff`. Normal chromatic slots use the base named colors; bright slots use red-warmer, green-cooler, yellow-warmer, blue-warmer, magenta-cooler, and cyan-cooler. Black text on the black Vivendi background and white text on the white Operandi background are expected consequences of those terminal identities. The normal terminal foreground remains distinct and readable. Applications that hard-code black or white ANSI text may need their own color configuration.

The validator checks foreground/background and foreground/surface at 7:1; muted/background and muted/surface at 4.5:1; accent/background and secondary/background at 7:1; accent/surface and secondary/surface at 4.5:1. These are selected opaque text-role pairs. They are not a claim that every ANSI pair, transparency, wallpaper region, terminal program, or existing desktop layout meets WCAG AAA. The native terminal fragments force opaque backgrounds. Lock and login color overrides should use opaque text and readable input surfaces; visual verification is still necessary with the user's existing layouts.

## Verification layers

1. Unit tests mutate synthetic bundles to confirm that wrong palette values, excluded components, duplicate or corrupt images, unlisted files, missing provenance, escaping paths, and symlinks are rejected.
2. Static collection checks require the exact pinned mapping, exactly four unique landscape PNGs per theme (at least 1536 × 864), structural PNG integrity, and attribution/prompt records.
3. Grove's validator decodes the real images and validates bundle contracts. Isolated runtime checks import each bundle, preview all included components without mutation, apply into representative preexisting configuration, inspect generated content, rotate every image on each surface, and check idempotence and exact undo restoration.
4. Human/agent visual inspection checks the finished wallpapers and their contact sheets. Runtime tests do not replace this aesthetic review or verify every application renderer.

Chrome and T3 Code are not selected. The runtime fixture seeds both browsers' GTK stylesheet targets and the editor theme target, then proves that these files stay byte-for-byte unchanged through apply and undo. The current-state component list must match the included eleven Grove components; the power palette must equal the theme palette.
