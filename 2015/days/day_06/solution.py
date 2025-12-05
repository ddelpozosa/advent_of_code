from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 4, "part2": None}
]

def parse(data):
    lines = parse_lines(data)
    instructions = []
    for line in lines:
        end = line.split(" through ")[1]
        if line.contains("turn on"):
            start = line.split("turn on ")[1].split(" through ")[0]
            action = "on"
        elif line.contains("turn off"):
            start = line.split("turn off ")[1].split(" through ")[0]
            action = "off"
        elif line.contains("toggle"):
            start = line.split("toggle ")[1].split(" through ")[0]
            action = "toggle"
        instructions.append((action, tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))))
    return instructions

def part1(data):
    parsed = parse(data)
    return 0

def part2(data):
    parsed = parse(data)
    return 0
