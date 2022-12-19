from pathlib import Path
import ast

p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

rocks = set()
sand_source = (500,0)
sand_rest = set()

def print_simulation():
    for y in range(0,12):
        line = ""
        for x in range(490,510):
            if (x,y) in rocks:
                line+="#"
            elif (x,y)==sand_source:
                line+="+"
            elif (x,y) in sand_rest:
                line+="o"
            else:
                line+="."
        print(line)

def parse_input(input):
    for line in input:
        prev = (-1,-1)
        for item in line.strip().split(" -> "):
            current = (int(item.split(",")[0]),int(item.split(",")[1]))
            if prev == (-1,-1):
                prev = current
            else:
                xs = sorted([prev[0],current[0]])
                ys = sorted([prev[1],current[1]])
                for x in range(xs[0],xs[1]+1):
                    for y in range(ys[0],ys[1]+1):
                        rocks.add((x,y))
                prev = current
            #print(item)

def get_max_y():
    max = -1
    for rock in rocks:
        if max == -1:
            max = rock[1]
        elif max <  rock[1]:
            max = rock[1]
    return max

def add_sand(bottom_y):
    x,y = sand_source
    while y <= bottom_y:
        if (x,y+1) in rocks or (x,y+1) in sand_rest or y+1==bottom_y: ###check if there is a rock below
            if (x-1,y+1) not in rocks and (x-1,y+1) not in sand_rest and y+1!=bottom_y: ###check if there is space bottom left
                x = x-1
            elif (x+1,y+1) not in rocks and (x+1,y+1) not in sand_rest and y+1!=bottom_y: ### check if there is space bottom left
                x = x+1
            else: ###no space anywhere, so sand comes to rest
                sand_rest.add( (x,y) )
                y = bottom_y
        y+=1
        #print(y)

parse_input(lines)

end = 0
bottom_y = get_max_y() + 2
while end<1:
    prev_len = len(sand_rest)
    #print(len(sand_rest))
    add_sand(bottom_y)
    if prev_len == len(sand_rest):
        end+=1
    else:
        end=0

print_simulation()
print(f'Part 1: {len(sand_rest)} come to rest before sand starts flowing into the abyss below')