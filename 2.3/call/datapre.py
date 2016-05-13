# -*- coding: utf-8 -*-

import os
import csv
import json
from operator import itemgetter

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'call.csv')
reader = csv.DictReader(file(file_path, 'rb'))

def pearson(x,y):
    n = len(x)
    vals = range(n)

    sumx = sum([float(x[i]) for i in vals])
    sumy = sum([float(y[i]) for i in vals])

    sumxSq = sum([x[i] ** 2.0 for i in vals])
    sumySq = sum([y[i] ** 2.0 for i in vals])

    pSum = sum([x[i] * y[i] for i in vals])

    num = pSum - (sumx * sumy / n)
    den = ((sumxSq - pow(sumx, 2) / n) * (sumySq - pow(sumy, 2) / n)) ** 0.5

    return (den == 0 and 0 or num / den)

def chi_square(data, sumX, sumY):
    dataMap = copy.deepcopy(data)
    dataSumX = copy.deepcopy(sumX)
    dataSumY = copy.deepcopy(sumY)
    dataSum = 0
    for x in dataSumX:
        dataSum += dataSumX[x]

    k = 0
    for x in dataMap.keys():
        for y in dataMap[x].keys():
            if dataSumX[x] == 0 or dataSumY[y] == 0:
                continue
            k += 1.0 * dataMap[x][y] ** 2 / dataSumX[x] / dataSumY[y]
    k -= 1
    k *= dataSum
    return k

callTime = {}
relationship = {}

for line in reader:
    #print json.dumps(line, ensure_ascii=False)
    callTime[line['对方号码']] = callTime.get(line['对方号码'],0) + int(line['通信时长'])
    relationship[line['对方号码']] = relationship.get(line['对方号码'],0) + int(line['亲密性'])

for x in relationship:
    relationship[x] = relationship[x] / abs(relationship[x])

#print callTime
#print relationship
