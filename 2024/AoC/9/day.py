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
    line = f.read().strip()
    return line

def get_files(line):
    block = 1
    output, inversed_blocks = [], []
    index = 0
    for c in line:
        if block == 1:
            output += [index] * int(c)
            index += 1
        else:
            output += ["."] * int(c)
        block = block * (-1)
    for i in range(len(output),0,-1):
        if output[i-1] != ".":
            inversed_blocks += [i-1]
    return output, inversed_blocks

def move_files(files, inversed_blocks):
    output = []
    index = 0
    for i in range(0,len(files)):
        new_i = inversed_blocks[index]
        if new_i < i:
            break
        if files[i] == ".":
            output +=[files[new_i]]
            index += 1
        else:
            output += [files[i]]
    return output

def get_checksum(files):
    checksum = 0
    index = 0
    for c in files:
        checksum += index * int(c)
        index += 1
    return checksum


#Solution to Part 1
def part_1(line):
    output, inversed_blocks = get_files(line)
    #print(''.join(map(str,output)))
    output = move_files(output,inversed_blocks)
    #print(''.join(map(str,output)))
    checksum = get_checksum(output)
    print(f"The final checksum is: {checksum}")

def sum_n(a, b):
    return (b-a+1)*(a+b)//2

#Solution to Part 2
def part_2(line):
    lines = [int(x) for x in line]
    idxs = []
    b = 0
    for i in range(len(lines)):
        idxs.append(b)
        b += lines[i]
    res = 0
    id = len(lines)//2
    for j in range(len(lines)-1,-1,-2):
        fsize = lines[j]
        for i in range(1, j, 2):
            if lines[i] >= fsize:
                b = idxs[i]
                res += sum_n(b, b+fsize-1)*id
                idxs[i] += fsize
                lines[i] -= fsize
                break
        else:
            b = idxs[j]
            res += sum_n(b, b+fsize-1)*id
        id -= 1

    print(res)
if __name__ == "__main__":
    if args.test == "true":
        line = parse_input("test"+args.part+".txt")
    else:
        line = parse_input("input"+args.part+".txt")
    if args.part == "1":
        part_1(line)
    elif args.part == "2":
        part_2(line)
    else:
        print("Error: Part number invalid: " + args.part)