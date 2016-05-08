import os
import csv

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'forestfires.csv')
reader = csv.DictReader(file(file_path,'rb'))
for line in reader:
    print line
