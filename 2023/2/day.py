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

def possibleGame(cubes):
    cubesTotal = {
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }
    for key in cubesTotal:
        if cubes[key] > cubesTotal[key]:
            return False
    return True

#Solution to Part 1
def part1(lines):
    IDsum = 0
    for line in lines:
        gameNumber = int(line.split(": ")[0].split(" ")[1])
        game = line.split(": ")[1]
        possible = True
        for set in game.split("; "):
            cubesSet = {"red" : 0,"green" : 0,"blue" : 0}
            for ball in set.split(", "):
                number = int(ball.split(" ")[0])
                color = ball.split(" ")[1].strip()
                cubesSet[color] += number
            if possibleGame(cubesSet):
                printtest("A set of game " + str(gameNumber) + " is possible!")
            else:
                printtest("A set of game " + str(gameNumber) + " is not possible!")
                possible = False
        if(possible):
            printtest("Game " + str(gameNumber) + " is possible!")
            IDsum += gameNumber
        else:
            printtest("Game " + str(gameNumber) + " is not possible!")
    print("The Sum of IDs of all possible games is: " + str(IDsum))

#Solution to Part 2
def part2(lines):
    powerSum = 0
    for line in lines:
        gameNumber = int(line.split(": ")[0].split(" ")[1])
        game = line.split(": ")[1]
        possible = True
        cubesGame = {"red" : 0,"green" : 0,"blue" : 0}
        for set in game.split("; "):
            cubesSet = {"red" : 0,"green" : 0,"blue" : 0}
            for ball in set.split(", "):
                number = int(ball.split(" ")[0])
                color = ball.split(" ")[1].strip()
                cubesSet[color] += number
            for color in cubesSet:
                if cubesSet[color] > cubesGame[color]:
                    cubesGame[color] = cubesSet[color]
        power = cubesGame["red"] * cubesGame["green"] * cubesGame["blue"]
        powerSum += power
        printtest("Game " + str(gameNumber) + " powers: " + str(cubesGame) + " with a power of " + str(power))

    print("The sum of powers of all possible games is: " + str(powerSum))   

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