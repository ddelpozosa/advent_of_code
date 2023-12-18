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
    patterns = []
    pattern = []
    for line in lines:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())
    patterns.append(pattern)
    return patterns

def checkVertical(pattern):
    equalCols = []
    for i in range(len(pattern[0])-1):
        equal = True
        for row in pattern:
            if row[i]!=row[i+1]:
                equal = False
        if equal == True:
            equalCols.append((i,i+1))
            printtest("Column " + str(i) + " is equal to column " + str(i+1))
    for col1, col2 in equalCols:
        colId = col2
        end = False
        while end == False:
            if col1 - 1 >= 0 and col2 + 1 < len(pattern[0]):
                col1-=1 
                col2+=1
                equal = True
                for row in pattern:
                    if row[col1]!=row[col2]:
                        equal = False
                if equal == False:
                    end = True
            else:
                return colId
    return -1

def checkHorizontal(pattern):
    equalRows = []
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            equalRows.append((i,i+1))
            printtest("Row " + str(i) + " is equal to row " + str(i+1))
    for row1,row2 in equalRows:
        rowId = row2
        end = False
        while end == False:
            if row1 - 1 >= 0 and row2 + 1 < len(pattern):
                row1-=1 
                row2+=1
                if pattern[row1] != pattern[row2]:
                    end = True
            else:
                return rowId*100

    return -1

def fixSmudgeVertical(pattern):
    smudges = []
    for j in range(len(pattern[0])-1):
        equal = True
        for row in pattern:
            if row[j]!=row[j+1]:
                equal = False
        if equal == False:
            differences = []
            for i in range(len(pattern)):
                if pattern[i][j] != pattern[i][j+1]:
                    differences.append((i,j))
            if len(differences) == 1:
                smudges.append(differences[0])
    return smudges

def fixSmudgeHorizontal(pattern):
    smudges = []
    for i in range(len(pattern)-1):
        if pattern[i] != pattern[i+1]:
            differences = []
            for j in range(len(pattern[i])):
                if pattern[i][j] != pattern[i+1][j]:
                    differences.append((i,j))
            if len(differences) == 1:
                smudges.append(differences[0])
                
    return smudges

def getReflexion(pattern):
    result = -1
    result = checkHorizontal(pattern)
    if result == -1:
        result = checkVertical(pattern)
    return result

#Solution to Part 1
def part1(lines):
    patterns = parse(lines)
    total = 0
    for pattern in patterns:
        ref = getReflexion(pattern)
        total += ref
    print("The total reflexion is: " + str(total))

#Solution to Part 2
def part2(lines):
    patterns = parse(lines)
    total = 0
    for pattern in patterns:
        smudgesHor = fixSmudgeHorizontal(pattern)
        smudgesVer = fixSmudgeVertical(pattern)
        print(str(smudgesHor) + "--" + str(smudgesVer))
    print("")

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