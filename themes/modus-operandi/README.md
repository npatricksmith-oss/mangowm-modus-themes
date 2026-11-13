# Modus Operandi

Crisp white paper and graphite text, with blue and violet accents from Prot's original
Modus Operandi palette. Four original wallpapers offer quiet Mediterranean architecture,
paper sculpture, olive paths, and a place to think. See [sources and complete prompts](SOURCES.md).

Validate and try the complete bundle without changing your desktop:

```sh
mango-grove validate themes/modus-operandi
mango-grove --root /tmp/grove-operandi-example import themes/modus-operandi
mango-grove --root /tmp/grove-operandi-example preview modus-operandi --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove --root /tmp/grove-operandi-example apply modus-operandi --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove --root /tmp/grove-operandi-example undo
```

The four terminals use opaque white surfaces, white-on-blue selections, and the exact
upstream terminal palette. Waybar has opaque white and pale-gray surfaces with dark
semantic text. Fuzzel, MangoWM, Grove's interface, and the power-menu palette use Grove's
native palette generation. The login-screen override uses opaque control surfaces and
opaque text roles. Chrome and T3 Code are deliberately excluded: do not select those
components when applying this collection.

Hyprlock receives all `$grove_*` color variables with full opacity, including text,
clock, label, glass, and error roles; Grove adds the selected wallpaper path. Existing
Hyprlock layout rules remain in control: a hardcoded transparent input field, Pango alpha
span, or wallpaper path can override those choices. For guaranteed contrast, the consuming
layout should place text over `$grove_bg` or `$grove_surface`, use the supplied text roles,
and source `$grove_wallpaper`. This bundle preserves the layout and cannot guarantee text
contrast over every image pixel. ReGreet requires Grove's normal one-time greeter setup
for real use; the isolated `--root` mode creates its own test greeter directory.
