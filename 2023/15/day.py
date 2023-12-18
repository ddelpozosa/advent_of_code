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

def parse(lines):
    sequences = lines[0].strip().split(",")
    return sequences

def hash_alg(line):
    current_value = 0
    for char in line:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
        #printtest("After char " + char + " value is " + str(current_value))
    return current_value

#Solution to Part 1
def part1(lines):

    sequences = parse(lines)
    sum = 0
    for seq in sequences:
        hash_value = hash_alg(seq)
        sum += hash_value
        printtest(seq + " becomes " + str(hash_value))
    print("The sum of all hash values is: " + str(sum))

def init_boxes():
    boxes = []
    for i in range(256):
        boxes.append([])
    return boxes

def print_boxes(boxes):
    for i, box in enumerate(boxes):
        if len(box)>0:
            printtest("Box " + str(i) + ": " + str(box))

def label_in_box(box, lb):
    for i, lbls in enumerate(box):
        if lbls[0] == lb:
            return True, i
    return False, -1

def get_focusing_power(boxes):
    total = 0
    for i, box in enumerate(boxes):
        for j,lense in enumerate(box):
            total += ((i+1) * (j+1) * int(lense[1]))
    return total


#Solution to Part 2
def part2(lines):
    sequences = parse(lines)
    boxes = init_boxes()
    sum = 0
    for seq in sequences:
        if "=" in seq:
            label = seq.split("=")[0]
            focal_strength = seq.split("=")[1]
            box_id = hash_alg(label)
            found, i = label_in_box(boxes[box_id],label)
            
            if found:
                boxes[box_id][i][1] = focal_strength
            else:
                boxes[box_id].append([label,focal_strength]) 

        elif "-" in seq:
            label = seq.split("-")[0]
            box_id = hash_alg(label)
            found, i = label_in_box(boxes[box_id],label)
            if found:
                boxes[box_id].pop(i)

        printtest('After ' + seq + ":")
        print_boxes(boxes)
        printtest("")
    total = get_focusing_power(boxes)
    print("The sum of all focusing powers is: " + str(total))

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