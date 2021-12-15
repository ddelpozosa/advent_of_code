file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/8/input1.txt', 'r')
lines = file1.readlines()

uniqueLengths = [2,3,4,7]
uniqueDigits = 0
for line in lines:
    for number in line.split("|")[1].split(" "):
        if len(number.strip()) in uniqueLengths:
            uniqueDigits +=1
            #print(number.strip() + " is unique!")

print("There are " + str(uniqueDigits) + " unique digits.")
