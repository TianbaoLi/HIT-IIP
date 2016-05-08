import os
import csv

BASE_DIR = os.path.dirname(__file__)
file_path1 = os.path.join(BASE_DIR, 'GPSSample\\20121110\\20121110035412.txt')
file_path2 = os.path.join(BASE_DIR, 'GPSSample\\20121110\\20121110035631.txt')
file_path3 = os.path.join(BASE_DIR, 'GPSSample\\20121110\\20121110035852.txt')
file_path4 = os.path.join(BASE_DIR, 'GPSSample\\20121110\\20121110040111.txt')
file_path5 = os.path.join(BASE_DIR, 'GPSSample\\20121110\\20121110040331.txt')

dict_schema = {"Car":0, "Trigger":1, "Status":2, "GPSTime":3, "GPSLongitude":4, "GPSLatitude":5, "GPSVelocity":6, "GPSDirection":7, "GPSStatus":8}

def read_file_data(filepaths):
    for filepath in filepaths:
        fin = open(filepath, 'r')
        for line in fin:
            line = line.strip()
            if line == '':
                continue
            fields = line.split(",")
            yield fields
        fin.close()

def map_fields_dict_schema(fields, dict_schema):
    pdict = {}
    for fstr, findex in dict_schema.iteritems():
        pdict[fstr] = str(fields[int(findex)])
    return pdict

for fields in read_file_data([file_path1, file_path2, file_path3, file_path4, file_path5]):
    dict_fields = map_fields_dict_schema(fields, dict_schema)
    print dict_fields
