import argparse
from pathlib import Path
import numpy as np
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

def parseText(lines):
    matrix = []
    for line in lines:
        row = []
        for item in line.strip():
            row += [item]
        matrix += [row]
    return np.array(matrix)

def readDiags(matrix, pattern):
    matches = []
    # true diags
    min = -1*len(matrix)
    max = len(matrix.T)
    for i in range(min,max):
        diagonal = np.diagonal(matrix, offset=i)
        matches += pattern.findall("".join(diagonal))
        matches += pattern.findall("".join(diagonal[::-1]))
    # anti diags
    flipped_matrix = np.fliplr(matrix)
    min = -1*len(flipped_matrix)
    max = len(flipped_matrix.T)
    for i in range(min,max):
        diagonal = np.diagonal(flipped_matrix, offset=i)
        matches += pattern.findall("".join(diagonal))
        matches += pattern.findall("".join(diagonal[::-1]))
    return matches
#Solution to Part 1
def part1(lines):
    matrix = parseText(lines)
    transposed = matrix.T
    matches = []
    pattern = re.compile(r"XMAS")

    #access rows
    for row in matrix:
        matches += pattern.findall("".join(row))  # check left to right
        matches += pattern.findall("".join(row[::-1])) # check right to left
    #access cols
    for col in transposed:
        matches += pattern.findall("".join(col))  # check top to bottom
        matches += pattern.findall("".join(col[::-1])) # check bottom to bottom
    
    matches += readDiags(matrix,pattern)

    print("There are " + str(len(matches)) + " matches.")

def getX(rowi,coli,matrix):
    return matrix[rowi:rowi+3,coli:coli+3]   

#Solution to Part 2
def part2(lines):
    pattern = re.compile(r"MAS")
    matrix = parseText(lines)
    total = 0    
    for rowi in range(0,len(matrix)-2):
        for coli in range(0,len(matrix.T)-2):
            x = getX(rowi,coli,matrix)
            matches = readDiags(x,pattern)
            if len(matches) == 2:
                total += 1
    print("There are " + str(total) + " X-MAS")            

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