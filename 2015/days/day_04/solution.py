from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 609043, "part2": None},
    {"input": "input_test_2.txt", "part1": 1048970, "part2": None}
]

def parse(data):
    lines = parse_lines(data)
    return lines[0]

def md5_hash(secret_key, number):
    import hashlib
    to_hash = f"{secret_key}{number}".encode()
    return hashlib.md5(to_hash).hexdigest()

def is_valid(hash_str, num_zeros):
    return hash_str.startswith("0" * num_zeros)

def get_smallest_number(secret_key, num_zeros):
    number = 1
    while True:
        hash_str = md5_hash(secret_key, number)
        if is_valid(hash_str, num_zeros):
            return number
        number += 1

def part1(data):
    secret_key = parse(data)
    return get_smallest_number(secret_key, num_zeros=5)

def part2(data):
    secret_key = parse(data)
    return get_smallest_number(secret_key, num_zeros=6)
