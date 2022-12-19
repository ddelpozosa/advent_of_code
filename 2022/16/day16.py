from pathlib import Path
import ast

p = Path(__file__).with_name('test.txt')

f = p.open('r')
lines = f.readlines()

