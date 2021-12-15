file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/6/input1.txt', 'r')
lines = file1.readlines()

fishArray = []
for number in lines[0].split(","):
    fishArray.append(int(number))

print("Initial State: " + str(fishArray))
day = 1
while day <= 256:
    tempFishArray = []
    for fish in fishArray:
        if fish == 0:
            tempFishArray.append(6)
            tempFishArray.append(8)
        else:
            tempFishArray.append(fish-1)
    fishArray = tempFishArray
    day+=1
    print("After " + str(day-1) + " days: " + str(len(fishArray)))

print("There are " + str(len(fishArray)) + " fish.")