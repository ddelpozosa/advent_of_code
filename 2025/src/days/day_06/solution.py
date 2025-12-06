from lib import *
import re
import numpy as np

TESTS = [
    {"input": "input_test_1.txt", "part1": 4277556, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 3263827}
]

# Used numpy arrays for efficiency, but actually the input is small enough 
# that the list would be actually more efficient.
# However, still useful for parsing due to the easy transposition
def parse(data):
    lines = parse_lines(data)
    all_rows = []
    for line in lines[:len(lines)-1]:
        row = list(map(int,re.findall(r'\d+',line)))
        all_rows.append(row)
    arr_2d = np.array(all_rows)
    problems = arr_2d.T
    
    operations = re.findall(r'[^\s]+',lines[-1])
    return problems, operations

def parse_part_2(data):
    lines = data.split('\n')
    #Get the number of spaces after each operation symbol (length of the numbers to be read)
    space_counts = [len(match) for match in re.findall(r'\s+', lines[-1])]
    #Add one space to the end (missing "extra" space)
    space_counts[-1] = space_counts[-1] + 1
    all_rows = []
    current_index = 0
    for space_count in space_counts:
        row = []
        for i in range(space_count-1, -1,-1):
            number_index = current_index + i
            number_str = ""
            for l in range(0,len(lines)-1):
                if lines[l][number_index] != " ":
                    number_str += lines[l][number_index]
            if number_str != "":
                row.append(int(number_str))
        all_rows.append(row)
        current_index += space_count + 1
    
    # Don't convert to NumPy array because of arrays of different size not being supported
    operations = re.findall(r'[^\s]+',lines[-1])
    return all_rows, operations  # Return list instead

def process_problems(problems, operations):
    grand_total = 0
    for i in range(0, len(operations)):
        op = operations[i]
        sub_total = 0
        if op == '+':
            if isinstance(problems[i], list): #part2
                sub_total = sum(problems[i])
            else: #part 1 (numpy array)
                sub_total = problems[i].sum() 
        elif op == '*':
            if isinstance(problems[i], list): #part2
                sub_total = 1
                for num in problems[i]:
                    sub_total *= num
            else: #part 1 (numpy array)
                sub_total = problems[i].prod() 
        debug("The result of the ", operations[i], " for ", problems[i], " is: ", sub_total)
        grand_total += sub_total
    return grand_total

def part1(data):
    problems, operations = parse(data)
    debug(problems, operations)
    grand_total = process_problems(problems,operations)
    
    return grand_total

def part2(data):
    converted_problems, operations = parse_part_2(data)
    debug(converted_problems, operations)
    grand_total = process_problems(converted_problems,operations)

    return grand_total
