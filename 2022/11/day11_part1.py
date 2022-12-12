import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

class Monkey(object):
    def __init__(self, ):
        self.operation = "" ### operation in format: [smth] [operator] [smth]
        self.test_div = 0
        self.test_true = -1
        self.test_false = -1
        self.inspected_items = 0
        self.items = []

    def calc_new_worry(self, old_worry): 
        operand_1 = 0
        operand_2 = 0
        operator = self.operation.strip().split(" ")[1]
        
        if self.operation.strip().split(" ")[0] == "old":
            operand_1 = old_worry
        else:
            operand_1 = int(self.operation.strip().split(" ")[0])

        if self.operation.strip().split(" ")[2] == "old":
            operand_2 = old_worry
        else:
            operand_2 = int(self.operation.strip().split(" ")[2])

        if operator == "*":
            #print(f'    Worry level is multiplied by {operand_2} to {operand_1 * operand_2}')
            return operand_1 * operand_2
        elif operator == "+":
            #print(f'    Worry level is increased by {operand_2} to {operand_1 + operand_2}')
            return operand_1 + operand_2
        return -1

def init_monkeys(input):
    monkeys = []
    monkey = Monkey()
    for i, line in enumerate(input):
        match i%7:
            case 0:
                monkey = Monkey()
            case 1:
                items = []
                for item in line.split(":")[1].strip().split(","):
                    items.append(int(item))
                monkey.items = items
            case 2:
                monkey.operation = line.split(":")[1].strip().split("=")[1]
            case 3:
                monkey.test_div = int(line.strip().split(" ")[3])
            case 4:
                monkey.test_true = int(line.strip().split(" ")[5].strip())
            case 5:
                monkey.test_false = int(line.strip().split(" ")[5].strip())
                monkeys.append(monkey)
    return monkeys

def print_monkeys(monkeys):
    for m, monkey in enumerate(monkeys):
        print(f'Monkey {m}: {monkey.items}')

def print_result(monkeys):
    print()
    for m, monkey in enumerate(monkeys):
        print(f'Monkey {m} inspected items {monkey.inspected_items} times.')

def get_monkey_business(monkeys):
    n_items = []
    for monkey in monkeys:
        n_items.append(monkey.inspected_items)
    monkey_bussiness = sorted(n_items)[-2] * sorted(n_items)[-1]
    print(f'The level of monkey business is {monkey_bussiness}')

def get_super_modulo(monkeys):
    super_modulo = 0
    for monkey in monkeys:
        if super_modulo == 0:
            super_modulo = monkey.test_div
        else:
            super_modulo = super_modulo * monkey.test_div
    return super_modulo

def calc_round(monkeys, divideWorryLevel, modulo=0):
    for m, monkey in enumerate(monkeys):
        #print(f'Monkey {m}:')
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            #print(f'  Monkey inspects an item with a worry level of {item}')
            monkey.inspected_items += 1
            
            item = monkey.calc_new_worry(item)

            if divideWorryLevel == True:
                item = int(item / 3) ### Part 1 ###
            else: 
                item = int(item % modulo) ### Part 2 ###

            #print(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}')

            if item % monkey.test_div == 0:
                #print(f'    Current worry level is divisible by {monkey.test_div}')

                monkeys[monkey.test_true].items.append(item)
                #print(f'    Item with worry level {item} is thrown to monkey {monkey.test_true}.')
            else:
                #print(f'    Current worry level is not divisible by {monkey.test_div}')

                monkeys[monkey.test_false].items.append(item)
                #print(f'    Item with worry level {item} is thrown to monkey {monkey.test_false}.')
    return monkeys

### Part 1 ###
monkeys = init_monkeys(lines)
round = 1

while round < 21:
    calc_round(monkeys,True)
    #print(f'\nROUND {round}')
    #print_monkeys(monkeys)
    round+=1
get_monkey_business(monkeys)
#print_result(monkeys)

### Part 2 ###
monkeys = init_monkeys(lines)
round = 1
modulo = get_super_modulo(monkeys)
print(f'Modulo is: {modulo}')
while round < 10001:   
    calc_round(monkeys, False, modulo)
    if round == 1 or round == 20 or round%1000==0:
        print(f'\nROUND {round}')
        print_result(monkeys)
    round+=1

get_monkey_business(monkeys)