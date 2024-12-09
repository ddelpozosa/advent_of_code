import argparse
from pathlib import Path
from itertools import combinations
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
    lines = [line.strip() for line in f.readlines()]
    return lines

def get_limits(lines):
    return len(lines[0]),len(lines)

def get_antennas(lines):
    antennas = {}
    max_x,max_y = get_limits(lines)
    for x in range(0,max_x):
        for y in range(0,max_y):
            if lines[y][x] != ".":
                if lines[y][x] in antennas:
                    antennas[lines[y][x]] += [(x,y)]
                else:
                    antennas[lines[y][x]] = [(x,y)]
    return antennas

def get_antinodes(a1,a2):
    
    delta_x = a2[0] - a1[0]
    delta_y = a2[1] - a1[1]
    antinodes = []
    antinodes += [(a1[0] - delta_x, a1[1] - delta_y)]
    antinodes += [(a2[0] + delta_x, a2[1] + delta_y)]
    #print(f"the antinodes of {a1} and {a2} are: {antinodes}")
    return antinodes

def print_result(antinodes, lines):
    max_x,max_y = get_limits(lines)
    for y in range(0,max_y):
        row = ""
        for x in range(0,max_x):
            if (x,y) in antinodes:
                row += "#"
            else:
                row += lines[y][x]
        print(row)

#Solution to Part 1
def part_1(lines):
    max_x, max_y = get_limits(lines)
    antennas = get_antennas(lines)
    antinodes = set()
    for antenna in antennas:
        pairs = list(combinations(antennas[antenna], 2))
        for pair in pairs:
            temp = get_antinodes(pair[0],pair[1])
            for a in temp:
                if a[0] >= 0 and a[0] < max_x and a[1] >= 0 and a[1] < max_y:
                    antinodes.add(a)
    #print_result(antinodes,lines)
    print(f'There are {len(antinodes)} distinct locations')

def get_antinodes_2(a1,a2,max_x,max_y):
    
    delta_x = a2[0] - a1[0]
    delta_y = a2[1] - a1[1]
    antinodes = []
    mode = 0
    index = 0
    while mode<2:
        a = (a1[0] - delta_x*index, a1[1] - delta_y*index)
        if mode == 1:
            a = (a1[0] + delta_x*index, a1[1] + delta_y*index)
        if a[0] >= 0 and a[0] < max_x and a[1] >= 0 and a[1] < max_y:
            antinodes += [a]
            index += 1
        else:
            mode +=1
            index = 0

    #print(f"the antinodes of {a1} and {a2} are: {antinodes}")
    return antinodes
#Solution to Part 2
def part_2(lines):
    max_x, max_y = get_limits(lines)
    antennas = get_antennas(lines)
    antinodes = set()
    for antenna in antennas:
        pairs = list(combinations(antennas[antenna], 2))
        for pair in pairs:
            temp = get_antinodes_2(pair[0],pair[1],max_x,max_y)
            for a in temp:
                antinodes.add(a)
    #print_result(antinodes,lines)
    print(f'There are {len(antinodes)} distinct locations')

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