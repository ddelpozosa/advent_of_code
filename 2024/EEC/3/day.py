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

def parseGrid(lines):
    grid = []
    #empty . row for borders
    empty_row = []
    for i in range(0,len(lines[0])+1):
        empty_row.append(0)
    grid.append(empty_row) # first empty row
    for row in lines:
        grid_row = []
        grid_row.append(0) # first empty col
        for item in row.strip():
            if item == '.':
                grid_row.append(0)
            elif item == '#':
                grid_row.append(1)
        grid_row.append(0) # last empty col
        grid.append(grid_row)
    grid.append(empty_row) # last empty row
    return grid

def printGrid(grid):
    for row in grid:
        str_row = ""
        for item in row:
            if item == 0:
                str_row += "."
            else:
                str_row += str(item)
        print(str_row)

def dig(grid):
    change = False
    temp_grid = [row[:] for row in grid]
    for row_i in range(0,len(grid)):
        for col_j in range(0,len(grid[0])):
            if grid[row_i][col_j] != 0:
                diglevel = grid[row_i][col_j]
                if diglevel == grid[row_i+1][col_j] and diglevel == grid[row_i-1][col_j] and diglevel == grid[row_i][col_j-1] and diglevel == grid[row_i][col_j+1]:
                    temp_grid[row_i][col_j] = diglevel + 1
                    change = True
    return change, temp_grid

def dig_advanced(grid):
    change = False
    temp_grid = [row[:] for row in grid]
    for row_i in range(0,len(grid)):
        for col_j in range(0,len(grid[0])):
            if grid[row_i][col_j] != 0:
                diglevel = grid[row_i][col_j]
                if diglevel == grid[row_i+1][col_j] and diglevel == grid[row_i-1][col_j] and diglevel == grid[row_i][col_j-1] and diglevel == grid[row_i][col_j+1]:
                    if diglevel == grid[row_i+1][col_j+1] and diglevel == grid[row_i-1][col_j-1] and diglevel == grid[row_i+1][col_j-1] and diglevel == grid[row_i-1][col_j+1]:
                        temp_grid[row_i][col_j] = diglevel + 1
                        change = True
    return change, temp_grid

def countGrid(grid):
    count = 0
    for row in grid:
        for item in row:
            count += item
    return count

#Solution to Part 1
def part1(lines):
    grid = parseGrid(lines)
    if args.test == "true":
        print("Inital parsed grid: ")
        printGrid(grid)
    change = True
    while change:
        change, grid = dig(grid)
        if args.test == "true":
            printGrid(grid)
    count = countGrid(grid)
    print("We can safely remove a total of " + str(count) +" blocks.")
#Solution to Part 2
def part2(lines):
        
    part1(lines)

#Solution to Part 3
def part3(lines):
    grid = parseGrid(lines)
    if args.test == "true":
        print("Inital parsed grid: ")
        printGrid(grid)
        print(" ")
    change = True
    while change:
        change, grid = dig_advanced(grid)
        if args.test == "true":
            printGrid(grid)
    count = countGrid(grid)
    print("We can safely remove a total of " + str(count) +" blocks.")

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