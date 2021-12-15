from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "test1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

rows, cols = len(lines), len(lines[0])
cave = []
for line in lines:
    caveLine = []
    for risk in line:
        caveLine.append(int(risk))
    cave.append(caveLine)



stop = timeit.default_timer()

print('Time: ', stop - start)  