"""Run the reproducible arithmetic delivered inside each deep worked example."""
import contextlib
import io
import json
import os
import re
import tempfile
import unittest
from build import ROOT


class ProcessFixtures(unittest.TestCase):
    def test_embedded_fixture_derivations_match_catalog_records(self):
        suites=json.loads((ROOT/'_maintainer/process-suites.json').read_text())['suites']
        self.assertTrue(suites)
        for slug in suites:
            with self.subTest(suite=slug):
                text=(ROOT/'suites'/slug/'10-worked-example.md').read_text()
                blocks=re.findall(r'<!-- FIXTURE_CHECK:START -->\s*```python\n(.*?)^```\s*<!-- FIXTURE_CHECK:END -->',text,re.S|re.M)
                self.assertEqual(len(blocks),1,'One complete fixture check is required')
                namespace={'__name__':'__main__'}
                with tempfile.TemporaryDirectory() as temporary:
                    previous=os.getcwd()
                    try:
                        os.chdir(temporary)
                        with contextlib.redirect_stdout(io.StringIO()):exec(compile(blocks[0],slug+'/10-worked-example.md','exec'),namespace)
                    finally:os.chdir(previous)
                checked=namespace.get('CHECKED_TABLES')
                self.assertIsInstance(checked,dict)
                self.assertTrue(checked,'The check must expose calculated rows')
                catalog=json.loads((ROOT/'_maintainer/catalog'/f'{slug}.json').read_text())
                tables={t['name']:t for t in catalog['domain_tables']}
                for name,rows in checked.items():
                    self.assertIn(name,tables)
                    expected=tables[name]['rows']
                    self.assertEqual(len(rows),len(expected),name)
                    for i,(actual,original) in enumerate(zip(rows,expected)):
                        self.assertEqual(len(actual),len(original),(name,i))
                        for j,(value,target) in enumerate(zip(actual,original)):
                            if isinstance(target,float):self.assertAlmostEqual(float(value),target,places=10,msg=f'{name}[{i}][{j}]')
                            else:self.assertEqual(value,target,f'{name}[{i}][{j}]')


if __name__=='__main__':unittest.main(verbosity=2)
