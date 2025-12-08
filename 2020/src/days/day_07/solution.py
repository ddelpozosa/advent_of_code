from lib import *
import re
TESTS = [
    {"input": "input_test_1.txt", "part1": 4, "part2": 32},
    {"input": "input_test_2.txt", "part1": None, "part2": 126}
]

# Bag A contains 1 Bag B and 2 Bag C
a = {"Bag A": {"Bag B":1,"Bag C":2}}

# Need to build a list of such dict
def parse(data):
    lines = parse_lines(data)
    rules = dict()
    
    for line in lines:
        matches = re.match(r'(^.+) bags contain(\s.+).$',line)
        key = matches.groups()[0]
        values = dict()
        for value_str in matches.groups()[1].split(","):
            matches_value = re.match(r' (\d) (.+) bag', value_str)
            if matches_value:
                values[matches_value.groups()[1]] = int(matches_value.groups()[0])
        rules[key]=values
    return rules

def has_shiny_gold(bag, rules):
    # We found the bag!
    if bag == "shiny gold":
        return 1
    next_bags = rules[bag]
    shiny_bags = 0
    for next_bag in next_bags:
        shiny_bags += has_shiny_gold(next_bag,rules)
    return int(shiny_bags > 0) # We just care about whether there are shiny bags or not

def get_number_of_bags(bag, rules):
    next_bags = rules[bag]
    total = 1
    # If there are no bags within it, for not trigger (return 1)
    for next_bag in next_bags:
        # If the bag contains bag, we multiply the number of bags by the number of bags it contains, and add it to the total
        total += next_bags[next_bag] * get_number_of_bags(next_bag,rules)
    return total

def part1(data):
    rules = parse(data)
    shiny_gold_containers = 0
    for bag in rules:
        if bag != "shiny gold": # Don't count the shiny god bag itself
            shiny_gold_containers += has_shiny_gold(bag,rules)
    return shiny_gold_containers

def part2(data):
    rules = parse(data)
    return get_number_of_bags("shiny gold", rules) - 1 # We don't count the original bag itself
