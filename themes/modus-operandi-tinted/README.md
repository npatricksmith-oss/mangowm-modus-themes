# Modus Operandi Tinted

Warm paper, dark ink and restrained blue-violet accents from Prot's original tinted light palette. Four original wallpapers explore folded paper terrain, an afternoon portico, an olive walk, and sculpture in a quiet room. See [sources and complete generation prompts](SOURCES.md).

Validate and try the complete bundle without changing your desktop:

```sh
mango-grove validate themes/modus-operandi-tinted
mango-grove --root /tmp/grove-operandi-tinted-example import themes/modus-operandi-tinted
mango-grove --root /tmp/grove-operandi-tinted-example preview modus-operandi-tinted --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove --root /tmp/grove-operandi-tinted-example apply modus-operandi-tinted --components ghostty,foot,alacritty,kitty,wallpaper,waybar,fuzzel,mango,hyprlock,regreet,picker
mango-grove --root /tmp/grove-operandi-tinted-example undo
```

Ghostty, Foot, Alacritty and Kitty receive opaque warm-paper backgrounds, paper-on-blue selections, and the exact upstream ANSI palette. Both Foot color sections are supplied. Waybar uses opaque paper surfaces, dark semantic text and contrasting focused buttons. Hyprlock and ReGreet receive opaque text roles; ReGreet has opaque controls and label backgrounds. Fuzzel, MangoWM, Grove's own interface and Mango Power Menu use Grove's palette generation. Chrome and T3 Code are excluded: leave them unchecked and use the explicit component list above.

Grove supplies the chosen lock wallpaper path. Existing Hyprlock layout rules control where the variables are consumed: hardcoded transparency, Pango alpha spans, colors or image paths can override them. For reliable text contrast, the layout should place text over `$grove_bg` or `$grove_surface`, use the supplied opaque text roles, and use `$grove_wallpaper`. This bundle supplies colors rather than replacing the layout. ReGreet needs Grove's normal greeter setup for real use; isolated `--root` mode uses its own test greeter directory.
