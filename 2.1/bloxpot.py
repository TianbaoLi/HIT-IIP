# -*- coding: gbk -*-

import os
import csv
import json
from operator import itemgetter

def median(l, length):
    if length % 2 != 0:
        return l[length/2-1]
    else:
        return float(l[length/2-1] + l[length/2]) / 2

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'call.csv')
reader = csv.DictReader(file(file_path, 'rb'))

call_record = []
time = []
for line in reader:
    call_record.append(line)
    time.append(int(line['通信时长']))
'''
for x in call_record:
    print json.dumps(x, ensure_ascii = False)
'''

time.sort()
time_len = len(time)

#for x in time:
#    print x

time_min = time[0]
time_q1 = time[int(time_len * 0.25)]
time_median = median(time, time_len)
time_q3 = time[int(time_len * 0.75)]
time_max = time[time_len-1]
time_iqr = time_q3 - time_q1
time_min_observation = time_q1 - 1.5 * time_iqr > time_min and time_q1 - 1.5 * time_iqr or time_min
time_max_observation = time_q3 + 1.5 * time_iqr < time_max and time_q3 + 1.5 * time_iqr or time_max

print time_min
print time_q1
print time_median
print time_q3
print time_max
print time_min_observation
print time_max_observation
