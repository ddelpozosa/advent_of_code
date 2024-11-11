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
    for row in lines:
        grid_row = []
        for item in row.split(" "):
            grid_row.append(int(item))
        grid.append(grid_row)
    return list(map(list, zip(*grid)))

def getShout(grid):
    shout = ""
    for col in grid:
        shout += str(col[0])
    return shout

def round(grid, round_i):
    cols = len(grid)
    col_1 = round_i % cols
    col_2 = (round_i + 1) % cols
    temp_grid = [row[:] for row in grid]
    clapper = temp_grid[col_1][0]
    ###add clapper to the top of right column
    temp_grid[col_2].insert(0,clapper)
    ###remove clapper from the top of left column
    temp_grid[col_1] = temp_grid[col_1][1:]
    ###DANCE!
    q = clapper // (len(temp_grid[col_2]))
    if q % 2 == 0: ## left turn
        if clapper < len(temp_grid[col_2]):
            temp_grid[col_2].insert(clapper,clapper)
        else:
            temp_grid[col_2].insert(clapper % (len(temp_grid[col_2])),clapper)
    else: ## right turn
        temp_grid[col_2].insert((len(temp_grid[col_2])) - (clapper % (len(temp_grid[col_2]))),clapper)
    ###remove clapper from the top of right column
    temp_grid[col_2] = temp_grid[col_2][1:]
    return temp_grid, getShout(temp_grid)

#Solution to Part 1
def part1(lines):
    grid = parseGrid(lines)
    rounds = 0
    while rounds < 10:
        grid,shout = round(grid,rounds)
        if args.test == "true":
            print("Round " + str(rounds+1) + " shouts: " + shout)
            if rounds == 2 or rounds ==3:
                print(grid)
        rounds+=1
    print("Round " + str(rounds) + " shouts: " + shout)
#Solution to Part 2
def part2(lines):
    grid = parseGrid(lines)
    shouts = {}
    stop = False
    rounds = 0
    while not stop:
        grid,shout = round(grid,rounds)
        if shout not in shouts:
            shouts[shout] = 1
        else:
            shouts[shout] += 1
        if shouts[shout] == 2024:
            stop = True
        rounds+=1
    print("Number " + str(shout) + " has been sang 2024 times in round " + str(rounds) + ". Final answer: " + str(int(shout)*rounds))
#Solution to Part 3
def part3(lines):
    grid = parseGrid(lines)
    shouts = []
    stop = False
    rounds = 0
    max = 0
    while stop == False:
        grid,shout = round(grid,rounds)
        if shout not in shouts:
            shouts.append(shout)
        if int(shout) > max:
            max = int(shout)
            print("Round: " + str(rounds) + " New max shout: " + str(max))
        if rounds % 25000 == 0:
            print("Round: " + str(rounds) + "... Max: " + str(max))
        rounds+=1
    
    print("Max shout is: " + str(max(shouts)))

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