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
    rows = []
    for line in lines:
        row = []
        for number in line.strip().split(" "):
            row.append(int(number))
        rows.append(row)

    return rows

def expandRow(row):
    subRows = []
    subRows.append(row)
    while subRows[-1][-1] != 0:
        subRow = []
        for i in range(1,len(row)):
            subRow.append(row[i] - row[i-1])
        subRows.append(subRow)
        row = subRow
    return subRows

def extrapolateRow(subRows):
    for i in range(len(subRows)-2,-1,-1):
        subRows[i].append(subRows[i][-1] + subRows[i+1][-1])
        printtest(subRows[i])
    return subRows[0][-1]

def extrapolateRowBack(subRows):
    for i in range(len(subRows)-2,-1,-1):
        subRows[i].insert(0,subRows[i][0] - subRows[i+1][0])
        printtest(subRows[i])
    return subRows[0][0]

#Solution to Part 1
def part1(lines):
    rows = parse(lines)
    total = 0
    for row in rows:
        expandedRows = expandRow(row)
        printtest(expandedRows)
        extrapolation = extrapolateRow(expandedRows)
        total += extrapolation
    print("The total of extrapolated values is: " + str(total))

#Solution to Part 2
def part2(lines):
    rows = parse(lines)
    total = 0
    for row in rows:
        expandedRows = expandRow(row)
        printtest(expandedRows)
        extrapolation = extrapolateRowBack(expandedRows)
        total += extrapolation
    print("The total of extrapolated values back in time is: " + str(total))

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