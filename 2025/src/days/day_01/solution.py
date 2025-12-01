from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 3, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 6},
    {"input": "input_test_2.txt", "part1": None, "part2": 8},
    {"input": "input_test_3.txt", "part1": None, "part2": 10}
]

def parse(data):
    lines = parse_lines(data)
    # Custom logic here
    rotations = []
    for line in lines:
        if line[0] == "L":
            rotations.append(-int(line[1:]))
        else:
            rotations.append(int(line[1:]))

    return rotations

def calculate_rotations(dial_start, rotations, part=1):
    dial = dial_start
    number_of_ceroes = 0
    for rotation in rotations:
        if part == 1:
            dial = (dial + rotation) % 100
            if dial == 0:
                number_of_ceroes += 1
        if part == 2:
            if rotation > 0:  # R (right/positive)
                number_of_ceroes += (dial + rotation) // 100
                dial = (dial + rotation) % 100
            else:  # L (left/negative)
                flipped_dial = (100 - dial) % 100
                number_of_ceroes += (flipped_dial + abs(rotation)) // 100
                dial = (dial + rotation) % 100

        debug("Rotated", rotation, "to", dial, "| passes:", number_of_ceroes)
    
    return dial, number_of_ceroes

def part1(data):
    rotations = parse(data)
    debug("Parsed rotations: ", rotations)
    final_dial, number_of_ceroes = calculate_rotations(50, rotations)
    debug("Final dial position: ", final_dial, " with ", number_of_ceroes, " ceroes hit.")
    return number_of_ceroes

def part2(data):
    rotations = parse(data)
    debug("Parsed rotations: ", rotations)
    final_dial, number_of_ceroes = calculate_rotations(50, rotations, part=2)
    debug("Final dial position: ", final_dial, " with ", number_of_ceroes, " ceroes hit.")
    return number_of_ceroes