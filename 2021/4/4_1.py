import numpy as np

file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/4/input1.txt', 'r')
lines = file1.readlines()

def check_if_bingo(bingo, bingoNumbers):
    bingo_array = np.array(bingo)
    bingoSet = set(bingoNumbers)
    #check rows
    for row in bingo_array:
        if bingoSet.issuperset(row):
            return True
    #check columns
    for column in bingo_array.T:
        if bingoSet.issuperset(column):
            return True
    return False

def sum_bingo(bingo, bingoNumbers):
    sum = 0
    for row in bingo:
        for number in row:
            if number not in bingoNumbers:
                sum += int(number)
    return sum

numberInput = lines[0].strip().split(",")
print(numberInput)
lines = lines[2:]
i = 0
bingoArray = []
bingo = []
for line in lines:
    if line == "\n":
        bingoArray.append(bingo)
        bingo = []
    else:
        #print("line is: " + line)
        lineArray = []
        for number in line.strip().split(" "):
            if number!="":
                lineArray.append(number)
        bingo.append(lineArray)

print(len(bingoArray))
currentNumberInput = []
isBingo = False
sumBingo = 0
bingoNumber = 0
for number in numberInput:
    if isBingo is False:
        currentNumberInput.append(number)
        for bingo in bingoArray:
            if check_if_bingo(bingo, currentNumberInput):
                print("BINGO AT NUMBER: " + number)
                bingoNumber = int(number)
                sumBingo = sum_bingo(bingo, currentNumberInput)
                isBingo = True
                break

print(currentNumberInput)
print("Sum of unmarked numbers in winning bingo: " + str(sumBingo))
print("The number that won the bingo: " + str(bingoNumber))
print("Multiplication of both: " + str(sumBingo*bingoNumber))
#print(bingoNumpyArray[0])
#print(bingoNumpyArray[0].T)
#print("check if bingo is " + str(check_if_bingo(bingoArray[0], numberInput)))

