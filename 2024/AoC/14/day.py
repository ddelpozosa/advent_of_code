import argparse
import re
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
    lines = f.read().split("\n")
    robots = []
    pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

    # Match and extract
    for line in lines:
        match = re.search(pattern, line)
        p = (int(match.group(1)),int(match.group(2)))
        v = (int(match.group(3)),int(match.group(4)))
        robots += [[p,v]]
    return robots

def get_limits(robots):
    max_x, max_y = -1,-1
    for robot in robots:
        p = robot[0]
        if p[0] > max_x:
            max_x = p[0]
        if p[1] > max_y:
            max_y = p[1]
    return max_x+1, max_y+1

def get_coord(p,v,seconds,max_x,max_y):
    end = (p[0] + seconds*v[0], p[1] + seconds*v[1])
    end = (end[0] % max_x, end[1] % max_y)
    return end

def print_grid(coords,max_x,max_y):
    for y in range(max_y):
        row = ""
        for x in range(max_x):
            if (x,y) in coords:
                row += str(coords[(x,y)])
            else:
                row += "."
        print(row)
    print("")

def add_to_dict(dict,item):
    if item not in dict:
        dict[item] = 1
    else:
        dict[item] += 1

def get_safety_factor(coords,max_x,max_y):
    safety_factor = 0
    mid_x_1, mid_x_2 = max_x // 2, max_x // 2
    mid_y_1, mid_y_2 = max_y // 2, max_y // 2
    if max_x % 2 != 0:
        mid_x_1-=1
        mid_x_2+=1
    if max_y % 2 != 0:
        mid_y_1-=1
        mid_y_2+=1
    
    ## top left
    q1 = 0
    print(f"Quadrant 1: {(0,mid_x_1)} - {(0,mid_y_1)}")
    for coord in coords:
        if coord[0] >= 0 and coord[0]<= mid_x_1 and coord[1] >= 0 and coord[1] <= mid_y_1:
            q1 += coords[coord]
    ## top right
    q2 = 0
    print(f"Quadrant 2: {(mid_x_2,max_x-1)} - {(0,mid_y_1)}")
    for coord in coords:
        if coord[0] >= mid_x_2 and coord[0]<= max_x-1 and coord[1] >= 0 and coord[1] <= mid_y_1:
            q2 += coords[coord]
    ## bot left
    q3 = 0
    print(f"Quadrant 3: {(0,mid_x_1)} - {(mid_y_2,max_y-1)}")
    for coord in coords:
        if coord[0] >= 0 and coord[0]<= mid_x_1 and coord[1] >= mid_y_2 and coord[1] <= max_y-1:
            q3 += coords[coord]
    ## bot right
    q4 = 0
    print(f"Quadrant 4: {(mid_x_2,max_x-1)} - {(mid_y_2,max_y-1)}")
    for coord in coords:
        if coord[0] >= mid_x_2 and coord[0]<= max_x-1 and coord[1] >= mid_y_2 and coord[1] <= max_y-1:
            q4 += coords[coord]
    return q1 * q2 * q3 * q4
#Solution to Part 1
def part_1(robots):
    coords = {}
    s = 100
    max_x, max_y = get_limits(robots)
    for robot in robots:
        p,v = robot[0], robot[1]
        coord = get_coord(p,v,s,max_x,max_y)
        print(f"After {s} seconds: {coord}")
        add_to_dict(coords,coord)
    print_grid(coords,max_x,max_y)

    sf = get_safety_factor(coords,max_x,max_y)
    print(f"The total safety factor after {s} seconds is: {sf}")

def get_region(start, visited,reg_visit, coords,max_x, max_y):
    visited.add(start)
    reg_visit.add(start)
    area = 1
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for dir in dirs:
        next = (start[0] + dir[0],start[1] + dir[1])
        if next not in reg_visit:
            if next[0]>=0 and next[0] < max_x and next[1]>=0 and next[1] < max_y:
                if next in coords:
                    area += get_region(next,visited,reg_visit,coords,max_x,max_y)
    return area

#Solution to Part 2
def part_2(robots):
    max_x, max_y = get_limits(robots)
    threshold = 40 #arbitrary, if a large number of robots are adjacent to one another I assume it is not a coincidence and might be a tree
    end = False
    for s in range(1000000):
        if end == False:
            visited = set()
            coords = {}
            for robot in robots:
                p,v = robot[0], robot[1]
                coord = get_coord(p,v,s,max_x,max_y)
                #print(f"After {s} seconds: {coord}")
                add_to_dict(coords,coord)

            for coord in coords:
                if coord not in visited:
                    reg_visit = set()
                    area = get_region(coord,visited,reg_visit,coords,max_x,max_y)
                    if area > threshold: 
                        print(f"Found area of size: {area} after {s} seconds")
                        print_grid(coords,max_x,max_y)
                        end = True 
                    
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