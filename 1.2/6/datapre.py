import os
import csv

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'lenses.data')

dict_schema = {"Age":0, "Prescription":1, "Astigmatic":2, "TearProductionRate":3}

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
