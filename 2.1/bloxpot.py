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

call_record = []
time = []
for line in reader:
    call_record.append(line)
    time.append(int(line['通信时长']))

time.sort()
time_len = len(time)
time_min = time[0]
time_q1 = time[int(time_len * 0.25)]
time_median = median(time, time_len)
time_q3 = time[int(time_len * 0.75)]
time_max = time[time_len-1]
time_iqr = time_q3 - time_q1
time_min_observation = time_q1 - 1.5 * time_iqr > time_min and time_q1 - 1.5 * time_iqr or time_min
time_max_observation = time_q3 + 1.5 * time_iqr < time_max and time_q3 + 1.5 * time_iqr or time_max
time_outlier = []

for t in time:
    if t < time_min_observation or t > time_max_observation:
        time_outlier.append(t)

x = [1] * len(time_outlier)
y = time_outlier

plt.figure(figsize=(6,10), num = "Boxplot")
plt.title('Boxplot call time')
plt.ylabel('Call time (second)')
xsize = 2.0
ysize = 800.0
plt.xlim(0, xsize)
plt.ylim(0, ysize)
axes = plt.subplot(111)
axes.set_xticks([])
axes.set_yticks(range(0, int(ysize) + 50, 50))
axes.plot(x, y, color = 'red', marker = '+', linestyle='')
plt.axvline(x = 1, ymin = time_min_observation / ysize, ymax = time_q1 / ysize, linewidth = 1, color = 'black', linestyle = '--')
plt.axvline(x = 1, ymin = time_q3 / ysize, ymax = time_max_observation / ysize, linewidth = 1, color = 'black', linestyle = '--')
plt.axvline(x = 0.5, ymin = time_q1 / ysize, ymax = time_q3 / ysize, linewidth=1, color = 'blue')
plt.axvline(x = 1.5, ymin = time_q1 / ysize, ymax = time_q3 / ysize, linewidth=1, color = 'blue')
plt.axhline(y = time_q1, xmin = 0.5 / xsize, xmax = 1.5 / xsize, linewidth=1, color = 'blue')
plt.axhline(y = time_q3, xmin = 0.5 / xsize, xmax = 1.5 / xsize, linewidth=1, color = 'blue')
plt.axhline(y = time_median, xmin = 0.5 / xsize, xmax = 1.5 / xsize, linewidth=1, color = 'red')
plt.axhline(y = time_min_observation, xmin = 0.8 / xsize, xmax = 1.2 / xsize, linewidth=1, color = 'black')
plt.axhline(y = time_max_observation, xmin = 0.8 / xsize, xmax = 1.2 / xsize, linewidth=1, color = 'black')

plt.show()
