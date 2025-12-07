from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 7, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 336}
]

SLOPES = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def parse(data):
    trees = set()
    lines = parse_lines(data)
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == '#':
                trees.add((x,y))
    return trees, len(lines[0]), len(lines)

def drive_toboggan(trees, slope, max_x, max_y):
    x, y = 0, 0
    found_trees = 0
    while y < max_y:
        x += slope[0]
        y += slope[1]
        if x >= max_x:
            x = x - max_x 
        if (x,y) in trees:
            found_trees += 1
    return found_trees

def part1(data):
    trees, max_x, max_y = parse(data)
    return drive_toboggan(trees, (3,1), max_x, max_y)

def part2(data):
    trees, max_x, max_y = parse(data)
    total = 1
    for slope in SLOPES:
        total *= drive_toboggan(trees, slope, max_x, max_y)
    return total
