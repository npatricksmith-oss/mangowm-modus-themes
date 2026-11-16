# Arch Linux package

Build a local source snapshot and package without root:

```sh
./scripts/build-arch-package.sh
```

The output is in `~/Packages/mangowm-modus-themes/`. Install with:

```sh
sudo pacman -U ~/Packages/mangowm-modus-themes/mangowm-modus-themes-1.0.0-1-any.pkg.tar.zst
```

The package installs all four bundles and sixteen wallpapers under
`/usr/share/mango-grove/themes/`. It does not modify home directories or apply a theme.
With Mango Grove installed, import the variants you want as your regular user:

```sh
for theme in /usr/share/mango-grove/themes/modus-*; do
    mango-grove import "$theme"
done
```

Then open Mango Grove and refresh the collection. Import refuses existing IDs;
package upgrades do not overwrite previously imported copies. To update an imported
theme, back up and remove its existing user bundle before importing the new copy.
Removing this package leaves imported user copies intact.

See README.md for component selection, preview/apply commands, and greeter setup.
The source archive alongside PKGBUILD is a complete local build input; keep them
together when sharing. AUR publication would require hosting a matching release
archive and changing the source URL; this local recipe is not an AUR submission.
