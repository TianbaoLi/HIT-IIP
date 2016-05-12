import os
import csv
import copy
import math

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'TrainingData.csv')
reader = csv.DictReader(file(file_path,'rb'))
data = []
selectedAttrs = ['Solar.radiation_64', 'target_1_57', 'Sample.Baro.Pressure_52']

def missingHandler_global(data, selectedAttr):
    dataList = []
    dataList = copy.deepcopy(data)
    for x in dataList:
        if x[selectedAttr] == 'NA':
            x[selectedAttr] = "-1000000"
            #Selected transformaed number by www.kaggle.com
    return dataList

def missingHandler_avg(data, selectedAttr):
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
def standardize_minmax(data, selectedAttr):
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

def standardize_decimal(data, selectedAttr):
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



numControl = 10000
#Number of lines to be tested
index = 0

for line in reader:
    index += 1
    if index > numControl:
        break
    data.append(line)

#data_missingHandeledByGlobal = missingHandler_global(data, 'Solar.radiation_64')
#print data_missingHandeledByGlobal

tmp = copy.deepcopy(data)
for attr in selectedAttrs:
    tmp = missingHandler_avg(tmp, attr)
data_missingHandeledByAvg = copy.deepcopy(tmp)
#print data_missingHandeledByAvg

#data_standardize_minmax = standardize_minmax(data_missingHandeledByAvg, 'Solar.radiation_64')
#print data_standardize_minmax
data_standardize_decimal= standardize_decimal(data_missingHandeledByAvg, 'Solar.radiation_64')
#print data_standardize_decimal

solarRadiation64 = []
target157 = []
for x in data_standardize_decimal:
    solarRadiation64.append(float(x["Solar.radiation_64"]))
    target157.append(float(x["target_1_57"]))
r_solarRadiation64_target157 = pearson(solarRadiation64, target157)
print r_solarRadiation64_target157

map_weekday_sampleBaroPressure52 = {"Monday":{}, "Tuesday":{}, "Wednesday":{}, "Thursday":{}, "Friday":{}, "Saturday":{}, "Sunday":{}}
range_sampleBaroPressure52 = range(730, 772)
range_sampleBaroPressure52.append(775)
sum_weekday = {"Monday":0, "Tuesday":0, "Wednesday":0, "Thursday":0, "Friday":0, "Saturday":0, "Sunday":0}
sum_sampleBaroPressure52 = {v:0 for v in range_sampleBaroPressure52}
for x in map_weekday_sampleBaroPressure52.keys():
    map_weekday_sampleBaroPressure52[x] = {v:0 for v in range_sampleBaroPressure52}

for x in data_standardize_decimal:
    try:
        map_weekday_sampleBaroPressure52[x["weekday"]][int(x["Sample.Baro.Pressure_52"])] += 1
        sum_weekday[x["weekday"]] += 1
        sum_sampleBaroPressure52[int(x["Sample.Baro.Pressure_52"])] += 1
    except ValueError:
        pass
k_weekday_sampleBaroPressure52 = chi_square(map_weekday_sampleBaroPressure52, sum_weekday, sum_sampleBaroPressure52)
print k_weekday_sampleBaroPressure52
