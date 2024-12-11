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
    lines = f.read().split(" ")
    return lines

def get_blink(stones):
    new_stones = []
    for stone in stones:
        if int(stone) == 0:
            new_stones += ["1"]
        elif len(stone) % 2 != 0:
            new_stones += [str(int(stone)*2024)]
        else:
            mid = len(stone) // 2  # Find the middle index
            new_stones += [str(int(stone[:mid])), str(int(stone[mid:]))]
    return new_stones

def add_to_dict(dict, key, value):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value
    return dict

def get_blink_2(stones_dic):
    new_stones = {}
    for stone in stones_dic:
        if stone == "0":
            new_stones = add_to_dict(new_stones,"1",stones_dic[stone])
        elif len(stone) % 2 != 0:
            new_stones = add_to_dict(new_stones,str(int(stone)*2024),stones_dic[stone])
        else:
            mid = len(stone) // 2  # Find the middle index
            new_stones = add_to_dict(new_stones,str(int(stone[:mid])),stones_dic[stone])
            new_stones = add_to_dict(new_stones,str(int(stone[mid:])),stones_dic[stone])
    return new_stones

#Solution to Part 1 brute force hehe
def part_1(stones):
    blinks = 25
    for i in range(1,blinks+1):
        stones = get_blink(stones)
        #print(f"After {i} blinks: {stones}")
    print(f"After {i} blinks, there are {len(stones)} stones")

def get_total(stones):
    total = 0
    for stone in stones:
        total += stones[stone]
    return total

#Solution to Part 2 smarter way
def part_2(stones):
    stones_dic = {}
    for stone in stones:
        stones_dic[stone] = 1
    blinks = 75
    for i in range(1,blinks+1):
        stones_dic = get_blink_2(stones_dic)
        #print(f"After {i} blinks: {stones_dic}")
    
    print(f"After {i} blinks, there are {get_total(stones_dic)} stones")

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