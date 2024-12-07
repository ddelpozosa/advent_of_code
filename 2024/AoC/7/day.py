import argparse
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
    nums, results = [],[]
    for line in f.read().split("\n"):
        nums += [[int(num) for num in line.split(": ")[1].split(" ")]]
        results += [int(line.split(": ")[0])]
    return nums, results

#1 means possible, 0 means impossible
def is_result_possible(target,numbers,subtotal, next_i, successes=0):
    if subtotal == target and next_i == len(numbers): #we got it :)
        return 1
    elif subtotal > target or next_i == len(numbers): #reached the end or surpassed target
        return 0
    successes += is_result_possible(target,numbers,subtotal+numbers[next_i],next_i+1)
    successes += is_result_possible(target,numbers,subtotal*numbers[next_i],next_i+1)
    return successes

#1 means possible, 0 means impossible
def is_result_possible_2(target,numbers,subtotal, next_i, successes=0):
    if subtotal == target and next_i == len(numbers): #we got it :)
        return 1
    elif subtotal > target or next_i == len(numbers): #reached the end or surpassed target
        return 0

    successes += is_result_possible_2(target,numbers,subtotal+numbers[next_i],next_i+1)
    successes += is_result_possible_2(target,numbers,subtotal*numbers[next_i],next_i+1)
    successes += is_result_possible_2(target,numbers,int(str(subtotal)+str(numbers[next_i])),next_i+1)
    
    return successes


#Solution to Part 1
def part_1(numbers_list, results):
    sum = 0
    for i in range(0, len(results)):
        target = results[i]
        numbers = numbers_list[i]
        success = is_result_possible(results[i],numbers_list[i],numbers_list[i][0],1)
        if success > 0:
            sum += target
        if args.test == "true":
            print(f"{target}:{numbers} has {success} possibilites")
    print(f"The calibration result is: {sum}")

#Solution to Part 2
def part_2(numbers_list, results):
    sum = 0
    for i in range(0, len(results)):
        target = results[i]
        numbers = numbers_list[i]
        success = is_result_possible_2(results[i],numbers_list[i],numbers_list[i][0],1)
        if success > 0:
            sum += target
        if args.test == "true":
            print(f"{target}:{numbers} has {success} possibilites")
    print(f"The calibration result is: {sum}")

if __name__ == "__main__":
    if args.test == "true":
        nums, results = parse_input("test"+args.part+".txt")
    else:
        nums, results = parse_input("input"+args.part+".txt")
    if args.part == "1":
        part_1(nums, results)
    elif args.part == "2":
        part_2(nums, results)
    else:
        print("Error: Part number invalid: " + args.part)