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

class Number:
  def __init__(self, value, x1, x2, y):
    self.value = value
    self.x1 = x1
    self.x2 = x2
    self.y = y
    self.part = False
  def __str__(self):
    return f"Value: {self.value} -- x1={self.x1}, x2={self.x2}, y={self.y}"

def getNumbers(lines):
    totalNumbers = []
    for y, line in enumerate(lines):
        currentNumber = Number("",-1,-1,y)
        for x, char in enumerate(line.strip()):
            if char.isdigit():
                #we are working with a number, so add it to total but check if it is the first digit first
                if currentNumber.value == "":
                    currentNumber.x1 = x
                currentNumber.value += char
                #if end of line, number finished and append, append to list and reset number
                if x + 1 == len(line):
                    currentNumber.x2 = x
                    totalNumbers.append(currentNumber)
                    currentNumber = Number("",-1,-1,y)   
                #if next is not a digit, number finished, append to list and reset number
                elif(line[x+1].isdigit() == False):
                    currentNumber.x2 = x
                    totalNumbers.append(currentNumber)
                    currentNumber = Number("",-1,-1,y)   
                
    printtest("List of numbers:")         
    for number in totalNumbers:
        printtest(number)
    return totalNumbers
                

#Solution to Part 1
def part1(lines):

    totalNumbers = getNumbers(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char.isdigit() == False and char != ".":
                printtest(char + " is located at " + str(x) + "," + str(y))
                for number in totalNumbers:
                    if abs(number.y - y) <= 1 and ((abs(number.x1 - x) <= 1 or abs(number.x2 - x) <= 1)):
                        number.part = True
                        printtest(str(number) + ") is adjacent to " + char)
    sumParts = 0
    for number in totalNumbers:
        if number.part == True:
            printtest(number.value + " is part number")
            sumParts += int(number.value)
    print("The sum of all parts is: " + str(sumParts))

#Solution to Part 2
def part2(lines):
    
    totalNumbers = getNumbers(lines)
    totalGearRatio = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == "*":
                printtest(char + " is located at " + str(x) + "," + str(y))
                adjacent = 0
                ratio = 1
                for number in totalNumbers:
                    if abs(number.y - y) <= 1 and ((abs(number.x1 - x) <= 1 or abs(number.x2 - x) <= 1)):
                        adjacent += 1
                        ratio *= int(number.value)
                        printtest(str(number) + ") is adjacent to " + char)
                if adjacent == 2:
                    printtest("this is a gear because it has 2 adjacent numbers! Gear ratio: " + str(ratio))
                    totalGearRatio += ratio

    print("The sum of all gear ratios is: " + str(totalGearRatio))

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