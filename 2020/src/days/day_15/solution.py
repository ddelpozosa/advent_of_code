from lib import *
from collections import defaultdict

TESTS = [
    {"input": "input_test_1.txt", "part1": 436, "part2": None},
    {"input": "input_test_2.txt", "part1": 10, "part2": None}
]

def parse(data):
    lines = parse_lines(data)
    return list(map(int,lines[0].split(',')))

def speak_numbers(numbers, until):
    spoken_numbers = {}  # number -> (last_turn, prev_turn)
    
    # Initialize with starting numbers
    for turn, number in enumerate(numbers, 1):
        spoken_numbers[number] = (turn, None)  # First time, no previous
    
    last_spoken = numbers[-1]
    
    # Play until the target turn
    for turn in range(len(numbers) + 1, until + 1):
        last_turn, prev_turn = spoken_numbers[last_spoken]
        
        if prev_turn is None:
            # Last spoken was NEW (first time), speak 0
            next_spoken = 0
        else:
            # Otherwise, speak the difference
            next_spoken = last_turn - prev_turn
        
        # Update: record when next_spoken was just spoken
        if next_spoken in spoken_numbers:
            # It was spoken before, shift the turns
            old_last_turn, _ = spoken_numbers[next_spoken]
            spoken_numbers[next_spoken] = (turn, old_last_turn)
        else:
            # First time being spoken
            spoken_numbers[next_spoken] = (turn, None)
        
        last_spoken = next_spoken
    
    return last_spoken

# defaultdict to avoid "number in spoken" checks
# goes from 45s to 6s in part 2
def speak_numbers_optimized(numbers, until):
    last_turn = defaultdict(int)
    prev_turn = defaultdict(int)
    
    for turn, number in enumerate(numbers, 1):
        last_turn[number] = turn
    
    current = numbers[-1]
    
    for turn in range(len(numbers) + 1, until + 1):
        prev = prev_turn[current]
        if prev:
            next_num = last_turn[current] - prev
        else:
            next_num = 0
        
        prev_turn[next_num] = last_turn[next_num]
        last_turn[next_num] = turn
        
        current = next_num
    
    return current

def part1(data):
    numbers = parse(data)
    return speak_numbers(numbers, 2020)

def part2(data):
    numbers = parse(data)
    return speak_numbers_optimized(numbers, 30000000)
