import os
import csv
import copy

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

numControl = 40
index = 0

for line in reader:
    index += 1
    if index > numControl:
        break
    data.append(line)

data_missingHandeledByGlobal = missingHandler_global(data)
#print data_missingHandeledByGlobal
data_missingHandeledByAvg = missingHandler_avg(data)
#print data_missingHandeledByAvg
