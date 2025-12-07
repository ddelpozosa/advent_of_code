from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 514579, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 241861950}
]

def parse(data):
    expenses = list(map(int,parse_lines(data)))
    return expenses

# Straightforward solution - O(n2) for part 1 and O(n3) for part 2
def get_expense_report(expenses, part):
    for i in range(0,len(expenses)):
        for j in range(0,len(expenses)):
            if part == 2:
                for k in range(0,len(expenses)):
                    if expenses[i] + expenses[j] + expenses[k] == 2020:
                        return expenses[i] * expenses[j] * expenses[k]
            elif expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]
    return -1

# Algorithm in O(n) time for part1 (0.28ms -> 0.04ms improvement)
def get_expense_report_two_sum(expenses):
    seen = set()
    for expense in expenses:
        complement = 2020 - expense
        if complement in seen:
            return expense * complement
        seen.add(expense)
    return -1

# Algorithm in O(n2) time for part2 (18.94ms -> 0.21ms improvement)
def get_expense_report_three_sum_hash(expenses):
    expense_set = set(expenses)
    
    for i in range(len(expenses)):
        for j in range(i + 1, len(expenses)):
            complement = 2020 - expenses[i] - expenses[j]
            if complement in expense_set and complement != expenses[i] and complement != expenses[j]:
                return expenses[i] * expenses[j] * complement
    return -1

def part1(data):
    expenses = parse(data)
    return get_expense_report_two_sum(expenses)

def part2(data):
    expenses = parse(data)
    return get_expense_report_three_sum_hash(expenses)
