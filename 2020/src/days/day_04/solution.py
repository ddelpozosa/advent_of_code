from lib import *
import re

TESTS = [
    {"input": "input_test_1.txt", "part1": 2, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 0},
    {"input": "input_test_3.txt", "part1": None, "part2": 4}
]

VALIDATIONS = {
    "byr": lambda x: bool(re.match(r'^\d{4}$', x)) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: bool(re.match(r'^\d{4}$', x)) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: bool(re.match(r'^\d{4}$', x)) and 2020 <= int(x) <= 2030,
    "hgt": lambda x: validate_height(x),
    "hcl": lambda x: bool(re.match(r'^#[0-9a-f]{6}$', x)),
    "ecl": lambda x: bool(re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x)), 
    "pid": lambda x: bool(re.match(r'^[0-9]{9}$', x)),
}

def parse(data):
    passports = parse_groups(data)

    return passports

def validate_height(height):
    match = re.match(r'(^\d+)(cm|in)', height)
    if not match:
        return 0
    if match.groups()[1] == "cm":
        return 150 <= int(match.groups()[0]) <= 193
    elif match.groups()[1] == "in":
        return 59 <= int(match.groups()[0]) <= 76
    return 0

def is_valid(passport, part):
    pattern = r"([^\s\n]+)"
    matches = re.findall(pattern, passport)
    remaining_fields = set(VALIDATIONS)
    debug("\nValidating ", passport)
    for field in matches:
        field_key = field.split(":")[0]
        if field_key in remaining_fields:
            if part == 1:
                remaining_fields.remove(field_key)
            elif part == 2:
                field_value = field.split(":")[1]
                # validate the value
                if VALIDATIONS[field_key](field_value):
                    debug(field, " is valid")
                    remaining_fields.remove(field_key)
                else:
                    debug(field_key, " is invalid")
                    return 0 # If even one field is invalid, whole passport is invalid
            
    if len(remaining_fields) > 0:
        return 0 # If a field is missing, passport is invalid
    return 1 # If nothing makes it invalid, it's valid

def validate_passports(passports, part):
    total = 0
    for passport in passports:
        total += is_valid(passport, part)
    return total

def part1(data):
    passports = parse(data)
    return validate_passports(passports, 1)

def part2(data):
    passports = parse(data)
    return validate_passports(passports, 2)
