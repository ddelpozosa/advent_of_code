from lib import *
import re
TESTS = [
    {"input": "input_test_1.txt", "part1": 4, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": None}
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
                values[matches_value.groups()[1]] = matches_value.groups()[0]
        rules[key]=values
    return rules

def has_shiny_gold(bag, rules):
    visited = set()
    if bag == "shiny gold":
        return 1
    next_bags = rules[bag]
    #debug(" ",next_bags)
    for next_bag in next_bags:
        #debug("  ",next_bag)
        if next_bag not in visited:
            #visited.add(next_bag)
            return has_shiny_gold(next_bag,rules)
    return 0

def part1(data):
    rules = parse(data)
    shiny_gold_containers = 0
    for bag in rules:
        if bag != "shiny gold":
            shiny_gold_containers += has_shiny_gold(bag,rules)
    return shiny_gold_containers

def part2(data):
    parsed = parse(data)
    return 0
