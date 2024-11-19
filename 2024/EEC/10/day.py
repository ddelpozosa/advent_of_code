import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def printtest(text):
    if args.test == "true":
        print(text)

def getLines(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.readlines()
    return lines

def getGrid(lines):
    grid = []
    for line in lines:
        row = []
        for c in line.strip():
            row += [c]
        grid+=[row]
    return grid

def getColumn(grid, index):
    col = []
    for row in grid:
        col += [row[index]]
    return col

def getDuplicate(col, row):
    for c in col:
        if c in row and c != ".":
            return c

def fillGrid(grid):
    word = ""
    for row in range(2,6):
        for col in range(2,6):
            rune = getDuplicate(getColumn(grid,col), grid[row])
            grid[row][col] = rune
            word += rune
    return word

#Solution to Part 1
def part1(lines):
    grid = getGrid(lines)
    word = fillGrid(grid)
    print("I am the word, and the word is: " + word)

def getBasePower(c):
    return ord(c) - 64

def getPower(word):
    power = 0
    for i in range(0,len(word)):
        power += (i+1) * getBasePower(word[i])
    return power

def getAllGrids(lines):

    grids = []
    for irow in lines[0].strip().split(" "):
        grids += [[irow]]

    for i in range(1,len(lines)):
        if lines[i] == "\n":
           grids += getAllGrids(lines[i+1:])
           return grids
        row = lines[i].strip().split(" ")
        for irow in range(0,len(row)):
            grids[irow] += [row[irow]]
    return grids

#Solution to Part 2
def part2(lines):
    grids = getAllGrids(lines)
    #printtest(grids)
    total = 0
    for gridText in grids:
        grid = getGrid(gridText)
        word = fillGrid(grid)
        power = getPower(word)
        total += power
        printtest("I am the word, and the word's power is: " + str(power))
    print("The total power of all words is: " + str(total))

#Solution to Part 3
def part3(lines):

    print(lines)

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test"+args.part+".txt")
    else:
        lines = getLines("input"+args.part+".txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    elif args.part == "3":
        part3(lines)
    else:
        print("Error: Part number invalid: " + args.part)