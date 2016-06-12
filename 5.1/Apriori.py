import os
from operator import itemgetter
from collections import OrderedDict

min_sup_count = 2

def load_data(filename):
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, filename)
    data = []
    dataIn = open(file_path, 'r')
    for line in dataIn:
        line = line.strip()
        (id, items) = line.split()
        items = items.split(',')
        data.append(items)
    return data

def genL1(data):
    L1 = {}
    for d in data:
        for x in d:
            L1[x] = L1.get(x, 0) + 1
    return L1

def apriori_gen(L, k):
    C = []
    LItem = L.keys();
    LItem.sort()
    for i in range(len(LItem)):
        for j in range(i + 1, len(LItem)):
            L1 = list(LItem[i])[ : k - 2]
            L2 = list(LItem[j])[ : k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                C.append("".join(OrderedDict.fromkeys(LItem[i] + LItem[j])))
    return C

def subsetScan(C, data, k):
    L = {}
    for c in C:
        for d in data:
            sub = True
            for x in c:
                if x not in d:
                    sub = False
                    break
            if sub == True:
                L[c] = L.get(c, 0) + 1
    return L

def Apriori(data, support):
    result = {}
    L = genL1(data)
    for l in L.keys():
        if L[l] < support:
            L.pop(l)
    for l in L.keys():
        result[l] = L[l]
    k = 1
    while(len(L) > 0):
        k = k + 1
        C = apriori_gen(L, k)
        L = subsetScan(C, data, k)
        for l in L.keys():
            if L[l] < support:
                L.pop(l)
        for l in L.keys():
            result[l] = L[l]
    return result

if __name__ == '__main__':
    data = load_data('homework.dat')
    result = Apriori(data, min_sup_count)
    print result
