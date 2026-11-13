#!/usr/bin/env python3
"""Validate source fidelity and exercise Grove entirely inside temporary roots."""
from __future__ import annotations
import argparse
import configparser
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import tomllib
import zlib

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = json.loads((ROOT / 'docs/modus-palettes.json').read_text())
THEMES = tuple(REFERENCE['themes'])
COMPONENTS = ('ghostty', 'foot', 'alacritty', 'kitty', 'wallpaper', 'waybar', 'fuzzel', 'mango', 'hyprlock', 'regreet', 'picker')
EXCLUDED = {'chrome', 't3code'}
APP_PATHS = {
    'ghostty': 'config/ghostty/config', 'foot': 'config/foot/foot.ini',
    'alacritty': 'config/alacritty/alacritty.toml', 'kitty': 'config/kitty/kitty.conf',
    'waybar': 'config/waybar/style.css', 'fuzzel': 'config/fuzzel/fuzzel.ini',
    'mango': 'config/mango/config.conf', 'hyprlock': 'config/hypr/hyprlock-colors.conf',
    'regreet': 'greeter/regreet.css',
}
SEED = {
    'config/ghostty/config': 'font-size = 13\nbackground-opacity = 0.5\n',
    'config/foot/foot.ini': '[main]\nfont=monospace:size=13\n[colors-dark]\nalpha=0.5\n',
    'config/alacritty/alacritty.toml': '[font]\nsize = 13\n[window]\nopacity = 0.5\n',
    'config/kitty/kitty.conf': 'font_size 13\nbackground_opacity 0.5\n',
    'config/waybar/style.css': '#clock { padding: 0 7px; }\n',
    'config/fuzzel/fuzzel.ini': '[main]\nfont=monospace:size=13\n[colors]\nbackground=123456ff\n',
    'config/mango/config.conf': 'borderpx=3\n',
    'config/hypr/hyprlock-colors.conf': '$personal = 13\n$grove_bg = rgba(123456ff)\n',
    'greeter/regreet.css': '/* original login theme */\n',
    'config/gtk-3.0/gtk.css': '/* preserved excluded browser CSS */\n',
    'config/gtk-4.0/gtk.css': '/* preserved excluded browser CSS */\n',
    't3/userdata/themes/mango-grove.json': '{"name":"preserved excluded editor theme"}\n',
}
PRESERVED = {'ghostty': 'font-size = 13', 'foot': 'font=monospace:size=13',
             'kitty': 'font_size 13', 'waybar': '#clock { padding: 0 7px; }',
             'fuzzel': 'font=monospace:size=13', 'mango': 'borderpx=3', 'hyprlock': '$personal = 13'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def luminance(color):
    c = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in c]
    return sum(v * k for v, k in zip(c, (.2126, .7152, .0722)))


def contrast(a, b):
    lo, hi = sorted((luminance(a), luminance(b)))
    return (hi + .05) / (lo + .05)


def png_info(path):
    """Check PNG structure/CRCs; Grove additionally decodes every image."""
    raw = path.read_bytes()
    require(raw[:8] == b'\x89PNG\r\n\x1a\n', f'{path}: expected PNG')
    pos, dimensions, seen_data, ended = 8, None, False, False
    while pos < len(raw):
        require(pos + 12 <= len(raw), f'{path}: truncated PNG chunk')
        size = struct.unpack('>I', raw[pos:pos+4])[0]
        kind = raw[pos+4:pos+8]
        payload = raw[pos+8:pos+8+size]
        require(pos + 12 + size <= len(raw), f'{path}: truncated PNG payload')
        crc = struct.unpack('>I', raw[pos+8+size:pos+12+size])[0]
        require(zlib.crc32(kind + payload) & 0xffffffff == crc, f'{path}: bad PNG CRC')
        if kind == b'IHDR':
            require(dimensions is None and pos == 8 and size == 13, f'{path}: malformed IHDR')
            dimensions = struct.unpack('>II', payload[:8])
        elif kind == b'IDAT':
            seen_data = True
        elif kind == b'IEND':
            ended = True
            require(size == 0 and pos + 12 == len(raw), f'{path}: trailing PNG data')
        pos += 12 + size
    require(dimensions and seen_data and ended, f'{path}: incomplete PNG')
    return dimensions


