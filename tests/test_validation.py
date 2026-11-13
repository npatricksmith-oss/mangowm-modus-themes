"""Regression tests for rejection paths in the collection validator."""
import importlib.util
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zlib

SPEC = importlib.util.spec_from_file_location('validation', Path(__file__).resolve().parents[1] / 'scripts/validate-themes.py')
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def chunk(kind, data):
    return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data) & 0xffffffff)


def png(shade):
    width,height = 1536,864
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB',width,height,8,0,0,0,0)) + chunk(b'IDAT', zlib.compress((b'\x00' + bytes([shade])*width)*height)) + chunk(b'IEND', b'')


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.bundle = Path(self.tmp.name)
        self.name = 'modus-operandi'
        self.palette = v.REFERENCE['themes'][self.name]['palette']
        self.files = ''
        self.provenance = 'Protesilaos '+v.REFERENCE['revision']+' imagegen full prompts\n'
        for i in range(4):
            (self.bundle / f'{i}.png').write_bytes(png(40+i))
            self.provenance += f'{i}.png prompt: synthetic test fixture only\n'
        self.write_manifest()

    def write_manifest(self):
        header = f'version = 1\nid = "{self.name}"\nname = "Fixture"\ndescription = "Test fixture"\nauthor = "Test"\n'
        palette = '[palette]\n'+'\n'.join(k+' = '+json.dumps(value) for k,value in self.palette.items())+'\n'
        images = ''.join(f'\n[[wallpapers]]\nname = "Image {i}"\npath = "{i}.png"\n' for i in range(4))
        (self.bundle / 'theme.toml').write_text(header + palette + self.files + images)
        (self.bundle / 'SOURCES.md').write_text(self.provenance)

    def check(self):
        return v.check_manifest(self.bundle,self.name)

    def test_valid_reference_and_images(self):
        manifest,digests = self.check()
        self.assertEqual(manifest['id'],self.name)
        self.assertEqual(len(digests),4)

    def test_changed_palette_rejected(self):
        self.palette = dict(self.palette,background='#eeeeee')
        self.write_manifest()
        with self.assertRaisesRegex(ValueError,'palette differs'):
            self.check()

    def test_excluded_override_rejected(self):
        self.files = '\n[files]\nchrome = "chrome.css"\n'
        self.write_manifest()
        with self.assertRaisesRegex(ValueError,'excluded component'):
            self.check()

    def test_duplicate_images_rejected(self):
        (self.bundle/'1.png').write_bytes((self.bundle/'0.png').read_bytes())
        with self.assertRaisesRegex(ValueError,'duplicate wallpapers'):
            self.check()

    def test_corrupt_image_rejected(self):
        data = bytearray((self.bundle/'0.png').read_bytes())
        data[50] ^= 1
        (self.bundle/'0.png').write_bytes(data)
        with self.assertRaisesRegex(ValueError,'bad PNG CRC'):
            self.check()

    def test_missing_provenance_rejected(self):
        (self.bundle/'SOURCES.md').write_text('unknown origin')
        with self.assertRaisesRegex(ValueError,'attribution'):
            self.check()

    def test_unlisted_image_rejected(self):
        (self.bundle/'extra.png').write_bytes(png(99))
        with self.assertRaisesRegex(ValueError,'extra/unlisted'):
            self.check()

    def test_escaping_asset_rejected(self):
        with self.assertRaisesRegex(ValueError,'unsafe asset'):
            v.asset(self.bundle,'../outside.png')

    def test_symlink_rejected(self):
        (self.bundle/'link').symlink_to(self.bundle/'0.png')
        with self.assertRaisesRegex(ValueError,'symlink'):
            self.check()

    def test_all_reference_contrast_pairs(self):
        for theme,data in v.REFERENCE['themes'].items():
            p=data['palette']
            self.assertGreaterEqual(v.contrast(p['foreground'],p['background']),7,theme)
            self.assertGreaterEqual(v.contrast(p['muted'],p['surface']),4.5,theme)

    def test_excluded_components_never_selected(self):
        self.assertFalse(v.EXCLUDED.intersection(v.COMPONENTS))
        self.assertEqual(len(v.COMPONENTS),11)


class ReapplyTests(unittest.TestCase):
    def setUp(self):
        self.foot = v.APP_PATHS['foot']
        self.before = {
            self.foot: (b'[main]\nfont=monospace:size=13\n[colors-dark]\nalpha=1\nbackground=000000\n\n[colors-light]\nbackground=000000\n', 0o640),
            'config/kitty/kitty.conf': (b'font_size 13\n', 0o640),
        }

    def test_only_foot_whitespace_movement_allowed(self):
        after = dict(self.before)
        content, mode = after[self.foot]
        after[self.foot] = (content.replace(b'[colors-dark]\n', b'[colors-dark]\n\n').replace(b'\n\n[colors-light]', b'\n[colors-light]'),mode)
        v.check_reapply(self.before,after)

    def test_foot_changed_palette_rejected(self):
        after = dict(self.before)
        content,mode = after[self.foot]
        after[self.foot] = (content.replace(b'background=000000', b'background=ffffff'),mode)
        with self.assertRaisesRegex(ValueError, 'Foot INI values'):
            v.check_reapply(self.before,after)

    def test_foot_changed_unrelated_setting_rejected(self):
        after = dict(self.before)
        content,mode = after[self.foot]
        after[self.foot] = (content.replace(b'size=13', b'size=15'),mode)
        with self.assertRaisesRegex(ValueError, 'Foot INI values'):
            v.check_reapply(self.before,after)

    def test_foot_duplicate_key_rejected(self):
        after = dict(self.before)
        content,mode = after[self.foot]
        after[self.foot] = (content.replace(b'alpha=1', b'alpha=1\nalpha=1'),mode)
        with self.assertRaises(v.configparser.DuplicateOptionError):
            v.check_reapply(self.before,after)

    def test_other_file_whitespace_change_rejected(self):
        after = dict(self.before)
        after['config/kitty/kitty.conf'] = (b'font_size 13\n\n',0o640)
        with self.assertRaisesRegex(ValueError, 'file bytes'):
            v.check_reapply(self.before,after)

    def test_foot_permissions_change_rejected(self):
        after = dict(self.before)
        after[self.foot] = (after[self.foot][0],0o644)
        with self.assertRaisesRegex(ValueError, 'permissions'):
            v.check_reapply(self.before,after)

    def test_added_file_rejected(self):
        after = dict(self.before,new_file=(b'added',0o640))
        with self.assertRaisesRegex(ValueError, 'file set'):
            v.check_reapply(self.before,after)

if __name__ == '__main__':
    unittest.main()
