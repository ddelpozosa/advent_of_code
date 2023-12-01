import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = False, help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

#Solution to Part 1
def part1(file):
    solution = ""
    f = file.open('r')
    lines = f.readlines()

    print(solution)

#Solution to Part 2
def part2(file):
    solution = ""
    f = file.open('r')
    lines = f.readlines()
        
    print(solution)

if __name__ == "__main__":
    if args.test == True:
        file = "test.txt"
    else:
        file = "input.txt"
    if args.part == "1":
        part1(file)
    elif args.part == "2":
        part2(file)
    else:
        print("Error: Part number invalid: " + args.part)