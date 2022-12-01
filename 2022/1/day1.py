import os

from pathlib import Path
p = Path(__file__).with_name('test.txt')

f = p.open('r')
lines = f.readlines()

print(lines)