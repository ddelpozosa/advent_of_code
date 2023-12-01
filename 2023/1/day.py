import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "true", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = 1, help= "Problem part to run", type=int)
args = parser.parse_args()

def getLines(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.readlines()
    return lines

#Solution to Part 1
def part1(lines):
    total = 0
    for line in lines:
        firstDigit = ""
        lastDigit = ""
        for char in line:
            if char.isdigit():
                if firstDigit == "":
                    firstDigit = char
                    lastDigit = char
                else:
                    lastDigit = char
        
        lineNumber = firstDigit + lastDigit
        total += int(lineNumber)  

    print("The sum of all of the calibration values is " + str(total))

#Solution to Part 2
def part2(file):
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for i, line in enumerate(lines):
        for key in numbers:
            line = line.replace(key, key+numbers[key]+key)
        lines[i] = line
    part1(lines)

if __name__ == "__main__":
    print(args.test)
    print(args.part)
    if args.test == "true":
        lines = getLines("test.txt")
    else:
        lines = getLines("input.txt")
    if args.part == 1:
        part1(lines)
    elif args.part == 2:
        part2(lines)
    else:
        print("Error: Part number invalid: " + args.part)