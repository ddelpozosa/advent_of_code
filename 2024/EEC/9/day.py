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

def getNumberOfBeetles(brightness,stamps):
    n_of_beetles = 0
    while brightness > 0:
        for stamp in stamps:
            if brightness >= stamp:
                print(stamp)
                n_of_beetles+=1
                brightness-=stamp
                break    

    return n_of_beetles

def min_numbers_for_target(stamps, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 elements are needed to make target 0
    combination = [[] for _ in range(target + 1)]
    for num in stamps:
        for i in range(num, target + 1):
            if dp[i - num] + 1 < dp[i]:
                dp[i] = dp[i - num] + 1
                # Store the current combination of numbers used
                combination[i] = combination[i - num] + [num]
    if dp[target] == float('inf'):
        return -1, []
    
    return dp[target], combination[target]


#Solution to Part 1
def part1(lines):
    total = 0
    stamps = list(reversed([1, 3, 5, 10]))
    for line in lines:
        n_of_beetles = getNumberOfBeetles(int(line.strip()),stamps)
        printtest("We need " + str(n_of_beetles) + " to reach brightness level " + line.strip())
        total+=n_of_beetles
    print("The minimum number of beetles is: " + str(total))

#Solution to Part 2
def part2(lines):
    total = 0
    stamps = list(reversed([1, 3, 5, 10, 15, 16, 20, 24, 25, 30]))
    for line in lines:
        n_of_beetles, combination = min_numbers_for_target(stamps,int(line.strip()))
        printtest("We need " + str(n_of_beetles) + " to reach brightness level " + line.strip() + " for this combination: " + str(combination))
        total+=n_of_beetles
    print("The minimum number of beetles is: " + str(total) )

#Solution to Part 3
def part3(lines):
    total = 0
    stamps = list(reversed([1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]))
    for line in lines:
        n_of_beetles, combination = min_numbers_for_target(stamps,int(line.strip()))
        printtest("We need " + str(n_of_beetles) + " to reach brightness level " + line.strip() + " for this combination: " + str(combination))
            
    print("The minimum number of beetles is: " + str(total) )

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