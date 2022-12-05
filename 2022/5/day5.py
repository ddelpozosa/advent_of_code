import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

def getIndexOfStacks(input):
    for i, line in enumerate(input):
        #print(line.strip())
        for char in line:
            if char.isdigit():
                return i

def parseInput(input):
    stacks = {}
    movements = []
    indexOfStacks = getIndexOfStacks(lines)

    ### Init Stacks ###
    for stackIndex in lines[indexOfStacks].strip().split("   "):
        stacks[stackIndex] = []
    index = indexOfStacks - 1

    ### Add crates to Stacks ###
    while index >= 0:
        line = lines[index]
        for stack in stacks:
            #print(1+((int(stack)-1)*4))
            crate = line[1+((int(stack)-1)*4)]
            #print(f'Crate for line with index {index} and stack {stack} is {crate}')
            if crate != " ":
                stacks[stack].append(crate)
        index -= 1

    ### Parse movements ###
    index = indexOfStacks + 2
    while index < len(lines):
        movementLine = lines[index].strip().split(" ")
        movements.append({"amount":movementLine[1],"from":movementLine[3],"to":movementLine[5]})
        index +=1
    return stacks, movements

### Part 1 ###
stacks,movements = parseInput(input)
#print(f'Initial Stack: {stacks}')
for movement in movements:
    cratesLeftToMove = int(movement["amount"])
    while cratesLeftToMove > 0:
        stacks[movement["to"]].append(stacks[movement["from"]].pop())
        cratesLeftToMove -= 1
#print(f'Final Stack: {stacks}')

firstCrates = ""
for stack in stacks:
    firstCrates += stacks[stack].pop()
print(f'Final message for Part 1 is: {firstCrates}')


### Part 2 ###
stacks,movements = parseInput(input)
#print(f'Initial Stack: {stacks}')
for movement in movements:
    cratesToMove = int(movement["amount"])
    crates = stacks[movement["from"]]
    takenCrates = crates[len(crates)-cratesToMove:len(crates)]
    
    for crate in takenCrates:
        stacks[movement["to"]].append(crate)
        stacks[movement["from"]].pop()
print(f'Final Stack: {stacks}')

firstCrates = ""
for stack in stacks:
    firstCrates += stacks[stack].pop()
print(f'Final message for Part 1 is: {firstCrates}')
