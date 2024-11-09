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

enemies = {"A":0, "B":1, "C":3, "D":5, "x":0}

#Solution to Part 1
def part1(lines):
    total = 0
    for c in lines[0]:
        total += enemies[c]

    print(total)

#Solution to Part 2
def part2(lines):
    total = 0
    row = lines[0]
    for i in range(0,int(len(row)/2)):
        subtotal = 0
        subtotal += enemies[row[i*2]]
        subtotal += enemies[row[i*2 + 1]]
        if row[i*2] != "x" and row[i*2 + 1] != "x":
            subtotal += 2
        if args.test == "true":
            print("The value of " + row[i*2] + row[i*2+1] + " is: " + str(subtotal))
        total += subtotal
    print(total)

#Solution to Part 3
def part3(lines):
    total = 0
    row = lines[0]
    for i in range(0,int(len(row)/3)):
        subtotal = 0
        subtotal += enemies[row[i*3]]
        subtotal += enemies[row[i*3 + 1]]
        subtotal += enemies[row[i*3 + 2]]
        x = 0
        if row[i*3] == "x":
            x+=1
        if row[i*3+1] == "x":
            x+=1
        if row[i*3+2] == "x":
            x+=1
        if x==1:
            subtotal+=2
        elif x==0:
            subtotal+=6
        if args.test == "true":
            print("The value of " + row[i*3] + row[i*3+1] + row[i*3+2] + " is: " + str(subtotal))
        total += subtotal
    print(total)
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