def asset(bundle, relative):
    p = Path(relative)
    require(not p.is_absolute() and '..' not in p.parts, f'unsafe asset path: {relative}')
    result = bundle / p
    require(result.is_file() and not result.is_symlink(), f'missing/unsafe asset: {result}')
    require(result.resolve().is_relative_to(bundle.resolve()), f'asset escapes bundle: {result}')
    return result


def check_manifest(bundle, name):
    manifest = tomllib.loads((bundle / 'theme.toml').read_text())
    require(manifest.get('version') == 1 and manifest.get('id') == name, f'{name}: version/id mismatch')
    require(manifest.get('name') and manifest.get('description') and manifest.get('author'), f'{name}: missing metadata')
    palette = manifest['palette']
    require(palette == REFERENCE['themes'][name]['palette'], f'{name}: palette differs from pinned upstream role mapping')
    files = manifest.get('files', {})
    require(not (EXCLUDED & files.keys()), f'{name}: excluded component override')
    require(set(files) <= set(APP_PATHS), f'{name}: unsupported overrides')
    require(not manifest.get('extras'), f'{name}: unexpected extra apps')
    for value in files.values():
        asset(bundle, value)
    require(not any(p.is_symlink() for p in bundle.rglob('*')), f'{name}: symlink in bundle')
    source = (bundle / 'SOURCES.md').read_text()
    require(REFERENCE['revision'] in source and 'protesilaos' in source.lower(), f'{name}: missing pinned palette attribution')
    require('prompt' in source.lower() and ('imagegen' in source.lower() or 'image_gen' in source.lower()), f'{name}: missing generation provenance')
    wallpapers = manifest.get('wallpapers', [])
    require(len(wallpapers) == 4, f'{name}: expected exactly four wallpaper entries')
    digests = set()
    for wp in wallpapers:
        require(wp.get('name'), f'{name}: unnamed wallpaper')
        path = asset(bundle, wp['path'])
        w, h = png_info(path)
        require(w >= 1536 and h >= 864 and 1.45 <= w / h <= 2.5, f'{path}: expected desktop landscape >=1536x864, got {w}x{h}')
        require(wp['path'] in source, f'{path}: no source/prompt entry')
        digests.add(hashlib.sha256(path.read_bytes()).hexdigest())
    require(len(digests) == 4, f'{name}: duplicate wallpapers')
    images = {p.relative_to(bundle).as_posix() for p in bundle.rglob('*') if p.suffix.lower() in {'.png','.jpg','.jpeg','.webp'}}
    require(images == {wp['path'] for wp in wallpapers}, f'{name}: extra/unlisted wallpaper images')
    pairs = [('foreground','background',7), ('foreground','surface',7), ('muted','background',4.5),
             ('muted','surface',4.5), ('accent','background',7), ('secondary','background',7),
             ('accent','surface',4.5), ('secondary','surface',4.5)]
    for fg,bg,minimum in pairs:
        value = contrast(palette[fg], palette[bg])
        require(value >= minimum, f'{name}: {fg}/{bg} contrast {value:.2f} < {minimum}')
    print(f'{name}: upstream palette, contrast pairs, four distinct landscape PNGs, provenance PASS')
    return manifest, digests


def run(command):
    p = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    require(p.returncode == 0, f'command failed ({p.returncode}): {command!r}\n{p.stdout}')
    return p.stdout


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mode & 0o777)
            for top in ('config','greeter','t3') for p in (root / top).rglob('*') if p.is_file()}


def ini(text):
    obj = configparser.ConfigParser(interpolation=None, strict=True)
    obj.optionxform = str
    obj.read_string(text)
    return obj


