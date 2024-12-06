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
    lab = [list(line) for line in f.read().split("\n")] ### this return an array which can be accessed as lab[y][x]
    return lab

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def turn_right(self):
        self.x, self.y = -self.y, self.x 
    def __str__(self):
        return f"({self.x}, {self.y})"
    def get_tuple(self):
        return (self.x,self.y)
    
def get_start(lab):
    for x in range(0, len(lab[0])):
        for y in range(0, len(lab)):
            if lab[y][x] == '^':
                return (x,y)

def move(cur_coord, direction, lab):
    min_x,min_y,max_x,max_y = 0,0,len(lab[0])-1,len(lab)-1
    cur_x,cur_y = cur_coord[0],cur_coord[1]
    tries = 0
    while tries <= 4:
        next_x,next_y = cur_x + direction.x, cur_y + direction.y
        #check if next position is possible
        #first, check if in-bounds
        if next_x >= min_x and next_x <= max_x and next_y >= min_y and next_y <= max_y:
            #then, check next item is passable
            if lab[next_y][next_x] != "#":
                return (next_x,next_y)
        else:
            return -1 # if out of bounds, return -1 immediatly
        #if not possible to move, turn right and try again:
        direction.turn_right()
        tries +=1

    return -1 #no more moves are possible

def print_lab(lab, visited):
    for coord in visited:
        lab[coord[1]][coord[0]] = "X"
    for line in lab:
        row = ""
        for c in line:
            row +=c
        print(row)

#Solution to Part 1
def part_1(lab):
    cur_coord = get_start(lab)
    direction = Vector(0,-1) #default vector is northbound (negative y is up)
    visited = set()
    while cur_coord != -1:
        visited.add(cur_coord)
        cur_coord = move(cur_coord,direction,lab)
    print(f"We have visited a total of {len(visited)} distinct coords.")
    if args.test == "true":
        print_lab(lab,visited)

def get_possible_Os(lab):
    Os = []
    for x in range(0, len(lab[0])):
        for y in range(0, len(lab)):
            if lab[y][x] != "#" and lab[y][x] != "^":
                Os += [(x,y)]
    return Os

def is_loop(cur_coord, direction, visited):
    if (cur_coord, (direction.x,direction.y)) in visited:
        return True
    return False

#Solution to Part 2
def part_2(lab):
    start = get_start(lab)
    Os = get_possible_Os(lab)   
    valid_os = set()
    #Os = [(3,4)]
    n = 0
    for o in Os:
        n+=1
        direction = Vector(0,-1) #default vector is northbound (negative y is up)

        lab[o[1]][o[0]] = "#"
        cur_coord = start
        visited = set()
        print(f"O {n}/{len(Os)}")
        steps = 0
        while cur_coord != -1:
            visited.add((cur_coord,(direction.x,direction.y)))
            steps += 1
            cur_coord = move(cur_coord,direction,lab)
            if cur_coord != -1 and is_loop(cur_coord,direction,visited):
                valid_os.add(o)
                cur_coord = -1
        #print_lab(lab,visited)
        lab[o[1]][o[0]] = "."
    print(f"There is a total of {len(valid_os)} places we can add an obstacle to create a loop.")

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