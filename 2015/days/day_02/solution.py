from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 101, "part2": 48}
]

def parse(data):
    presents = []
    for present in parse_lines(data):
        presents.append(list(map(int, present.split("x"))))
    # Custom logic here
    return presents

def calculate_present_area(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def calculate_ribbon_area (l,w,h):
    return l*w*h + min(2*(l+w), 2*(w+h), 2*(h+l))

def get_total_wrapping_area(presents):
    total_area = 0
    for present in presents:
        l, w, h = present
        total_area += calculate_present_area(l, w, h)
    return total_area

def get_total_ribbon_area(presents):
    total_ribbon = 0
    for present in presents:
        l, w, h = present
        total_ribbon += calculate_ribbon_area(l, w, h)
    return total_ribbon

def part1(data):
    presents = parse(data)
    return get_total_wrapping_area(presents)

def part2(data):
    presents = parse(data)
    return get_total_ribbon_area(presents)