def check_reapply(before, after):
    """Only Foot's INI whitespace may move; every other byte/mode is stable."""
    require(before.keys() == after.keys(), 'reapply changed the configuration file set')
    for path, (old_bytes, old_mode) in before.items():
        new_bytes, new_mode = after[path]
        require(old_mode == new_mode, f'reapply changed permissions: {path}')
        if path == APP_PATHS['foot']:
            # Grove's Foot merge can relocate blank lines on a second apply. A
            # strict parser still rejects duplicate sections/keys and compares
            # every key/value, including unrelated user settings.
            old_ini, new_ini = ini(old_bytes.decode()), ini(new_bytes.decode())
            require(old_ini == new_ini, f'reapply changed Foot INI values: {path}')
        else:
            require(old_bytes == new_bytes, f'reapply changed file bytes: {path}')


def assignments(text, separator='='):
    values = {}
    for line in text.splitlines():
        if line.strip().startswith(('#',';')) or separator not in line:
            continue
        key, value = line.split(separator, 1)
        values[key.strip()] = value.strip()
    return values


def check_outputs(root, bundle, manifest, indices):
    p = manifest['palette']
    bg, fg = p['background'], p['foreground']
    text = {c: (root / relative).read_text() for c,relative in APP_PATHS.items()}
    for c,marker in PRESERVED.items():
        require(marker in text[c], f'{c}: unrelated setting lost')
    require(tomllib.loads(text['alacritty'])['font']['size'] == 13, 'Alacritty: unrelated setting lost')
    g = assignments(text['ghostty'])
    require(g['background'] == bg and g['foreground'] == fg, 'Ghostty palette mismatch')
    require(float(g.get('background-opacity', '0')) == 1, 'Ghostty must be opaque')
    k = assignments(text['kitty'], ' ')
    require(k['background'] == bg and k['foreground'] == fg, 'Kitty palette mismatch')
    require(float(k.get('background_opacity', '0')) == 1, 'Kitty must be opaque')
    f = ini(text['foot'])
    for section in ('colors-dark','colors-light'):
        require(f[section]['background'] == bg[1:] and f[section]['foreground'] == fg[1:], 'Foot palette mismatch')
        require(float(f[section].get('alpha', '0')) == 1, f'Foot {section} must be opaque')
    a = tomllib.loads(text['alacritty'])
    require(a['colors']['primary']['background'] == bg and a['colors']['primary']['foreground'] == fg, 'Alacritty palette mismatch')
    require(a.get('window', {}).get('opacity') == 1, 'Alacritty must be opaque')
    for i,color in enumerate(p['ansi']):
        require(re.search(r'^palette\s*=\s*'+str(i)+r'='+re.escape(color)+r'\s*$',text['ghostty'], re.M), f'Ghostty ANSI {i}')
        require(k.get('color'+str(i)) == color, f'Kitty ANSI {i}')
        for section in ('colors-dark','colors-light'):
            require(f[section][('regular' if i < 8 else 'bright')+str(i%8)] == color[1:], f'Foot ANSI {i}')
        key = ('black','red','green','yellow','blue','magenta','cyan','white')[i%8]
        require(a['colors']['normal' if i < 8 else 'bright'][key] == color, f'Alacritty ANSI {i}')
    fu = ini(text['fuzzel'])['colors']
    require(fu['background'] == bg[1:]+'ff' and fu['text'] == fg[1:]+'ff', 'Fuzzel palette mismatch')
    require(fu['selection-text'] == fg[1:]+'ff' and fu['selection'] == p['surface'][1:]+'ff', 'Fuzzel selection mismatch')
    m = assignments(text['mango'])
    require(m['root_color'] == '0x'+bg[1:]+'ff' and m['focus_color'] == '0x'+p['accent'][1:]+'ff', 'Mango palette mismatch')
    for c in ('waybar','regreet'):
        for role in ('background','foreground','accent'):
            require(p[role] in text[c], f'{c}: missing palette {role}')
    h = assignments(text['hyprlock'])
    require(h['$grove_bg'] == 'rgba('+bg[1:]+'ff)' and h['$grove_fg'] == 'rgba('+fg[1:]+'ff)', 'Hyprlock palette mismatch')
    require(h['$grove_wallpaper'] == str(root / 'config/mango-grove/lock-wallpaper.png'), 'Hyprlock wallpaper path mismatch')
    state = json.loads((root / 'config/mango-grove/current.json').read_text())
    require(state['theme'] == manifest['id'], 'applied theme mismatch')
    require(set(state['components']) == set(COMPONENTS), 'component coverage or exclusion mismatch')
    require(state['picker'] == p and state['power'] == p, 'Grove/power menu palette mismatch')
    for role,index in zip(('wallpaper_index','lock_wallpaper_index','login_wallpaper_index'),indices):
        require(state[role] == index, f'{role}: wrong selected wallpaper')
    targets = ('config/mango-grove/wallpaper.png','config/mango-grove/lock-wallpaper.png','greeter/wallpaper.png')
    for target,index in zip(targets,indices):
        require((root / target).read_bytes() == asset(bundle,manifest['wallpapers'][index]['path']).read_bytes(), f'{target}: wrong copied wallpaper')
    require((root / 'greeter/regreet.css').stat().st_mode & 0o777 == 0o644, 'greeter stylesheet not world-readable')
    for path in ('config/gtk-3.0/gtk.css','config/gtk-4.0/gtk.css','t3/userdata/themes/mango-grove.json'):
        require((root / path).read_text() == SEED[path], f'excluded app changed: {path}')


