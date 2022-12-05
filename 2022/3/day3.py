import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

def charToValue(char):
    if(ord(char) >= 97):
        return ord(char) - 96
    else:
        return ord(char) - 38

### Part 1 ###
output = []
for rucksack in lines:
    rucksack = rucksack.strip()
    firstCompartment, secondCompartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

    firstSet = set(firstCompartment)
    secondSet = set(secondCompartment)

    for item in firstSet:
        if item in secondSet:
            output.append(item)

total = 0
for char in output:
    total += charToValue(char)

###print(f'Duplicated items are: {output}')
print(f'Total value of duplicated items are: {total}')

### Part 2 ###
output = []
groupSet = set()
for i, rucksack in enumerate(lines):
    rucksack = rucksack.strip()
    ### if it's the first rucksack of a group reset the badge filter
    if (i+1)%3 == 1: 
        groupSet = set()
    if len(groupSet) == 0:
        groupSet = set(rucksack)
    else:
        newGroupSet = set()
        for char in set(rucksack):
            if char in groupSet:
                newGroupSet.add(char)
        groupSet = newGroupSet
    ### if it's the last rucksack of a group add badge to output list
    if (i+1)%3 == 0:
        output.append(groupSet.pop())

total = 0
for char in output:
    total += charToValue(char)

###print(f'Badges: {output}')
print(f'Total value of badges is: {total}')