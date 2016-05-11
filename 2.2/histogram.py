import os
from operator import itemgetter
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'score.data')
scoreIn = open(file_path, 'r')
tmp = scoreIn.readline().strip().split()
classA = []
classB = []
L = range(0, 21, 1)
countA = {v:0 for v in L}
countB = {v:0 for v in L}
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

print classA
print classB
print countA
print countB

xCorMin = 0
xCorMax = 5
yCorMin = 10
yCorMax = 20

plt.figure(figsize=(8,8), num = "Histogram")
axes1 = plt.subplot(211)
axes1.set_xlim([yCorMin - 1, yCorMax + 1])
axes1.set_xticks(range(yCorMin, yCorMax + 1, 1))
axes1.set_ylim([xCorMin, xCorMax])
axes1.set_yticks(range(0, xCorMax + 1, 1))

axes2 = plt.subplot(212)
axes2.set_xlim([yCorMin - 1, yCorMax + 1])
axes2.set_xticks(range(yCorMin, yCorMax + 1, 1))
axes2.set_ylim([xCorMin, xCorMax])
axes2.set_yticks(range(0, xCorMax + 1, 1))

plt.sca(axes1)
plt.title('Score of class A')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.subplots_adjust(hspace = 0.3)
for x in countA.keys():
    if x > 10:
        plt.axvspan(x - 0.5, x + 0.5, ymin = 0, ymax = 1.0 * countA[x] / xCorMax, facecolor = 'blue', alpha = 0.5)
plt.sca(axes2)
plt.title('Score of class B')
plt.xlabel('Score')
plt.ylabel('Number of Students')
for x in countB.keys():
    if x > 10:
        plt.axvspan(x - 0.5, x + 0.5, ymin = 0, ymax = 1.0 * countB[x] / xCorMax, facecolor = 'blue', alpha = 0.5)

plt.show()
