file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/6/input1.txt', 'r')
lines = file1.readlines()

def calc_total(dict):
    total = 0
    for i in dict:
        total+=dict[i]
    return total

fishArray = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
day = 1
for number in lines[0].split(","):
    fishArray[int(number)]+=1

while day <= 256:
    newBorns = fishArray[0]
    for i in range(1,len(fishArray)):
        fishArray[i-1] = fishArray[i]
        fishArray[i] = 0
    fishArray[8] = newBorns
    fishArray[6] += newBorns
    day+=1

print("Total after " + str(day) + " days: " + str(calc_total(fishArray)))