import argparse
from pathlib import Path
from math import gcd
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

def parse(lines):
    instructions = []
    for instruction in lines[0].strip().replace("L","0").replace("R","1"):
        instructions.append(int(instruction))
    maze = {}
    for room in lines[2:]:
        dup = (room[7:10],room[12:15])
        maze[room[0:3]] = dup
    return instructions, maze

def navigate(instructions, maze):
    moves = 0
    currentLocation = "AAA"
    end = False
    while end == False:
        for instruction in instructions:
            currentLocation = maze[currentLocation][instruction]
            moves += 1
            if currentLocation == "ZZZ":
                end = True
                break
    return moves

def locationsEndingWith(letter, maze):
    rooms = []
    for room in maze:
        if room[2] == letter:
            rooms.append(room)
    return rooms

def navigateGhost(instructions, maze, start):
    moves = 0
    currentLocation = start
    end = False
    while end == False:
        for instruction in instructions:
            currentLocation = maze[currentLocation][instruction]
            moves += 1
            if currentLocation[2] == "Z":
                print(start + " reached " + currentLocation + " after " + str(moves) + " moves!")
                end = True
                break
    return moves

def navigate2(instructions,maze):
    startLocations = locationsEndingWith("A",maze)
    totalMoves = []
    print("Start locations: " + str(startLocations))
    for location in startLocations:
        moves = navigateGhost(instructions,maze, location)
        totalMoves.append(moves)
        print("It took " + str(moves) + " moves to reach Z from location: " + location)
    return totalMoves


#Solution to Part 1
def part1(lines):
    instructions, maze = parse(lines)
    printtest(instructions)
    printtest(maze)
    moves = navigate(instructions, maze)
    print("It takes " + str(moves) + " number of moves to navigate the maze.")

#Solution to Part 2
def part2(lines):
    instructions, maze = parse(lines)
    moves = navigate2(instructions, maze)
    lcm = 1
    for i in moves:
        lcm = lcm*i//gcd(lcm, i)
    print("It takes " + str(lcm) + " number of moves to navigate the maze.")

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