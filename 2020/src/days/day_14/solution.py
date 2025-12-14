from lib import *
import re

TESTS = [
    {"input": "input_test_1.txt", "part1": 165, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 208}
]

# test and solution work on 36 bit integers
MASK_LEN = 36

def parse(data):
    lines = parse_lines(data)
    operations = []
    for line in lines:
        if "mask" in line:
            mask_str = re.search(r"mask = ([X01]+)", line).group(1)
            mask = {i: c for i, c in enumerate(mask_str) if c != "X"}
            operations.append(("mask", mask))
        else:
            match = re.search(r"mem\[(\d+)\] = (\d+)", line)
            if match:
                address = int(match.group(1))
                value = int(match.group(2))
                operations.append(("mem", (address, value)))
    return operations

def add_padding(bin_str):
    return bin_str.zfill(MASK_LEN) # equivalent to "0"*MASK_LEN+bin_str

# Applies mask v1 - returns single string (result to be written in address)
def apply_mask_v1(bin_str, mask):
    bin_list = list(bin_str)
    for bit in mask:
        bin_list[bit] = mask[bit]
    return "".join(bin_list)

def part1(data):
    operations = parse(data)
    mem = dict()
    current_mask = None
    for op in operations:
        if op[0] == "mask":
            current_mask = op[1]
        elif op[0] == "mem":
            address, value = op[1]
            value_bin = add_padding(bin(value)[2:])
            mem_bin_result = apply_mask_v1(value_bin, current_mask)
            mem[address] = int(mem_bin_result,2)
    return sum(mem.values())

# Applies mask v2. Returns a list of mem addresses (in bin)
def apply_mask_v2(bin_str, mask):
    bin_list = list(bin_str)
    for i in range(MASK_LEN):
        if i in mask and mask[i] == "1":
            bin_list[i] = "1"
        else:
            bin_list[i] = "X"
    bins = []
    def get_mask_combos(bin_list, i):
        if i == len(bin_list):
            bins.append("".join(bin_list))
            return
        if bin_list[i] == "X":
            for bit in ["1", "0"]:
                bin_list_copy = bin_list.copy()
                bin_list_copy[i] = bit
                get_mask_combos(bin_list_copy, i+1)
        else:
            get_mask_combos(bin_list, i+1)
    get_mask_combos(bin_list, 0)
    return bins

def part2(data):
    operations = parse(data)
    mem = {}
    current_mask = None
    for op in operations:
        if op[0] == "mask":
            current_mask = op[1]
        elif op[0] == "mem":
            address, value = op[1]
            address_bin = add_padding(bin(address)[2:])
            # This time the mask gives us addresses!
            mem_addresses = apply_mask_v2(address_bin, current_mask)
            # For each address, overwrite with the given decimal value
            for mem_address in mem_addresses:
                mem[int(mem_address, 2)] = value
    return sum(mem.values())
