from lib import *
import re

TESTS = [
    {"input": "input_test_1.txt", "part1": 2, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 1}
]

def parse(data):
    password_lines = parse_lines(data)
    return password_lines

def is_valid(password_line, part):
    pattern = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"
    match = re.match(pattern, password_line)

    if not match:
        return None
    
    if part == 1:
        min_count,max_count,letter,password = match.groups()
        count = password.count(letter)
        if count >= int(min_count) and count <= int(max_count):
            return 1 # valid
        else:
            return 0 # invalid
    elif part == 2:
        index_1, index_2, letter, password = match.groups()
        count = 0
        if int(index_1) <= len(password) and password[int(index_1)-1] == letter:
            count += 1
        if int(index_2) <= len(password) and password[int(index_2)-1] == letter:
            count += 1
        if count == 1:
            return 1
        else:
            return 0


def get_valid_passwords(password_lines, part):
    total = 0
    for password_line in password_lines:
        total += is_valid(password_line, part)
    return total

def part1(data):
    password_lines = parse(data)
    return get_valid_passwords(password_lines, 1)

def part2(data):
    password_lines = parse(data)
    return get_valid_passwords(password_lines, 2)
