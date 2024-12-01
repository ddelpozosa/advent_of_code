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

def parse1(lines):
    left, right = [], []
    for line in lines:
        left += [int(line.strip().split("   ")[0])]
        right += [int(line.strip().split("   ")[1])]
    left.sort()
    right.sort()

    return left, right

def parse2(lines):
    left, right = [],{}
    for line in lines:
        left_num = int(line.strip().split("   ")[0])
        right_num = int(line.strip().split("   ")[1])
        left += [left_num]
        if left_num not in right:
            right[left_num] = 0
        if right_num not in right:
            right[right_num] = 1
        else: 
            right[right_num] += 1
    return left, right

#Solution to Part 1
def part1(lines):
    left, right = parse1(lines)
    total_distance = 0
    for i in range(0,len(left)):
        total_distance += abs(right[i] - left[i])
    print("The total distance between the sorted lists is: " + str(total_distance))

#Solution to Part 2
def part2(lines):
    left, right = parse2(lines)
    total_similarity = 0
    for l in left:
        total_similarity += l * right[l]
    print("The total similarity between the lists is: " + str(total_similarity))

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