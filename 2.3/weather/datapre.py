import os
import csv
import copy
import math

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'TrainingData.csv')
reader = csv.DictReader(file(file_path,'rb'))
data = []
selectedAttr = 'target_11_1601'

def missingHandler_global(data):
    dataList = []
    dataList = copy.deepcopy(data)
    for x in dataList:
        if x[selectedAttr] == 'NA':
            x[selectedAttr] = "-1000000"
            #Selected transformaed number by www.kaggle.com
    return dataList

def missingHandler_avg(data):
    dataList = []
    dataList = copy.deepcopy(data)
    avg = 0.0
    for x in dataList:
        if x[selectedAttr] != 'NA':
            avg += float(x[selectedAttr])
    avg /= len(dataList)
    for x in dataList:
        if x[selectedAttr] == 'NA':
            x[selectedAttr] = "%f" % avg
    return dataList
def standardize_minmax(data):
    dataList = []
    dataList = copy.deepcopy(data)
    dataMin = 100.0
    dataMax = -100.0
    for x in dataList:
        if x[selectedAttr] == 'NA' or x[selectedAttr] == "-1000000":
            continue
        if float(x[selectedAttr]) < dataMin:
            dataMin = float(x[selectedAttr])
        if float(x[selectedAttr]) > dataMax:
            dataMax = float(x[selectedAttr])
    for x in dataList:
        x[selectedAttr] = "%.15f" % ((float(x[selectedAttr]) - dataMin) / (dataMax - dataMin) * (1 - 0) + 0)
    return dataList

def standardize_decimal(data):
    dataList = []
    dataList = copy.deepcopy(data)
    dataMax = -100.0
    for x in dataList:
        if x[selectedAttr] == 'NA' or x[selectedAttr] == "-1000000":
            continue
        if float(x[selectedAttr]) > dataMax:
            dataMax = float(x[selectedAttr])
    p = pow(10, int(math.log10(dataMax)) + 1)

    for x in dataList:
        x[selectedAttr] = "%.15f" % (float(x[selectedAttr]) / p)
    return dataList

numControl = 40
#Number of lines to be tested
index = 0

for line in reader:
    index += 1
    if index > numControl:
        break
    data.append(line)

data_missingHandeledByGlobal = missingHandler_global(data)
data_missingHandeledByAvg = missingHandler_avg(data)

data_standardize_minmax = standardize_minmax(data_missingHandeledByAvg)
data_standardize_decimal= standardize_decimal(data_missingHandeledByAvg)

#for x in data_standardize_decimal:
#    print x[selectedAttr]
