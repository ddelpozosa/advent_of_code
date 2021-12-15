import sys

file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/7/input1.txt', 'r')
lines = file1.readlines()
sys.setrecursionlimit(2000)

def step_fuel(steps, sum = 0, lastAdd = 0):
    lastAdd += 1
    sum += lastAdd
    if steps > 1:
        return step_fuel(steps - 1, sum, lastAdd)
    else:
        return sum

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



minFuel = 9999999999999999
hpos = -1
for i in range(0,max+1):
    roundFuel = 0
    print("Round " + str(i) + "/" + str(max))
    for sub in crabSubs:
        roundFuel += step_fuel(abs(i-sub)) * crabSubs[sub]
        #roundFuel += int((abs(i-sub) * (abs(i-sub) + 1))/2)* crabSubs[sub]
    if roundFuel < minFuel:
        minFuel = roundFuel
        print("New min fuel! " + str(minFuel))
        hpos = i

print("Minimum amount of fuel is: " + str(minFuel) + " at horizontal position: " + str(hpos))

