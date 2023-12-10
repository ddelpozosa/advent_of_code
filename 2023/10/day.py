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

def parse(lines):
    grid = []
    coord = (-1,-1)
    for y, line in enumerate(lines):
        l = []
        for x, char in enumerate(line.strip()):
            if char == "S":
                coord = (x,y)
            if char == "7":
                l.append("Z")
            else:
                l.append(char)
        grid.append(l)
    return grid, coord

def getField(x,y,grid):
    if y >= len(grid) or y < 0:
        return "-1"
    elif x >= len(grid[0]) or x < 0:
        return "-1"
    else:
        return grid[y][x]

def getConnected(x, y, grid):
    connectedCoords = []
    right = getField(x+1,y,grid)
    left = getField(x-1,y,grid)
    bottom = getField(x,y+1,grid)
    top = getField(x,y-1,grid)
    printtest("Field: " + str(grid[y][x]) +" right: " + str(right))
    match grid[y][x]:
        case "S":
            if right == "-" or right == "J" or right == "Z":
                connectedCoords.append((x+1,y))
            if left == "-" or left == "L" or left == "F":
                connectedCoords.append((x-1,y))
            if top == "|"   or top == "Z" or top == "F":
                connectedCoords.append((x,y-1))
            if bottom == "|" or bottom == "L" or bottom == "J":
                connectedCoords.append((x,y+1))
        case "-":
            if right == "-" or right == "J" or right == "Z":
                printtest("Field: " + str(grid[y][x]) +" is connected to the right")
                connectedCoords.append((x+1,y))
            if left == "-" or left == "L" or left == "F":
                connectedCoords.append((x-1,y))
        case "J":
            if left == "-" or left == "L" or left == "F":
                connectedCoords.append((x-1,y))
            if top == "|"   or top == "Z" or top == "F":
                connectedCoords.append((x,y-1))
        case "|":
            if top == "|"   or top == "Z" or top == "F":
                connectedCoords.append((x,y-1))
            if bottom == "|" or bottom == "L" or bottom == "J":
                connectedCoords.append((x,y+1))
        case "L":
            if top == "|"   or top == "Z" or top == "F":
                connectedCoords.append((x,y-1))
            if right == "-" or right == "J" or right == "Z":
                connectedCoords.append((x+1,y))
        case "Z":
            if bottom == "|" or bottom == "L" or bottom == "J":
                connectedCoords.append((x,y+1))
            if left == "-" or left == "L" or left == "F":
                connectedCoords.append((x-1,y))
        case "F":
            if bottom == "|" or bottom == "L" or bottom == "J":
                connectedCoords.append((x,y+1))
            if right == "-" or right == "J" or right == "Z":
                connectedCoords.append((x+1,y))
    printtest("Field: " + str(grid[y][x]) + " -- connected coords: " + str(connectedCoords))
    return connectedCoords
        
def printGrid(grid):
    for line in grid:
        s = ""
        for char in line:
            s+=str(char)
        printtest(s)

def replaceWithDistance(x,y, grid, ):
    connectedCoords = getConnected(x,y,grid)
    distance = 0
    while len(connectedCoords)>0:
        nextConn = []
        distance += 1
        for coord in connectedCoords:
            nextConn += getConnected(coord[0],coord[1],grid)
            grid[coord[1]][coord[0]] = distance
        printtest("Next conns: " + str(nextConn))
        connectedCoords = nextConn
    return grid, distance

def replaceWithInLoop(orGrid, solGrid):
    countI = 0
    for y in range(0,len(solGrid)):
        count = 0
        for x in range(0, len(solGrid[0])):
            if str(solGrid[y][x]).isdigit() or str(solGrid[y][x]) == "S":               
                if orGrid[y][x] == "F" or orGrid[y][x] == "Z" or orGrid[y][x] == "|":
                    count +=1
            else:
                if count%2==0:
                    orGrid[y][x] = "0"
                else:
                    orGrid[y][x] = "I"
                    countI += 1
    return orGrid, countI

#Solution to Part 1
def part1(lines):

    grid, coord = parse(lines)
    grid, distance = replaceWithDistance(coord[0],coord[1],grid)
    printGrid(grid)
    print("The furthest distance to S is: " + str(distance))
    

#Solution to Part 2
def part2(lines):
    grid, coord = parse(lines)
    grid, distance = replaceWithDistance(coord[0],coord[1],grid)
    gridOrg, coord = parse(lines)
    printGrid(grid)
    loopGrid, countI = replaceWithInLoop(gridOrg, grid)
    printGrid(loopGrid)
    print("There are " + str(countI) + " fields inside the loop!")

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