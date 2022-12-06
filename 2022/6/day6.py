import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
line = f.readlines()[0]

buffer = []
firstMarkerIndex = 0

### Part 1 ###
for i, char in enumerate(line):
    buffer.append(char)
    if len(buffer) > 4:
        del buffer[0]
    if len(set(buffer)) == 4:
        firstMarkerIndex = i + 1
        print(f'Start marker found! : {buffer} in position {firstMarkerIndex}')
        break
    
### Part 2 ###
for i, char in enumerate(line):
    buffer.append(char)
    if len(buffer) > 14:
        del buffer[0]
    if len(set(buffer)) == 14:
        firstMarkerIndex = i + 1
        print(f'Start marker found! : {buffer} in position {firstMarkerIndex}')
        break