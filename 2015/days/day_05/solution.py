from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 2, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 3}
]

FORBIDDEN_STRINGS = ["ab", "cd", "pq", "xy"]
VOWELS = "aeiou"

def str_is_really_nice(str):
    has_double_pair = False
    for i in range(len(str) - 1):
        if str[i:i+2] in str[i+2:]:
            has_double_pair = True
            break
    has_double_with_middle = False
    for i in range(len(str) - 2):
        if str[i] == str[i+2]:
            has_double_with_middle = True
            break
    debug(str,"-- has_double_with_middle=", has_double_with_middle, ", has_double_pair=", has_double_pair)
    if not has_double_with_middle or not has_double_pair:
        return False
    return True

def str_is_nice(str):
    if any(fs in str for fs in FORBIDDEN_STRINGS):
        return False
    vowel_count = sum(1 for c in str if c in VOWELS)
    if vowel_count < 3:
        return False
    has_double = any(str[i] == str[i+1] for i in range(len(str) - 1))
    if not has_double:
        return False
    return True

def get_nice_strings_count(strings, part):
    count = 0
    for s in strings:
        if part == 1 and str_is_nice(s):
            debug(s," is nice")
            count += 1
        elif part == 2 and str_is_really_nice(s):
            debug(s," is really nice")
            count += 1
        else:
            debug(s," is naughty")
    return count

def parse(data):
    strings = parse_lines(data)
    return strings

def part1(data):
    strings = parse(data)
    return get_nice_strings_count(strings, part=1)

def part2(data):
    strings = parse(data)
    return get_nice_strings_count(strings, part=2)
