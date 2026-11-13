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

if __name__ == '__main__':
    unittest.main()
