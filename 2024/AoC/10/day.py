import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def print_test(text):
    if args.test == "true":
        print(text)

def parse_input(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = [[int(c) if c.isdigit() else c for c in line] for line in f.read().split("\n")]
    return lines

def get_limits(lines):
    return len(lines[0]),len(lines)

def find_trails(map,trailhead, max_x, max_y):
    paths = set()
    x,y = trailhead[0], trailhead[1]
    cur_value = map[y][x]
    if cur_value == 9:
        #print(f"reached the end: {(x,y)}")
        return {(x, y)}
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    for dir in dirs:
        new_x = x + dir[0]
        new_y = y + dir[1]      
        if new_x >= 0 and new_x < max_x and new_y >= 0 and new_y < max_y:
            if map[new_y][new_x] != "." and map[new_y][new_x] - cur_value == 1: #if the new place is exactly 1 point higher, then its part of the path
                #print(f"going to: {(new_x,new_y)}")
                sub_paths = find_trails(map, (new_x, new_y), max_x, max_y)
                paths.update(sub_paths)
    return paths

def find_trailheads(map):
    trailheads = []
    max_x,max_y = get_limits(map)
    for x in range(max_x):
        for y in range(max_y):
            if map[y][x] == 0:
                trailheads += [(x,y)]
    return trailheads

def find_trails_2(map,trailhead, max_x, max_y):
    paths = 0
    x,y = trailhead[0], trailhead[1]
    cur_value = map[y][x]
    if cur_value == 9:
        #print(f"reached the end: {(x,y)}")
        return 1
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    for dir in dirs:
        new_x = x + dir[0]
        new_y = y + dir[1]      
        if new_x >= 0 and new_x < max_x and new_y >= 0 and new_y < max_y:
            if map[new_y][new_x] != "." and map[new_y][new_x] - cur_value == 1: #if the new place is exactly 1 point higher, then its part of the path
                #print(f"going to: {(new_x,new_y)}")
                paths += find_trails_2(map, (new_x, new_y), max_x, max_y)
    return paths

#Solution to Part 1
def part_1(map):
    #map[y][x]
    max_x,max_y = get_limits(map)
    trailheads = find_trailheads(map)
    total = 0
    for trailhead in trailheads:
        paths = find_trails(map,trailhead, max_x, max_y)
        total += len(paths)
        #print(f"{trailhead} has a score of: {len(paths)}")
    print(f"The sum of all the scores of all trailheads is: {total}")


#Solution to Part 2
def part_2(map):
    #map[y][x]
    max_x,max_y = get_limits(map)
    trailheads = find_trailheads(map)
    total = 0
    for trailhead in trailheads:
        paths = find_trails_2(map,trailhead, max_x, max_y)
        total += paths
        print(f"{trailhead} has a score of: {paths}")
    print(f"The sum of all the scores of all trailheads is: {total}")

if __name__ == "__main__":
    if args.test == "true":
        lines = parse_input("test"+args.part+".txt")
    else:
        lines = parse_input("input"+args.part+".txt")
    if args.part == "1":
        part_1(lines)
    elif args.part == "2":
        part_2(lines)
    else:
        print("Error: Part number invalid: " + args.part)