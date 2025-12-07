from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 11, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 6}
]

def parse(data):
    groups = parse_groups(data)
    return groups

# Build a dict of the numbers of yes to each question
def analyze_group(group):
    answered_questions = defaultdict(int)
    members = group.split("\n")
    for member in members:
        for c in member:
            answered_questions[c] += 1
    return answered_questions, len(members)

def part1(data):
    groups = parse(data)
    total_yes = 0
    for group in groups:
        answered_questions, members = analyze_group(group)
        # Get the total number of distinct questions with a yes answer
        total_yes+=len(answered_questions)
    return total_yes

def part2(data):
    groups = parse(data)
    total_yes = 0
    for group in groups:
        answered_questions, no_members = analyze_group(group)
        for question in answered_questions:
            # Only the questions that have been answered by all are valid
            if answered_questions[question] == no_members:
                total_yes+=1
    return total_yes
