import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def printtest(text):
    if args.test == "true":
        print(text)

def parse(lines, expansionFactor):
    empty_columns = []
    empty_rows = []
    for y, line in enumerate(lines):
        if len(line.split(".")) == len(line):
            empty_rows.append(y)
            printtest("Row " + str(y) + " is all empty")
    
    for x in range(0,len(lines[0].strip())):
        empty = True
        for y in range(0,len(lines)):
            if lines[y][x] == "#":
                empty = False
        if empty == True:
            empty_columns.append(x)
            printtest("Column " + str(x) + " is all empty")

    printtest("Empty columns: " + str(empty_columns))
    printtest("Empty rows: " + str(empty_rows))
    galaxies = []

    for x in range(0,len(lines[0].strip())):
        empty = True
        for y in range(0,len(lines)):
            if lines[y][x] == "#":
                gx = x
                gy = y
                for empty_row in empty_rows:
                    if y > empty_row:
                        gy += expansionFactor
                for empty_col in empty_columns:
                    if x > empty_col:
                        gx += expansionFactor
                galaxies.append((gx,gy))

    return galaxies

def getDistance(g1, g2):
    return abs(g1[1] - g2[1]) + abs(g1[0] - g2[0])

def getLines(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.readlines()
    return lines

#Solution to Part 1
def part1(lines):

    galaxies = parse(lines, 1)
    possible_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    printtest("Galaxies: " + str(galaxies))
    printtest("There are " + str(len(possible_pairs)) + " possible pairs")
    total = 0
    for pair in possible_pairs:
        d = getDistance(pair[0],pair[1])
        total += d
        printtest("Distance between pair " + str(pair) + " is " + str(d))
    print("The sum of all minimum lengths is " + str(total))

#Solution to Part 2
def part2(lines):
    galaxies = parse(lines, 999999)
    possible_pairs = [(a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1:]]
    printtest("Galaxies: " + str(galaxies))
    printtest("There are " + str(len(possible_pairs)) + " possible pairs")
    total = 0
    for pair in possible_pairs:
        d = getDistance(pair[0],pair[1])
        total += d
        printtest("Distance between pair " + str(pair) + " is " + str(d))
    print("The sum of all minimum lengths is " + str(total))

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test.txt")
    else:
        lines = getLines("input.txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    else:
        print("Error: Part number invalid: " + args.part)