def exercise_grove(bundle, manifest, binary):
    run([binary, 'validate', str(bundle)])
    with tempfile.TemporaryDirectory(prefix='modus-qa-') as tmp:
        root = Path(tmp)
        cmd = [binary,'--root',str(root)]
        run(cmd + ['list'])
        run(cmd + ['import',str(bundle)])
        for path,value in SEED.items():
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value)
            # Grove requires world-readable greeter artifacts and uses 0644
            # during both forward and undo writes. Start in its supported mode.
            target.chmod(0o644 if path.startswith('greeter/') else 0o640)
        baseline = snapshot(root)
        selection = ['--components',','.join(COMPONENTS)]
        # Every image is used on every surface, with independent choices in each transaction.
        for desktop in range(4):
            indices = (desktop, (desktop+1)%4, (desktop+2)%4)
            flags = selection + ['--wallpaper',str(indices[0]),'--lock-wallpaper',str(indices[1]),'--login-wallpaper',str(indices[2])]
            preview = run(cmd + ['preview',manifest['id']] + flags)
            require(snapshot(root) == baseline, 'preview modified configuration')
            for app in APP_PATHS:
                require(Path(APP_PATHS[app]).name in preview, f'preview missing {app}')
            run(cmd + ['apply',manifest['id']] + flags)
            check_outputs(root,bundle,manifest,indices)
            # Reapply checks merge stability and stacked undo.
            applied = snapshot(root)
            run(cmd + ['apply',manifest['id']] + flags)
            check_reapply(applied, snapshot(root))
            run(cmd + ['undo'])
            require(snapshot(root) == applied, 'undo second apply did not restore first apply')
            run(cmd + ['undo'])
            require(snapshot(root) == baseline, 'undo did not restore exact prior bytes/modes')
        print(f"{manifest['id']}: all included components, config preservation, four image rotations, excluded-app preservation, idempotence and undo PASS")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--themes', nargs='+', choices=THEMES, help='Explicit subset for staged integration; default requires all four')
    parser.add_argument('--static-only', action='store_true', help='Skip Grove runtime tests; never sufficient for final acceptance')
    parser.add_argument('--grove', default='mango-grove')
    args = parser.parse_args(argv)
    selected = args.themes or THEMES
    all_digests = set()
    try:
        for name in selected:
            bundle = ROOT / 'themes' / name
            manifest,digests = check_manifest(bundle,name)
            require(not all_digests.intersection(digests), 'wallpaper reused across themes')
            all_digests.update(digests)
            if not args.static_only:
                require(shutil.which(args.grove), f'Grove executable not found: {args.grove}')
                exercise_grove(bundle,manifest,args.grove)
        print(f'PASS: {len(selected)} theme(s), {len(all_digests)} unique wallpapers; '+('static only' if args.static_only else 'static and isolated Grove tests'))
        return 0
    except (ValueError,KeyError,OSError,tomllib.TOMLDecodeError,configparser.Error) as exc:
        print(f'FAIL: {exc}',file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
