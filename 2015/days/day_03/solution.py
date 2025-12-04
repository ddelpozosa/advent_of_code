from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 2, "part2": None},
    {"input": "input_test_2.txt", "part1": 4, "part2": None},
    {"input": "input_test_3.txt", "part1": 2, "part2": 11}
]

DEF_MOVEMENTS = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}

def parse(data):
    movements = parse_lines(data)
    # Custom logic here
    return movements[0]

def get_visited_houses(movements):
    houses = set()
    position = (0, 0)
    houses.add(position)
    for move in movements:
        position = (position[0] + DEF_MOVEMENTS[move][0], position[1] + DEF_MOVEMENTS[move][1])
        houses.add(position)
    return len(houses)

def get_visited_houses_with_robo(movements):
    houses = set()
    pos1 = (0, 0)
    pos2 = (0, 0)
    houses.add(pos1)
    for i in range(len(movements)):
        move = movements[i]
        if i % 2 == 0:
            pos1 = (pos1[0] + DEF_MOVEMENTS[move][0], pos1[1] + DEF_MOVEMENTS[move][1])
            houses.add(pos1)
        else:
            pos2 = (pos2[0] + DEF_MOVEMENTS[move][0], pos2[1] + DEF_MOVEMENTS[move][1])
            houses.add(pos2)
    return len(houses)

def part1(data):
    movements = parse(data)
    return get_visited_houses(movements)

def part2(data):
    movements = parse(data)
    return get_visited_houses_with_robo(movements)
