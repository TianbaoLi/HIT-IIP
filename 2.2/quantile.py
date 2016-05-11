import os
from operator import itemgetter
import matplotlib.pyplot as plt

def median(l, length):
    if length % 2 != 0:
        return l[length/2-1]
    else:
        return float(l[length/2-1] + l[length/2]) / 2

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'score.data')
scoreIn = open(file_path, 'r')
tmp = scoreIn.readline().strip().split()
classA = []
classB = []
L = range(0, 21, 1)
countA = {v:0 for v in L}
countB = {v:0 for v in L}
quantileA = {}
quantileB = {}
for x in tmp:
    classA.append(int(x))
    countA[int(x)] = countA[int(x)] + 1
tmp = scoreIn.readline().strip().split()
for x in tmp:
    classB.append(int(x))
    countB[int(x)] = countB[int(x)] + 1

scoreIn.close()
classA.sort()
classB.sort()

stuSum = 0
for x in countA.keys():
    if countA[x] != 0:
        stuSum += countA[x]
        quantileA[x] = 1.0 * stuSum / len(classA)
stuSum = 0
for x in countB.keys():
    if countB[x] != 0:
        stuSum += countB[x]
        quantileB[x] = 1.0 * stuSum / len(classB)
medianA = median(classA, len(classA))
q1A = classA[int(len(classA) * 0.25)]
q3A = classA[int(len(classA) * 0.75)]

medianB = median(classB, len(classB))
q1B = classB[int(len(classB) * 0.25)]
q3B = classB[int(len(classB) * 0.75)]

keyPointA = {'medianA': medianA, 'q1A': q1A, 'q3A': q3A}
keyPointB = {'medianB': medianB, 'q1B': q1B, 'q3B': q3B}

print classA
print classB
print countA
print countB
print quantileA
print quantileB
print keyPointA
print keyPointB

xCorMin = 0
xCorMax = 1
yCorMin = 0
yCorMax = 20
xtick = [i/10.0 for i in range(0, xCorMax * 10 + 2 , 2)]

plt.figure(figsize=(8,8), num = "Quantile")
axes1 = plt.subplot(211)
axes1.set_xlim([xCorMin, xCorMax])
axes1.set_xticks(xtick)
axes1.set_ylim([yCorMin - 1, yCorMax + 1])
axes1.set_yticks(range(yCorMin, yCorMax + 1, 2))


axes2 = plt.subplot(212)
axes2.set_xlim([xCorMin, xCorMax])
axes2.set_xticks(xtick)
axes2.set_ylim([yCorMin - 1, yCorMax + 1])
axes2.set_yticks(range(yCorMin, yCorMax + 1, 2))

plt.sca(axes1)
plt.title('Quantile of class B')
plt.xlabel('f value')
plt.ylabel('Score')
plt.subplots_adjust(hspace = 0.3)
for x in quantileA.keys():
    axes1.plot(quantileA[x], x, color = 'yellow', marker = 'D', linestyle = '')

plt.sca(axes2)
plt.title('Quantile of class A')
plt.xlabel('f value')
plt.ylabel('Score')
for x in quantileB.keys():
    axes2.plot(quantileB[x], x, color = 'yellow', marker = 'D', linestyle = '')

for x in keyPointA.keys():
    if keyPointA[x] in quantileA.keys():
        axes1.plot(quantileA[keyPointA[x]], keyPointA[x], color = 'red', marker = 'h', linestyle = '', label = x)
        axes1.annotate(x, xy = (quantileA[keyPointA[x]], keyPointA[x]), xytext = (20, -30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))
    else:
        up = 20
        below = 0
        for v in quantileA.keys():
            if v > keyPointA[x] and v < up:
                up = v
            if v < keyPointA[x] and v > below:
                below = v
        axes1.plot((quantileA[up] + quantileA[below]) / 2.0, keyPointA[x], color = 'red', marker = 'h', linestyle = '', label = 'line 1')
        axes1.annotate(x, xy = ((quantileA[up] + quantileA[below]) / 2.0, keyPointA[x]), xytext = (20, -30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))

for x in keyPointB.keys():
    if keyPointB[x] in quantileB.keys():
        axes2.plot(quantileB[keyPointB[x]], keyPointB[x], color = 'red', marker = 'h', linestyle = '', label = x)
        axes2.annotate(x, xy = (quantileB[keyPointB[x]], keyPointB[x]), xytext = (20, -30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))
    else:
        up = 20
        below = 0
        for v in quantileB.keys():
            if v > keyPointB[x] and v < up:
                up = v
            if v < keyPointB[x] and v > below:
                below = v
        axes2.plot((quantileB[up] + quantileB[below]) / 2.0, keyPointB[x], color = 'red', marker = 'h', linestyle = '', label = 'line 1')
        axes2.annotate(x, xy = ((quantileB[up] + quantileB[below]) / 2.0, keyPointB[x]), xytext = (20, -30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))

plt.show()
