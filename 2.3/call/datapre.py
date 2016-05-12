# -*- coding: gbk -*-

import os
import csv
import json
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

def median(l, length):
    if length % 2 != 0:
        return l[length/2-1]
    else:
        return float(l[length/2-1] + l[length/2]) / 2

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'call.csv')
reader = csv.DictReader(file(file_path, 'rb'))

for line in reader:
    print json.dumps(line, ensure_ascii=False)
