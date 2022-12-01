import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()
lines.append("\n")

topThree = [0,0,0]
highestElf = 0
currentElf = 0
for line in lines:
    if line == "\n":
        ### Part 1 ###
        if highestElf < currentElf:
            highestElf = currentElf
        
        ### Part 2 ###
        topThree.append(currentElf)
        topThree.remove(min(topThree))

        currentElf = 0
    else:
        currentElf += int(line)

print(f'The elf with the most calories has {highestElf} calories')

print(f'The top 3 elfs have the following calories: {topThree}')

print(f'The top 3 elfs have a total of {sum(topThree)} calories')
