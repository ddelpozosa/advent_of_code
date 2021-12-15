import numpy as np
from math import atan, degrees
file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/5/input1.txt', 'r')
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
    elif degrees(atan( abs(endPoint[1]-startPoint[1]) / abs(endPoint[0]-startPoint[0]))) == 45.0:
        print(degrees(atan( abs(endPoint[1]-startPoint[1]) / abs(endPoint[0]-startPoint[0]))))
        rectas.append([startPoint, endPoint])
        if startPoint[0] > max:
            max = startPoint[0]
        elif startPoint[1] > max:
            max = startPoint[1]
        elif endPoint[0] > max:
            max = endPoint[0]
        elif endPoint[1] > max:
            max = endPoint[1]
    else:
        print()
max +=1
print(rectas)
print(max)

resultArray = np.zeros((max,max))
reversedX = 1
reversedY = 1
for recta in rectas:
    reversedX = 1
    reversedY = 1
    if recta[0][0] == recta[1][0] or recta[0][1] == recta[1][1]:
        if recta[0][0] > recta[1][0]:
            reversedX = -1
        if recta[0][1] > recta[1][1]:
            reversedY = -1
        for x in range(recta[0][0],recta[1][0]+reversedX, reversedX):
            for y in range(recta[0][1],recta[1][1]+reversedY,reversedY): 
                resultArray[y][x] = resultArray[y][x] + 1
    else:
        if recta[0][0] > recta[1][0]:
            reversedX = -1
        if recta[0][1] > recta[1][1]:
            reversedY = -1
        #print("recta: " + str(recta[0]) + str(recta[1]))
        xArray=[]
        yArray=[]
        for x in range(recta[0][0],recta[1][0]+reversedX, reversedX):
            xArray.append(x)
        for y in range(recta[0][1],recta[1][1]+reversedY,reversedY): 
            yArray.append(y)
        for i in range(len(xArray)):
           # print((xArray[i],yArray[i]))
            resultArray[yArray[i]][xArray[i]] = resultArray[yArray[i]][xArray[i]] + 1
#print(resultArray)

print(np.count_nonzero(resultArray > 1))


