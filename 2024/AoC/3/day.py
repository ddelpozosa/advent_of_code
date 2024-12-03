import argparse
from pathlib import Path
import re
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

#Solution to Part 1
def part1(lines):
    total = 0
    for line in lines:
        pattern = re.compile(r"mul\(\d+,\d+\)")
        matches = pattern.findall(line)
        for match in matches:
            pattern2 = re.compile(r"\d+")
            numbers = pattern2.findall(match)
            total += int(numbers[0]) * int(numbers[1])
    print("The total sum of valid multiplications is: " + str(total))

#Solution to Part 2
def part2(lines):
    total = 0
    do = True
    for line in lines:
        pattern = re.compile(r"mul\(\d+,\d+\)|don't\(\)|do\(\)")
        matches = pattern.findall(line)
        printtest(matches)
        for match in matches:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            elif do == True:
                pattern2 = re.compile(r"\d+")
                numbers = pattern2.findall(match)
                total += int(numbers[0]) * int(numbers[1])
        
    print("The total sum of valid multiplications is: " + str(total))

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test"+args.part+".txt")
    else:
        lines = getLines("input"+args.part+".txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    else:
        print("Error: Part number invalid: " + args.part)