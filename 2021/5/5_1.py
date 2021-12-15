import numpy as np

file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/5/test1.txt', 'r')
lines = file1.readlines()

rectas = []
max = 0
for line in lines:
    splittedLine = line.split("->")
    startPoint = (int(splittedLine[0].split(",")[0]),int(splittedLine[0].split(",")[1]))
    endPoint = (int(splittedLine[1].split(",")[0]),int(splittedLine[1].split(",")[1]))

    if startPoint[0] == endPoint[0] or startPoint[1] == endPoint[1]:
        rectas.append([startPoint, endPoint])
        if startPoint[0] > max:
            max = startPoint[0]
        elif startPoint[1] > max:
            max = startPoint[1]
        elif endPoint[0] > max:
            max = endPoint[0]
        elif endPoint[1] > max:
            max = endPoint[1]
max +=1
print(rectas)
print(len(rectas))
print(max)

resultArray = np.zeros((max,max))
reversedX = 1
reversedY = 1
for recta in rectas:
    reversedX = 1
    reversedY = 1
    if recta[0][0] > recta[1][0]:
        reversedX = -1
    if recta[0][1] > recta[1][1]:
        reversedY = -1
    for x in range(recta[0][0],recta[1][0]+reversedX, reversedX):
        for y in range(recta[0][1],recta[1][1]+reversedY,reversedY): 
            resultArray[y][x] = resultArray[y][x] + 1
#print(resultArray)

print(np.count_nonzero(resultArray > 1))