import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

numberOfFullyContainedPairs = 0
numberOfOverlaps = 0
for line in lines:
    pair = []
    for elf in line.strip().split(','):
        pair.append([ int(x) for x in elf.split("-")])
    
    ### Part 1 ###
    if pair[0][0] <= pair[1][1] and pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1] and pair[0][1] >= pair[1][0]:
        numberOfFullyContainedPairs += 1
    elif pair[1][0] <= pair[0][1] and pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1] and pair[1][1] >= pair[0][0]:
        numberOfFullyContainedPairs += 1

    ### Part 2 ###
    if pair[0][0] <= pair[1][1] and pair[0][0] >= pair[1][0] or pair[0][1] <= pair[1][1] and pair[0][1] >= pair[1][0]:
        numberOfOverlaps += 1
    elif pair[1][0] <= pair[0][1] and pair[1][0] >= pair[0][0] or pair[1][1] <= pair[0][1] and pair[1][1] >= pair[0][0]:
        numberOfOverlaps += 1
print(f'There are {numberOfFullyContainedPairs} fully contained pairs.')
print(f'There are {numberOfOverlaps} overlaps.')