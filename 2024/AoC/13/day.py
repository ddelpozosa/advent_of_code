import argparse
import numpy as np
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def print_test(text):
    if args.test == "true":
        print(text)

def parse_input(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.read().split("\n")
    lines += [""]
    machines = []
    a1, b1, c1, a2, b2, c2 = None, None, None, None, None, None
    for line in lines:
        if "Button A" in line:
            a1 = int(line.split("+")[1].split(",")[0])
            a2 = int(line.split("+")[2])
        elif "Button B" in line:
            b1 = int(line.split("+")[1].split(",")[0])
            b2 = int(line.split("+")[2])
        elif "Prize" in line:
            c1 = int(line.split("=")[1].split(",")[0])
            c2 = int(line.split("=")[2])
            if args.part == "2":
                c1 += 10000000000000
                c2 += 10000000000000
        else:
            machines += [[a1, b1, c1, a2, b2, c2]]
            a1, b1, c1, a2, b2, c2 = None, None, None, None, None, None
    return machines

#Button A: X+94, Y+34
#Button B: X+22, Y+67
#Prize: X=8400, Y=5400
#94a + 22b = 8400
#43a + 67b = 5400

def solve_by_matrix(a1, b1, c1, a2, b2, c2):
    # a1*x + b1*y = c1
    # a2*x + b2*y = c2
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    return np.linalg.solve(A, B)

def is_int(X): #check if the result matrix is really integers
    return all(abs(x - round(x)) < 1e-4 for x in X)

#Solution to Part 1
def part_1(machines):
    tokens = 0
    for i in range(len(machines)):
        machine = machines[i]
        a1, b1, c1, a2, b2, c2 = machine[0],machine[1],machine[2],machine[3],machine[4],machine[5]
        solution = solve_by_matrix(a1, b1, c1, a2, b2, c2)
        if is_int(solution):
            print(f"Machine {i+1} is solvable with {solution[0]}({round(solution[0])}) A tokens and {round(solution[1])} tokens")
            tokens += 3*int(round(solution[0])) + round(solution[1])
        else:
            print(f"Machine {i} is not solvable")
    print(f"We need {tokens} tokens.")
#Solution to Part 2
def part_2(machines):
    tokens = 0
    print(machines)
    for i in range(len(machines)):
        print(f"Calculating {i}/{len(machines)}")
        machine = machines[i]
        a1, b1, c1, a2, b2, c2 = machine[0],machine[1],machine[2],machine[3],machine[4],machine[5]
        solution = solve_by_matrix(a1, b1, c1, a2, b2, c2)
        if is_int(solution):
            #print(f"Machine {i+1} is solvable with {solution[0]}({round(solution[0])}) A tokens and {round(solution[1])} tokens")
            tokens += 3*int(round(solution[0])) + round(solution[1])
    print(f"We need {tokens} tokens.")  

if __name__ == "__main__":
    if args.test == "true":
        lines = parse_input("test"+args.part+".txt")
    else:
        lines = parse_input("input"+args.part+".txt")
    if args.part == "1":
        part_1(lines)
    elif args.part == "2":
        part_2(lines)
    else:
        print("Error: Part number invalid: " + args.part)