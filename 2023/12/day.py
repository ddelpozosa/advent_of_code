import argparse
import itertools
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
    conditions = []
    groups = []

    for line in lines:
        conditions.append(line.strip().split(" ")[0])
        group_unit = []
        for group in line.strip().split(" ")[1].split(","):
            group_unit.append(int(group))
        groups.append(group_unit)
    return conditions, groups

def check_conditions(condition, group_unit):
    valid = True
    condition_units = []
    for group in condition.split("."):
        if len(group) != 0:
            condition_units.append(len(group))
    if len(condition_units) == len(group_unit):
        for i in range(0,len(condition_units)):
            if condition_units[i] != group_unit[i]:
                valid = False
    else:
        valid = False
    return valid

def fill_pounds(s, chars):
    for p in map(iter, itertools.product(chars, repeat=s.count('?'))):
        yield ''.join(c if c != '?' else next(p) for c in s)

#Solution to Part 1
def part1(lines):
    total = 0
    conditions, groups = parse(lines)
    for i in range(0,len(conditions)):
        print("Combination " + str(i) + "/" + str(len(conditions)))
        #printtest(conditions[i] + "---" + str(groups[i]))
        possibilities = fill_pounds(conditions[i], '.#')
        combinations = 0
        for possibility in possibilities:
            #printtest(possibility)
            valid = check_conditions(possibility, groups[i])
            if valid == True:
                combinations += 1
        printtest(conditions[i] + " has " + str(combinations) + " possible combinations")
        total += combinations
    print("The sum of all combinations is: " + str(total))

def parse_2(lines):
    conditions = []
    groups = []

    for line in lines:
        conditions.append(line.strip().split(" ")[0] + "?")
        group_unit = []
        for group in line.strip().split(" ")[1].split(","):
            group_unit.append(int(group))
        groups.append(group_unit)
    return conditions, groups   

def parse_fold(lines):
    conditions = []
    groups = []

    for line in lines:
        c = ""
        print(line.strip().split(" ")[0])
        for i in range(5): 
            
            c += line.strip().split(" ")[0]
            if i < 4:
                c += "?"
        conditions.append(c)
        group_unit = []
        for i in range(5):
            for group in line.strip().split(" ")[1].split(","):
                group_unit.append(int(group))
        groups.append(group_unit)
    return conditions, groups


#Solution to Part 2
def part2(lines):
    total = 0
    conditions, groups = parse_2(lines)
    print(conditions[0] + "-" + str(groups[0]))
    for i in range(0,len(conditions)):
        print("Combination " + str(i) + "/" + str(len(conditions)))
        #printtest(conditions[i] + "---" + str(groups[i]))
        possibilities = fill_pounds(conditions[i], '.#')
        combinations = 0
        #print(sum(1 for _ in possibilities))
        for possibility in possibilities:
            #printtest(possibility)
            valid = check_conditions(possibility, groups[i])
            if valid == True:
                combinations += 1
        printtest(conditions[i] + " has " + str(combinations) + " possible combinations")
        total += combinations
    print("The sum of all combinations is: " + str(total))

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