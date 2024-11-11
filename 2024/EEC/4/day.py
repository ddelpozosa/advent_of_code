import argparse
import statistics
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

def getNails(lines):
    nails = []
    min = None
    for line in lines:
        nail = int(line.strip())
        nails.append(nail)
        if min == None:
            min = nail
        elif nail < min:
            min = nail
    return nails, min

def getNails3(lines):
    nails = []
    for line in lines:
        nail = int(line.strip())
        nails.append(nail)
    return nails, statistics.median(nails)

def countHits(nails,min):
    count = 0
    for nail in nails:
        count += (nail-min)
    return count

def countHits3(nails,mean):
    count = 0
    for nail in nails:
        count += abs(nail-mean)
    return count

#Solution to Part 1
def part1(lines):
    nails, min = getNails(lines)
    count = countHits(nails, min)
    print("We need a minimum of " + str(count) + " hits.")

#Solution to Part 2
def part2(lines):
        
    part1(lines)

#Solution to Part 3
def part3(lines):

    nails, mean = getNails3(lines)
    count = countHits3(nails, mean)
    print("We need a minimum of " + str(count) + " hits.")

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