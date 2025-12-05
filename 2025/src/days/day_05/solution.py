from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 3, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 14}
]

# If unoptimized, prod runtime for part 1 is 3.29ms. With optimization, it's 1.83ms.
def optimize_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    optimized = []
    current_start, current_end = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            optimized.append((current_start, current_end))
            current_start, current_end = start, end

    optimized.append((current_start, current_end))
    return optimized

def is_fresh(ingredient_id, optimized_ranges):
    for start, end in optimized_ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def get_all_potential_fresh(optimized_ranges):
    fresh_ingredients = 0
    for start, end in optimized_ranges:
        fresh_ingredients += (end - start + 1)
    return fresh_ingredients

def parse(data):
    groups = parse_groups(data)
    raw_ranges = [tuple(map(int, line.split("-"))) for line in parse_lines(groups[0])]
    optimized_ranges = optimize_ranges(raw_ranges)
    ingredient_ids = list(map(int, parse_lines(groups[1])))
    debug(optimized_ranges)
    debug(ingredient_ids)
     
    return ingredient_ids, optimized_ranges

def part1(data):
    ingredient_ids, optimized_ranges = parse(data)
    fresh_ingredient_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, optimized_ranges):
            fresh_ingredient_count += 1
    return fresh_ingredient_count

def part2(data):
    ingredient_ids, optimized_ranges = parse(data)
    return get_all_potential_fresh(optimized_ranges)
