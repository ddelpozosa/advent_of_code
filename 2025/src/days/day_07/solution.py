from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 21, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 40}
]

def parse(data):
    lines = parse_lines(data)
    start = ()
    splitters = set()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            char = lines[y][x]
            if char == '^':
                splitters.add((x,y))
            elif char == 'S':
                start = (x,y)
    max_coords = (len(lines[0]), len(lines)) #(max_x, max_y)
    return start, max_coords, splitters

def get_visual_representation(beams,max_coords,splitters):
    s = ""
    for y in range (0, max_coords[1]):
        for x in range(0, max_coords[0]):
            if (x,y) in splitters:
                s += "^"
            elif (x,y) in beams:
                s += "|"
            else:
                s += "."
        s += "\n"
    return s

def split_tachyons(start, max_coords, splitters):
    beams = {start}
    splitted_beams = set()
    split_count = 0

    def next_beam(target_x, target_y):
        nonlocal split_count  # Allow modification of outer variable

        # Exit condition
        if (target_x, target_y) in beams or target_y >= max_coords[1] or target_x < 0 or target_x >= max_coords[0]:
            return 
        
        beams.add((target_x,target_y))

        # check sides and next beans right and left where possible
        if(target_x, target_y) in splitters:
            # Split left
            split_count += 1
            if target_x - 1 >= 0:
                splitted_beams.add((target_x - 1, target_y))
                next_beam(target_x - 1, target_y)
            
            # Split right
            if target_x + 1 < max_coords[0]:
                splitted_beams.add((target_x + 1, target_y))
                next_beam(target_x + 1, target_y)
        else:
            # Continue down
            next_beam(target_x, target_y + 1)

    next_beam(start[0], start[1] + 1)
    debug("Final state: ")
    debug(get_visual_representation(beams,max_coords,splitters))
    return split_count  # Return count of unique splitted beam positions

# Tracking all possible paths and storing them is exponential, causes timeout
# Tracking how many points reach each spot is linear (same as the split_tachyons() function)
def count_timelines(start, max_coords, splitters):
    # For each position, track how many ways we can reach it
    ways_to_reach = {(start[0], start[1] + 1): 1}
    
    # Process row by row from top to bottom
    for y in range(start[1] + 1, max_coords[1]):
        next_ways = {}
        
        for (x, curr_y), count in ways_to_reach.items():
            if curr_y != y:  # Skip if not current row
                continue
                
            if (x, y) in splitters:
                # Split: distribute count to left and right (next row)
                if x - 1 >= 0:
                    # Using .get(key,default) as a safe lookup in case key (cell) still not present
                    next_ways[(x - 1, y + 1)] = next_ways.get((x - 1, y + 1), 0) + count
                if x + 1 < max_coords[0]:
                    next_ways[(x + 1, y + 1)] = next_ways.get((x + 1, y + 1), 0) + count
            else:
                # Continue down: pass count to same x, next row
                next_ways[(x, y + 1)] = next_ways.get((x, y + 1), 0) + count
        
        ways_to_reach.update(next_ways)
    
    # Sum all the ways to reach the bottom row
    total_timelines = 0
    for (x, y), count in ways_to_reach.items():
        if y >= max_coords[1]:  # Reached bottom
            total_timelines += count
    
    return total_timelines

def part1(data):
    start, max_coords, splitters = parse(data)
    splitted_tachyons = split_tachyons(start, max_coords, splitters)
    return splitted_tachyons

def part2(data):
    start, max_coords, splitters = parse(data)
    timelines = count_timelines(start, max_coords, splitters)
    return timelines
