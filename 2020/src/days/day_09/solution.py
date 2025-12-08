from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 127, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 62}
]

def parse(data):
    numbers = list(map(int,parse_lines(data)))
    return numbers

# Algorithm in O(n) time for part1 (0.28ms -> 0.04ms improvement)
def get_expense_report_two_sum(expenses):
    seen = set()
    for expense in expenses:
        complement = 2020 - expense
        if complement in seen:
            return expense * complement
        seen.add(expense)
    return -1

# Checks if the given number can be formed with the sum of any two numbers on the list
def is_valid(target, numbers):
    seen = set(numbers)
    for number in numbers:
        complement = target - number
        if complement in seen and complement != number:
            return True
    return False

# Assumes input contains an invalid number, otherwise it will be an infinite loop
def get_first_invalid(preamble, numbers):
    current_index = preamble   
    while True:
        current_window = numbers[current_index-preamble:current_index]
        if not is_valid(numbers[current_index], current_window):
            return numbers[current_index]
        current_index += 1

def get_encryption_weakness(first_invalid, numbers):
    for i in range(0,len(numbers)):
        j = i
        contigious_nums = []
        while sum(contigious_nums) < first_invalid:
            contigious_nums.append(numbers[j])
            j +=1
            if sum(contigious_nums) == first_invalid:
                return min(contigious_nums) + max(contigious_nums)
    return -1

def part1(data):
    numbers = parse(data)
    preamble = 25
    if is_test_mode():
        preamble = 5
    return get_first_invalid(preamble, numbers)
    

def part2(data):
    numbers = parse(data)
    preamble = 25
    if is_test_mode():
        preamble = 5
    
    first_invalid = get_first_invalid(preamble, numbers)
    return get_encryption_weakness(first_invalid, numbers)
