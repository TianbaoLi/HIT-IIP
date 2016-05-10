# -*- coding: gbk -*-

import os
import csv
from operator import itemgetter

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'call.csv')
reader = csv.DictReader(file(file_path,'rb'))

count = {}
for line in reader:
    count[line['对方号码']] = count.get(line['对方号码'],0) + int(line['通信时长'])
    sorted_count=sorted(count.items(), key = itemgetter(1), reverse = True)
for number,time in sorted_count:
	print '%s\t%s' % (number, time)
