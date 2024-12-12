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
    lines = [list(c) for c in f.read().split("\n")]
    return lines

def get_limits(lines):
    return len(lines[0]),len(lines)

def get_region(start, visited,reg_visit, map):
    max_x,max_y = get_limits(map)
    visited.add(start)
    reg_visit.add(start)
    letter = map[start[1]][start[0]]
    area = 1
    perimeter = 0
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for dir in dirs:
        next = (start[0] + dir[0],start[1] + dir[1])
        if next not in reg_visit:
            if next[0]>=0 and next[0] < max_x and next[1]>=0 and next[1] < max_y:
                if map[next[1]][next[0]] == letter:
                    na,np = get_region(next,visited,reg_visit,map)
                    area += na
                    perimeter += np
                else:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter

#Solution to Part 1
def part_1(map):
    max_x,max_y = get_limits(map)
    visited = set()
    price = 0
    for y in range(0,max_y):
        for x in range(0,max_x):
            if(x,y) not in visited:
                l = map[y][x]
                start = (x,y)
                reg_visit = set()
                area, perimeter = get_region(start,visited,reg_visit,map)
                #print(f"Region {l} has an area of {area} and a perimeter of {perimeter}")
                price += area * perimeter
    print(f"The total price is: {price}")

def get_corners(area):
    corners = 0
    for cell in area:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        #external corners
        for dir in dirs:
            cell_1 = (cell[0] + dir[0], cell[1] + dir[1])
            cell_2 = (cell[0] + dir[1], cell[1] - dir[0])
            if cell_1 not in area and cell_2 not in area:
                corners += 1
                #print(f"{cell} is ext corner")
        #internal corners
        for dir in dirs:
            cell_1 = (cell[0] + dir[0], cell[1] + dir[1])
            cell_2 = (cell[0] + dir[1], cell[1] - dir[0])
            if cell_1 in area and cell_2 in area:
                cell_3 = (cell[0] + dir[0] + dir[1], cell[1] + dir[1] - dir[0])
                if cell_3 not in area:
                    corners += 1
                    #print(f"{cell} is in corner")
    #print(f"there are {corners}  corners")
    return corners

#Solution to Part 2
def part_2(map):
    max_x,max_y = get_limits(map)
    visited = set()
    price = 0
    for y in range(0,max_y):
        for x in range(0,max_x):
            if(x,y) not in visited:
                l = map[y][x]
                start = (x,y)
                reg_visit = set()
                area, perimiter = get_region(start,visited,reg_visit,map)
                corners = get_corners(reg_visit)
                #print(f"Region {l} has {corners} corners")
                price += area * corners
    print(f"The total price is: {price}")

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