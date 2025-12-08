from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 0, "part2": None},
    {"input": "input_test_2.txt", "part1": 220, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 19208}
]

def parse(data):
    adapters = [int(adapter) for adapter in parse_lines(data)]
    adapters = sorted(adapters)
    adapters = [0] + adapters + [adapters[-1] + 3]  # Add outlet and device
    return adapters

def get_diffs(adapters):
    diffs_1 = 0
    diffs_3 = 0
    for i in range(0,len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            diffs_1 += 1
        elif adapters[i+1] - adapters[i] == 3:
            diffs_3 += 1
    debug(diffs_1,diffs_3)
    return diffs_1 * diffs_3

def part1(data):
    adapters = parse(data)
    return get_diffs(adapters)

def get_number_of_arrangements(adapters):
    # dp[i] = number of ways to reach adapter at index i
    dp = [0] * len(adapters)
    dp[0] = 1  # One way to be at the outlet (start there)
    
    for i in range(1, len(adapters)):
        # Check all previous adapters
        for j in range(i):
            # If we can connect from j to i (within 1-3 jolts)
            if 1 <= adapters[i] - adapters[j] <= 3:
                dp[i] += dp[j]  # Add all ways to reach j to ways to reach i
    return dp[-1]  # Ways to reach the device

def part2(data):
    adapters = parse(data)
    return get_number_of_arrangements(adapters)
