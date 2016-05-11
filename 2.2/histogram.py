import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, 'score.data')
scoreIn = open(file_path, 'r')
tmp = scoreIn.readline().strip().split()
classA = []
classB = []
for x in tmp:
    classA.append(int(x))
tmp = scoreIn.readline().strip().split()
for x in tmp:
    classB.append(int(x))
scoreIn.close()

print classA
print classB
