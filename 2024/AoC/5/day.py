import argparse
from pathlib import Path
from functools import cmp_to_key
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
    order_str, pages = f.read().split("\n\n")
    order = {}
    order_rev = {}
    for line in order_str.split("\n"):
        if int(line.split("|")[0]) in order:
            order[int(line.split("|")[0])] += [int(line.split("|")[1])]
        else:
            order[int(line.split("|")[0])] = [int(line.split("|")[1])]

        if int(line.split("|")[1]) in order_rev:
            order_rev[int(line.split("|")[1])] += [int(line.split("|")[0])]
        else:
            order_rev[int(line.split("|")[1])] = [int(line.split("|")[0])]
    pages = list([int(item) for item in page.split(",")] for page in pages.split("\n"))
    return order, order_rev, pages

def is_page_valid(order,page,backwards=False):
    if backwards == True:
        page.reverse()
    next_values = []
    for number in page:
        for n in next_values:
            if len(n) != 0 and number not in n:
                return False
        if number in order:
            next_values +=  [order[number]]
    return True

def is_valid(order,order_rev,page):
    valid = is_page_valid(order,page)
    if valid: #reverse search
        valid = is_page_valid(order_rev,page,True)
    return valid

#Solution to Part 1
def part_1(order,order_rev, pages):
    sum = 0
    for page in pages:
        if is_valid(order,order_rev,page):
            sum += int(page[int((len(page)-1)/2)])
    print("The sum of the middle point of valid pages is: " + str(sum))

def order_page(order, page):
    def rule_based_sort(a, b):
        # Does a have a requirement for b to be in front?
        if a in order and b in order[a]:
            return -1 # b goes after
        if b in order and a in order[b]:
            return 1 # b goes before
        return 0 # not in list / equal
    sorted_update = sorted(page, key=cmp_to_key(rule_based_sort))
    return sorted_update

#Solution to Part 2
def part_2(order,order_rev, pages):
    sum = 0
    for page in pages:
        if not is_valid(order,order_rev,page):
            ordered_page = order_page(order,page)
            sum += int(ordered_page[int((len(ordered_page)-1)/2)])
    print("The sum of the middle point of fixed pages is: " + str(sum))

if __name__ == "__main__":
    if args.test == "true":
        order,order_rev, pages = parse_input("test"+args.part+".txt")
    else:
        order,order_rev, pages = parse_input("input"+args.part+".txt")
    if args.part == "1":
        part_1(order,order_rev, pages)
    elif args.part == "2":
        part_2(order,order_rev, pages)
    else:
        print("Error: Part number invalid: " + args.part)