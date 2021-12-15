file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/7/input1.txt', 'r')
lines = file1.readlines()

crabSubs = {}
day = 1
max = 0
for c in lines[0].split(","):
    number = int(c)
    if number in crabSubs.keys():
        crabSubs[number]+=1
    else: 
        crabSubs[number]=1
    if max < number:
        max = number

print("Max is " + str(max))

minFuel = 9999999999999999
hpos = -1
for i in range(0,max):
    roundFuel = 0
    for sub in crabSubs:
        roundFuel += abs(i-sub) * crabSubs[sub]
    if roundFuel < minFuel:
        minFuel = roundFuel
        hpos = i

print("Minimum amount of fuel is: " + str(minFuel) + " at horizontal position: " + str(hpos))