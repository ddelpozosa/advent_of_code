from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 1227775554, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 4174379265}
]

def parse(data):
    ranges = [tuple(int(id) for id in elf.split("-")) for elf in data.strip().split(",")]
    return ranges

#Invalid IDs are those where the first half matches the second half
def is_valid(id):
    str_id = str(id)
    #If it has an odd number of digits, it's valid
    if len(str_id) % 2 != 0:
        return True
    elif str_id[0:len(str_id)//2] == str_id[len(str_id)//2:]:
        return False
    return True

def is_valid_part_2(id):
    str_id = str(id)
    length = len(str_id)
    for i in range(1, (length // 2)+1): # maximum part size for invalid Ids is half the string length (a group of 2)
        # if the string is divisible by i, check that all parts are different
        if len(str_id) % i == 0:
            parts = set()
            for j in range(0, length, i): # step by i (search for equal parts of size i)
                parts.add(str_id[j:j+i])
                if len(parts) > 1:
                    continue
            if len(parts) == 1: # all parts are the same = invalid
                return False          
    return True

def part1(data):
    ranges = parse(data)
    sum_of_invalid = 0
    for r in ranges:
        start, end = r[0], r[1]
        for id in range(start, end + 1):
            if is_valid(id) == False:
                sum_of_invalid += id
                debug(id, " is invalid")
    return sum_of_invalid

def part2(data):
    ranges = parse(data)
    sum_of_invalid = 0
    debug("1006 is ", is_valid_part_2(1006))
    for r in ranges:
        start, end = r[0], r[1]
        for id in range(start, end + 1):
            if is_valid_part_2(id) == False:
                sum_of_invalid += id
                debug(id, " is invalid")
    return sum_of_invalid