from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 0, "part2": None},
    {"input": "input_test_2.txt", "part1": 3, "part2": None},
    {"input": "input_test_3.txt", "part1": 3, "part2": None},
    {"input": "input_test_4.txt", "part1": -3, "part2": None}
]

def parse(data):
    lines = parse_lines(data)
    return lines[0]

def get_final_floor(instructions):
    floor = 0
    for char in instructions:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor

def get_first_basement_position(instructions):
    floor = 0
    for i in range(len(instructions)):
        if instructions[i] == "(":
            floor += 1
        elif instructions[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    return -1


def part1(data):
    instructions = parse(data)
    return get_final_floor(instructions)

def part2(data):
    instructions = parse(data)
    return get_first_basement_position(instructions)
