import numpy as np
from lib import *


TESTS = [
    {"input": "input_test_1.txt", "part1": 998996, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 1},
    {"input": "input_test_3.txt", "part1": None, "part2": 2000000}
]

def parse(data):
    lines = parse_lines(data)
    instructions = []
    for line in lines:
        end = line.split(" through ")[1]
        if "turn on " in line:
            start = line.split("turn on ")[1].split(" through ")[0]
            action = "on"
        elif "turn off " in line:
            start = line.split("turn off ")[1].split(" through ")[0]
            action = "off"
        elif "toggle " in line:
            start = line.split("toggle ")[1].split(" through ")[0]
            action = "toggle"
        instructions.append((action, tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))))
    return instructions

def init_grid():
    grid = dict()
    for i in range(0,1000):
        for j in range(0,1000):
            grid[(i,j)] = 0 #indicates brightness level
    return grid

#First implementation was set() with Python for loop -> very innefficient 12s
#Current runtime in prod: 2.06ms
def apply_instructions(instructions):
    grid = np.zeros((1000, 1000), dtype=bool)  # Boolean array for on/off
    for action, (x1, y1), (x2, y2) in instructions:
        if action == "on":
            grid[x1:x2+1, y1:y2+1] = True
        elif action == "off":
            grid[x1:x2+1, y1:y2+1] = False
        elif action == "toggle":
            grid[x1:x2+1, y1:y2+1] = ~grid[x1:x2+1, y1:y2+1]
    return np.sum(grid) 

#First implementation was dict() with Python for loop -> very innefficient 14s
#Current runtime in prod: 34.63ms
def apply_instructions_part_2(instructions):
    grid = np.zeros((1000, 1000), dtype=int)  # Boolean array for on/off
    for action, (x1, y1), (x2, y2) in instructions:
        if action == "on":
            grid[x1:x2+1, y1:y2+1] += 1
        elif action == "off":
            grid[x1:x2+1, y1:y2+1] = np.maximum(grid[x1:x2+1, y1:y2+1] - 1, 0)
        elif action == "toggle":
            grid[x1:x2+1, y1:y2+1] += 2
    return np.sum(grid) 

def part1(data):
    instructions = parse(data)
    lit_lights = apply_instructions(instructions)
    return lit_lights

def part2(data):
    instructions = parse(data)
    total_brightness = apply_instructions_part_2(instructions)
    return total_brightness