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
    races = []
    time = " ".join(lines[0].split(":")[1].split()).strip().split(" ")
    distance = " ".join(lines[1].split(":")[1].split()).strip().split(" ")
    for i, t in enumerate(time):
        races.append((int(time[i]),int(distance[i])))
    return races

def parse2(lines):
    races = []
    time = "".join(lines[0].split(":")[1].split()).strip().split(" ")
    distance = "".join(lines[1].split(":")[1].split()).strip().split(" ")
    for i, t in enumerate(time):
        races.append((int(time[i]),int(distance[i])))
    return races

def getWins(race):
    win = 0
    time = race[0]
    recordDistance = race[1]
    for timeToPress in range(0,time+1,1):
        distance = timeToPress * (time - timeToPress)
        if distance > recordDistance:
            win+=1
    return win

#Solution to Part 1
def part1(lines):
    races = parse(lines)
    total = 1
    for i, race in enumerate(races):
        win = getWins(race)
        total*=win
        printtest("Race " + str(i+1) + " has " + str(win) + " possible ways to win.")
    print("The solution is: " + str(total))

#Solution to Part 2
def part2(lines):
    races = parse2(lines)
    total = 1
    for i, race in enumerate(races):
        win = getWins(race)
        total*=win
        printtest("Race " + str(i+1) + " has " + str(win) + " possible ways to win.")
    print("The solution is: " + str(total))

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