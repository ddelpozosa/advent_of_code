from lib import *
import re

TESTS = [
    {"input": "input_test_1.txt", "part1": 71, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 1}
]

#mask_str = re.search(r"mask = ([X01]+)", line).group(1)
#match = re.search(r"mem\[(\d+)\] = (\d+)", line)

def parse(data):
    groups = parse_groups(data)
    rules = []
    for rule in groups[0]:
        match = re.search(r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", rule)
        #rule_name, a1, b1, a2, b2 = match.groups()
        rules.append(match.groups())
    my_ticket = list(map(int,groups[1][1].split(',')))
    tickets = [list(map(int,ticket.split(','))) for ticket in groups[2][1:]]
    return rules, my_ticket, tickets

def get_valid_ranges(rules):
    ranges = []
    for rule in rules:
        rule_name, a1, b1, a2, b2 = rule
        a1, b1, a2, b2 = int(a1), int(b1), int(a2), int(b2)
        ranges.append((a1, b1))
        ranges.append((a2, b2))
    
    # Join overlapping ranges
    ranges.sort()
    optimized_ranges = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            optimized_ranges.append((current_start, current_end))
            current_start, current_end = start, end
    optimized_ranges.append((current_start, current_end))  # Append the last range
    return optimized_ranges

def is_valid_value(value, ranges):
    value_valid = False
    for start, end in ranges:
        if value >= start and value <= end:
            value_valid = True
            break
    if not value_valid:
        return False
    return True

def get_valid_tickets(my_ticket, tickets, ranges):
    valid_tickets = [my_ticket]
    for ticket in tickets:
        is_valid = True
        for value in ticket:
            if not is_valid_value(value, ranges):
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)
    return valid_tickets

def part1(data):
    rules, my_ticket, tickets = parse(data)
    ranges = get_valid_ranges(rules)
    invalid_sum = 0
    for ticket in tickets:
        for value in ticket:
            if not is_valid_value(value, ranges):
                invalid_sum += value
    print("The ticket scanning error rate is:",invalid_sum)
    return invalid_sum

# For each rule, check all valid ticket columns, and add that column if it could be valid for that rule
def get_valid_positions(rules, tickets):
    possible_rule_positions = defaultdict(set)
    for rule_name, start_1, end_1, start_2, end_2 in rules:
        for i in range(len(rules)):
            #debug("Checking if rule",rule_name,"is valid for all",i,"columns for every ticket")
            rule_is_i = True
            for ticket in tickets:
                if not ( (ticket[i] >= int(start_1) and ticket[i]<=int(end_1)) or (ticket[i] >= int(start_2) and ticket[i]<=int(end_2)) ):
                    debug(ticket[i],"is not included in",start_1, end_1, start_2, end_2)
                    rule_is_i = False
                    break
            if rule_is_i:
                possible_rule_positions[rule_name].add(i)
    return possible_rule_positions

# There are multiple valid columns for many rules, so we need to find the actual unique valid position
# When a rule has 1 position, eliminate that position it from others
def resolve_field_positions(rule_positions):
    rule_positions = {rule: set(positions) for rule, positions in rule_positions.items()}
    changed = True
    while changed:
        changed = False
        for rule, positions in list(rule_positions.items()):
            if len(positions) == 1:
                taken_pos = list(positions)[0]
                # Remove this position from all other rules
                for other_rule in rule_positions:
                    if other_rule != rule and taken_pos in rule_positions[other_rule]:
                        rule_positions[other_rule].discard(taken_pos)
                        changed = True 
    # Convert sets to single integers
    return {rule: list(positions)[0] for rule, positions in rule_positions.items()}

def get_result(rule_positions, my_ticket):
    result = 1
    for rule in rule_positions:
        if "departure" in rule:
            result *= my_ticket[rule_positions[rule]]
    return result

def part2(data):
    rules, my_ticket, tickets = parse(data)
    ranges = get_valid_ranges(rules)

    # Remove invalid tickets (part 1 logic)
    tickets = get_valid_tickets(my_ticket,tickets,ranges)
    debug("Valid tickets:",tickets)

    # Find all possible positions for each rule
    possible_rule_positions = get_valid_positions(rules, tickets)
    debug("Possible rule positions:",possible_rule_positions)

    # Find the actual unique position for each rule
    actual_rule_positions = resolve_field_positions(possible_rule_positions)
    debug("Actual rule positions",actual_rule_positions)

    # Multiply all values in my ticket that start with "departure"
    return get_result(actual_rule_positions,my_ticket)


