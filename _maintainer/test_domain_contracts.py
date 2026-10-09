"""Exercise primitive types, record identity and joins at the data boundary."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from build import ROOT, prepare, python_template
from schema import case_errors
from test_renderers import run_python


def typed_case():
    data=json.loads((ROOT/'_maintainer/catalog/control-testing.json').read_text())
    evidence=data['evidence'][0]['id']
    data['domain_tables']=[{
        'name':'Parents','columns':['id','currency','amount','active','evidence_ids'],
        'rows':[['P1','USD',10.5,True,evidence],['P1','EUR',0.0,False,evidence]],
        'primary_key':['id','currency'],
        'column_contracts':{
            'id':{'type':'text','nullable':False,'unit':'identifier','description':'Parent identity'},
            'currency':{'type':'text','nullable':False,'unit':'currency','description':'Native currency','enum':['USD','EUR']},
            'amount':{'type':'number','nullable':False,'unit':'row currency','description':'Known amount','minimum':0},
            'active':{'type':'boolean','nullable':False,'unit':'boolean','description':'Activity flag'},
            'evidence_ids':{'type':'text','nullable':False,'unit':'identifier list','description':'Semicolon-delimited evidence keys'},
        },
    },{
        'name':'Children','columns':['record_id','parent_id','currency','count','raw_value'],
        'rows':[['C1','P1','USD',1,'unparseable source amount'],['C2',None,None,0,'']],
        'primary_key':['record_id'],'report_section':5,
        'foreign_keys':[{'columns':['parent_id','currency'],'table':'Parents','references':['id','currency']}],
        'column_contracts':{
            'record_id':{'type':'text','nullable':False,'unit':'identifier','description':'Child identity'},
            'parent_id':{'type':'text','nullable':True,'unit':'identifier','description':'Optional parent identity'},
            'currency':{'type':'text','nullable':True,'unit':'currency','description':'Optional parent currency'},
            'count':{'type':'integer','nullable':False,'unit':'count','description':'Observed count','minimum':0},
            'raw_value':{'type':'text','nullable':False,'unit':'raw source text','description':'Preserved source defect, not a parsed amount'},
        },
    }]
    return data


class DomainContracts(unittest.TestCase):
    def test_compound_keys_and_raw_defects_are_distinct_from_parsed_values(self):
        self.assertEqual(case_errors(typed_case()),[])

    def test_all_declared_primitive_types_nulls_enums_and_bounds(self):
        mutations=[(0,3,'true','wrong boolean'),(0,2,True,'wrong number'),
                   (0,2,None,'null prohibited'),(0,2,-1,'outside minimum'),
                   (0,1,'XYZ','outside enum'),(1,3,1.0,'wrong integer')]
        for table,column,value,message in mutations:
            with self.subTest(value=value,column=column):
                data=typed_case();data['domain_tables'][table]['rows'][0][column]=value
                self.assertTrue(any(message in e for e in case_errors(data)),case_errors(data))

    def test_primary_key_evidence_and_compound_foreign_key_fail_closed(self):
        data=typed_case();data['domain_tables'][0]['rows'].append(copy.deepcopy(data['domain_tables'][0]['rows'][0]))
        self.assertTrue(any('duplicate primary key' in e for e in case_errors(data)))
        data=typed_case();data['domain_tables'][0]['rows'][0][-1]='MISSING'
        self.assertTrue(any('unresolved domain evidence' in e for e in case_errors(data)))
        for parent,currency in [('P2','USD'),(None,'USD'),('P1',None)]:
            data=typed_case();data['domain_tables'][1]['rows'][0][1:3]=[parent,currency]
            self.assertTrue(any('unresolved domain foreign key' in e for e in case_errors(data)))

    def test_contract_shapes_and_report_placement_are_checked(self):
        for value in [None,[],{}, {'id':{}}]:
            data=typed_case();data['domain_tables'][0]['column_contracts']=value
            self.assertTrue(case_errors(data))

        for placement in [0,3,6,'4',True]:
            data=typed_case();data['domain_tables'][0]['report_section']=placement
            self.assertTrue(any('report_section' in e for e in case_errors(data)))
        for key,value in [('primary_key',[]),('primary_key',['missing']),('foreign_keys',{}),('foreign_keys',[None])]:
            data=typed_case();data['domain_tables'][0][key]=value
            self.assertTrue(case_errors(data))

    def test_boolean_and_numeric_join_keys_cannot_alias(self):
        data=typed_case()
        data['domain_tables'][1]['foreign_keys']=[{'columns':['count'],'table':'Parents','references':['active']}]
        self.assertTrue(any('unresolved domain foreign key' in e for e in case_errors(data)))

    def test_display_precision_is_bounded_before_rendering(self):
        data=typed_case();data['domain_tables'][0]['formats']={'amount':'0.'+'0'*15}
        self.assertEqual(case_errors(data),[])
        data['domain_tables'][0]['formats']['amount']='0.'+'0'*101
        self.assertTrue(any('15 decimal places' in e for e in case_errors(data)))
        data=typed_case();data['metrics'][0]['format']='0.'+'0'*16
        self.assertTrue(any('invalid metric format' in e for e in case_errors(data)))
        for value in ['\ud800','\ufffe','\uffff']:
            data=typed_case();data['domain_tables'][1]['rows'][0][-1]=value
            self.assertTrue(any('XML Unicode' in e for e in case_errors(data)))

    def test_two_through_twelve_tables_preserve_legacy_compatibility(self):
        for count in [2,4,8,12]:
            data=typed_case()
            for n in range(count-2):
                extra=copy.deepcopy(data['domain_tables'][0]);extra['name']='Extra'+str(n);data['domain_tables'].append(extra)
            self.assertEqual(case_errors(data),[])
        for count in [0,1,13]:
            data=typed_case();data['domain_tables']=[dict(copy.deepcopy(data['domain_tables'][0]),name='Table'+str(n)) for n in range(count)]
            self.assertTrue(any('two and twelve' in e for e in case_errors(data)))

    def test_invalid_domain_values_reject_before_either_output_is_written(self):
        data=prepare(typed_case());data['domain_tables'][0]['rows'][0][3]='APPROVED'
        for renderer in ['report.py','workbook.py']:
            with tempfile.TemporaryDirectory() as tmp:
                with self.assertRaisesRegex(ValueError,'wrong boolean'):
                    run_python(python_template(renderer,data),Path(tmp),renderer)
                self.assertFalse(list(Path(tmp).glob('*.xlsx'))+list(Path(tmp).glob('*.docx')))


if __name__=='__main__':unittest.main(verbosity=2)
