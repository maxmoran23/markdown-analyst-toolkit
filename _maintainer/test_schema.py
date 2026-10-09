"""Boundary regressions for malformed cases and portable renderer safety."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from build import ROOT, prepare, python_template
from schema import case_errors
from test_renderers import run_python

class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'_maintainer/catalog/control-testing.json').read_text())

    def test_valid_case_and_materially_distinct_empty_states(self):
        self.assertEqual(case_errors(self.data),[])
        d=copy.deepcopy(self.data);d['findings']=[];d['evidence']=[];d['metrics']=[]
        for t in d['domain_tables']:t['rows']=[]
        self.assertEqual(case_errors(d),[])

    def test_malformed_shapes_produce_diagnostics_instead_of_crashing(self):
        changes=[('report_sections',[{}]*8),('report_narrative',None),('findings',[None]),('domain_tables',[None]),('evidence',[{'id':'x'}]),('metrics',[{'label':'x'}]),('slug','../escape'),('palette',{}),('limitations',[None]),('actions',{})]
        for key,value in changes:
            with self.subTest(field=key):
                d=copy.deepcopy(self.data);d[key]=value;self.assertTrue(case_errors(d))
        for value in [None,[],1,'case']:
            self.assertTrue(case_errors(value))

    def test_sheet_aliases_formats_numbers_and_control_bytes_rejected(self):
        def change_name(d):d['domain_tables'][0]['name']='summary'
        def change_format(d):d['domain_tables'][0]['formats']={'NONEXISTENT':'0.0%'}
        def change_nan(d):d['metrics'][0]['value']=float('nan')
        def change_control(d):d['evidence'][0]['title']='source\x01text'
        def change_evidence(d):d['findings'][0]['evidence_ids']='SYN-001'
        for mutation in [change_name,change_format,change_nan,change_control,change_evidence]:
            d=copy.deepcopy(self.data);mutation(d)
            with self.subTest(mutation=mutation.__name__):self.assertTrue(case_errors(d))

    def test_action_join_rejected_in_standalone_renderer(self):
        d=prepare(copy.deepcopy(self.data));d['actions'][0]['finding_id']='NO-SUCH-FINDING'
        for renderer in ['report.py','workbook.py']:
            with self.subTest(renderer=renderer),tempfile.TemporaryDirectory() as tmp:
                with self.assertRaisesRegex(ValueError,'unresolved action finding key'):
                    run_python(python_template(renderer,d),Path(tmp),renderer)
                self.assertFalse(list(Path(tmp).glob('*.xlsx'))+list(Path(tmp).glob('*.docx')))

    def test_long_excel_evidence_is_rejected_before_silent_truncation(self):
        d=prepare(copy.deepcopy(self.data));d['evidence'][0]['title']='x'*32768
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError,'32767'):
                run_python(python_template('workbook.py',d),Path(tmp),'workbook.py')
            self.assertFalse(list(Path(tmp).glob('*.xlsx')))

    def test_broken_catalog_files_produce_release_diagnostics(self):
        from validate import validate
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);catalog=root/'_maintainer/catalog'
            catalog.mkdir(parents=True);(root/'suites').mkdir()
            (catalog/'broken.json').write_text('{not JSON')
            (catalog/'missing.json').write_text('{}')
            errors=validate(root=root,check_generated=False)
            self.assertTrue(any('broken.json: invalid JSON' in e for e in errors))
            self.assertTrue(any('missing.json: slug must be nonempty text' in e for e in errors))

    def test_case_cutoff_is_distinct_from_template_release_date(self):
        d=copy.deepcopy(self.data);d['as_of']='2026-09-30'
        self.assertEqual(prepare(d)['as_of'],'2026-09-30')
        del d['as_of'];d['metadata']={'as_of':'2026-08-31'}
        self.assertEqual(prepare(d)['as_of'],'2026-08-31')

    def test_standalone_metadata_and_review_fields_cannot_be_omitted(self):
        for key in ['suite_id','version','as_of','notice','scope','methods','actions','qa','conclusion']:
            for renderer in ['report.py','workbook.py']:
                with self.subTest(field=key,renderer=renderer),tempfile.TemporaryDirectory() as tmp:
                    d=prepare(copy.deepcopy(self.data));del d[key]
                    with self.assertRaisesRegex(ValueError,'Case data rejected'):
                        run_python(python_template(renderer,d),Path(tmp),renderer)
                    self.assertFalse(list(Path(tmp).glob('*.xlsx'))+list(Path(tmp).glob('*.docx')))

    def test_excel_large_integer_rejected_and_explicit_text_preserved(self):
        from openpyxl import load_workbook
        d=prepare(copy.deepcopy(self.data));d['domain_tables'][0]['rows'][0][0]=10000000000000001
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp)
            with self.assertRaisesRegex(ValueError,'15-digit precision'):
                run_python(python_template('workbook.py',d),folder,'workbook.py')
            self.assertFalse(list(folder.glob('*.xlsx')))
            d['domain_tables'][0]['rows'][0][0]='10000000000000001'
            run_python(python_template('workbook.py',d),folder,'workbook.py')
            wb=load_workbook(folder/(d['slug']+'-review.xlsx'))
            self.assertEqual(wb[d['domain_tables'][0]['name']]['A2'].value,'10000000000000001')

if __name__=='__main__':unittest.main(verbosity=2)
