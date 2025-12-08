from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 5, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 8}
]

# instructions are a dictionary with value (operation, argument)
def parse(data):
    lines = parse_lines(data)
    instructions = dict()
    id = 0
    for line in lines:
        op, argument = line.split(" ")[0], int(line.split(" ")[1])
        instructions[id] = (op,argument)
        id += 1
    return instructions

def get_next(current_id, instructions, accumulator):
    op, argument = instructions[current_id]
    if op == "acc":
        accumulator += argument
        current_id += 1
    elif op == "jmp":
        current_id += argument
    else:
        current_id += 1
    
    if current_id >= len(instructions):
        current_id -= len(instructions)

    return current_id, instructions, accumulator

def compute(instructions):
    current_id = accumulator = 0
    visited = set()
    while current_id not in visited:
        visited.add(current_id)
        # End reached
        if current_id == len(instructions)-1:
            # We still need to calculate the accumulator
            current_id, instructions, accumulator = get_next(current_id, instructions, accumulator)
            return accumulator, False
        current_id, instructions, accumulator = get_next(current_id, instructions, accumulator)
    return accumulator, True
# Goal: find when an instruction is run a second time
# Backlog: 
#  - parse the instruction into ops and values
#  - write the boot function
def part1(data):
    instructions = parse(data)
    accumulator, recursion = compute(instructions)
    return accumulator

def part2(data):
    instructions = parse(data)
    for instruction in instructions:
        new_instructions = instructions.copy()
        op, arg = instructions[instruction]
        if op == "jmp":
            new_instructions[instruction] = ("nop",arg)
        elif op == "nop":
            new_instructions[instruction] = ("jmp",arg)
        else:
            continue # we just process changes in jmp or nop
        debug("Trying : ", new_instructions)
        accumulator, recursion = compute(new_instructions)
        if recursion == False:
            return accumulator
    return -1
