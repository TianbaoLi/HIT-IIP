import os
import csv

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'german.data')

dict_schema = {"Checking":0, "Duration":1, "CreditHistory":2, "Purpose":3, "CreditAmount":4, "Savings":5, "PresentEmployment":6, "Installment":7, "PersonalStatus":8, "Debtors":9, "PresentResidence":10, "Property":11, "Age":12, "OtherInstallment":13, "Housing":14, "ExistingCredits":15, "Job":16, "LiablePeople":17, "Telephone":18, "ForeignWorker":19, "CostMatrix":20}

def read_file_data(filepath):
    fin = open(filepath, 'r')
    for line in fin:
        line = line.strip()
        fields = line.split("\t")
        yield fields
    fin.close()

def map_fields_dict_schema(fields, dict_schema):
    pdict = {}
    fields = fields[0].split()
    for fstr, findex in dict_schema.iteritems():
        pdict[fstr] = str(fields[int(findex)])
    return pdict

for fields in read_file_data(file_path):
    dict_fields = map_fields_dict_schema(fields, dict_schema)
    print dict_fields
