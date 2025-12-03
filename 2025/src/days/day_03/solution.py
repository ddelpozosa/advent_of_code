from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 357, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 3121910778619}
]

def parse(data):
    banks = parse_lines(data)
    return banks

#joltage is a string representation of a 2 digit integer
def is_joltage_in_bank(bank, joltage):
    for i in range(0,len(bank)):
        if bank[i] == joltage[0]:
            for j in range(i+1,len(bank)):
                if bank[j] == joltage[1]:
                    return True
    return False

#joltage is a string representation of a any digit integer
def is_joltage_in_bank_recursive(bank, joltage, index_bank=0, index_joltage=0):
    if index_joltage >= len(joltage):
        return True
    if index_bank >= len(bank):
        return False
    if bank[index_bank] == joltage[index_joltage]:
        return is_joltage_in_bank_recursive(bank, joltage, index_bank + 1, index_joltage + 1)
    else:
        return is_joltage_in_bank_recursive(bank, joltage, index_bank + 1, index_joltage)

# Greedy algorithm to find the maximum joltage
# For each digit position, try digits 9 down to 0 and pick the first that allows completing the remaining digits.
def get_max_joltage_greedy(bank, digits):
    result = []
    bank_index = 0
    
    for pos in range(digits):
        remaining_digits = digits - pos
        # Try digits from 9 down to 0
        for digit_char in "9876543210":
            # Find this digit in bank starting from bank_index
            found_index = bank.find(digit_char, bank_index)
            if found_index == -1:
                continue  # This digit doesn't exist in remaining bank
            
            # Check if we can still form the remaining digits after this one
            remaining_bank = bank[found_index + 1:]
            if len(remaining_bank) >= remaining_digits - 1:
                # We can use this digit
                result.append(digit_char)
                bank_index = found_index + 1
                break
    
    return int(''.join(result)) if result else 0

def get_max_joltage(bank, digits):
    if digits == 2:
        # Original brute force is fast enough for 2 digits
        max_joltage = 10**digits - 1
        for i in range(max_joltage, -1, -1):
            joltage = str(i)
            if is_joltage_in_bank_recursive(bank, joltage):
                return i
        return max_joltage
    else:
        # Use greedy algorithm for larger digit counts
        return get_max_joltage_greedy(bank, digits)

def part1(data):
    banks = parse(data)
    sum_joltage = 0
    for bank in banks:       
        max_joltage = get_max_joltage(bank, 2)
        debug("Max joltage for " , bank, " = ",max_joltage)
        sum_joltage += max_joltage
    return sum_joltage

def part2(data):
    banks = parse(data)
    sum_joltage = 0
    for bank in banks:       
        max_joltage = get_max_joltage(bank, 12)
        debug("Max joltage for " , bank, " = ",max_joltage)
        sum_joltage += max_joltage
    return sum_joltage
