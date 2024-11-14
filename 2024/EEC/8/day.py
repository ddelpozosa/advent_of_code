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

#Solution to Part 1
def part1(lines):
    n_of_blocks = int(lines[0].strip())
    total, last_row = 1,1
    while total < n_of_blocks:
        last_row += 2
        total += last_row
    printtest("The last row has " + str(last_row) + " blocks and we are missing " + str(total-n_of_blocks) + " blocks.")
    print("Final answer: " + str(last_row*(total-n_of_blocks)))


#Solution to Part 2
def part2(lines):
    nullPointer = int(lines[0].strip())
    if args.test == "true":
        acolytes = 5
        n_of_blocks = 50
    else:
        acolytes = 1111
        n_of_blocks = 20240000
    total, last_row,thickness = 1,1,1
    while total < n_of_blocks:
        thickness = (thickness*nullPointer) % acolytes
        last_row += 2
        total += last_row*thickness
    printtest("The last row has " + str(last_row) + " blocks and we are missing " + str(total-n_of_blocks) + " blocks.")
    print("Final answer: " + str(last_row*(total-n_of_blocks)))    

def getBlocks(pyramid,nullPointer,acolytes):
    total = 0
    total += pyramid[0]
    for col in pyramid[1:-1]:
        total += col - ((nullPointer * len(pyramid)*col)%acolytes)
    total += pyramid[-1]
    return total


#Solution to Part 3
def part3(lines):
    nullPointer = int(lines[0].strip())
    if args.test == "true":
        acolytes = 5
        n_of_blocks = 160
    else:
        acolytes = 10
        n_of_blocks = 202400000
    total, last_row,thickness = 1,1,1
    layer = 2
    pyramid = [1]
    while total < n_of_blocks :
        thickness = (acolytes + (thickness*nullPointer) % acolytes)
        
        for i in range(0,last_row):
            pyramid[i] = pyramid[i] + thickness
        pyramid = [thickness] + pyramid + [thickness]
        last_row += 2
        total = getBlocks(pyramid,nullPointer,acolytes)
        printtest("total blocks is " + str(total) + " blocks for layer " + str(layer))
        layer+=1
    print("The king needs to purchase " + str(total-n_of_blocks) +" blocks")
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