#!/usr/bin/env bash
set -euo pipefail
repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
output=${1:-"$HOME/Packages/mangowm-modus-themes"}
mkdir -p -- "$output"
output=$(cd -- "$output" && pwd)
name=mangowm-modus-themes
version=1.0.0
archive="$name-$version.tar.gz"
# Reproducible archive metadata; includes the current themes, not an old commit.
tar --sort=name --mtime='@0' --owner=0 --group=0 --numeric-owner \
    --transform="s,^,$name-$version/," -czf "$output/$archive" \
    -C "$repo" themes LICENSE ATTRIBUTION.md README.md packaging/arch/README.md
checksum=$(sha256sum "$output/$archive")
checksum=${checksum%% *}
sed "s/SOURCE_CHECKSUM/$checksum/" "$repo/packaging/arch/PKGBUILD" > "$output/PKGBUILD"
cd -- "$output"
makepkg --force --cleanbuild
makepkg --printsrcinfo > .SRCINFO
