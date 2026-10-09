"""Check published-package boundaries against original files and manifest hashes."""
import hashlib
import json
from pathlib import Path
import unittest
import zipfile
from build import ROOT, VERSION
from package import package

class PackageTests(unittest.TestCase):
    def test_archives_reproduce_exact_source_and_repeatable_bytes(self):
        package();output=ROOT/'build/releases'
        names=sorted(p.name for p in (ROOT/'suites').iterdir() if p.is_dir())
        for name in names:
            with self.subTest(suite=name),zipfile.ZipFile(output/(name+'.zip')) as archive:
                expected={name+'/'+p.name:p.read_bytes() for p in (ROOT/'suites'/name).glob('*.md')}
                self.assertEqual(len(expected),12)
                self.assertEqual(set(archive.namelist()),set(expected))
                self.assertTrue(all(n.endswith('.md') and not n.startswith('/') and '..' not in Path(n).parts for n in archive.namelist()))
                for member,content in expected.items():self.assertEqual(archive.read(member),content)
        with zipfile.ZipFile(output/'all-markdown-suites.zip') as archive:
            self.assertEqual(len(archive.namelist()),len(names)*12)
            combined={name+'/'+p.name:p.read_bytes() for name in names for p in (ROOT/'suites'/name).glob('*.md')}
            self.assertEqual(set(archive.namelist()),set(combined))
            for member,content in combined.items():self.assertEqual(archive.read(member),content)
        manifest=json.loads((output/'release-manifest.json').read_text())
        self.assertEqual(manifest['version'],VERSION)
        self.assertEqual(manifest['suite_count'],len(names))
        self.assertEqual({s['id'] for s in manifest['suites']},set(names))
        for suite in manifest['suites']:
            self.assertEqual(len(suite['files']),12)
            for name,digest in suite['files'].items():
                self.assertEqual(hashlib.sha256((ROOT/'suites'/suite['id']/name).read_bytes()).hexdigest(),digest)
        before={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in output.iterdir()}
        package()
        self.assertEqual(before,{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in output.iterdir()})
        for line in (output/'SHA256SUMS.txt').read_text().splitlines():
            digest,name=line.split('  ')
            self.assertEqual(hashlib.sha256((output/name).read_bytes()).hexdigest(),digest)
        listed=[line.split('  ')[1] for line in (output/'SHA256SUMS.txt').read_text().splitlines()]
        expected={name+'.zip' for name in names}|{'all-markdown-suites.zip','suite-finder.html','release-manifest.json'}
        self.assertEqual(set(listed),expected)
        self.assertEqual(len(listed),len(expected))
        self.assertEqual({p.name for p in output.iterdir()},expected|{'SHA256SUMS.txt'})

if __name__=='__main__':unittest.main(verbosity=2)
