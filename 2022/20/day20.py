import os
from pathlib import Path
from copy import deepcopy
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

class Number(object):
    def __init__(self, value, index):
        self.value = value
        self.original_index = index
        self.current_index = index

def switch_numbers(numbers, current_position, target_position, i_number):
    numbers[i_number].current_index = target_position
    for number in numbers: 
        if number.current_index == target_position:
            number.current_index = current_position
            break

numbers = []
for i, line in enumerate(lines):
    numbers.append(Number(int(line.strip()),i))

def move_step(array, value, current_position, direction, i_number):
    
    if current_position + direction >= len(array): ### overflows to the right
        target_position = 0
    elif current_position + direction < 0 : ### overflows to the left
        target_position = len(array)-1
    else:
        target_position = current_position + direction
    
    array[current_position] = array[target_position]
    array[target_position] = value
    switch_numbers(numbers,current_position,target_position, i_number)

    return array, target_position

def get_right_and_left(array, pos):
    if pos + 1 >= len(array): ### overflows to the right
        b = 0
    else:
        b = pos + 1
    if pos -1 < 0 : ### overflows to the left
        a = len(array) - 1
    else:
        a = pos - 1
    return array[a], array[b]

def get_grove_coordinates(array):
    result_index = -1
    result = 0
    while result_index <= 3000:
        for number in array:
            if result_index == -1:
                if number == 0:
                    result_index = 1
            else:
                if result_index == 1000 or result_index == 2000 or result_index == 3000:
                    print(f'the {result_index}th number is {number}')
                    result += number
            result_index += 1    
    return result

result_array = []
for number in numbers:
    result_array.append(number.value)


print(f'Initial arrangement \n {result_array} \n')
for i, number in enumerate(numbers):
    print(f'Number {i+1}/{len(numbers)}')
    current_position = number.current_index
    steps_to_move = abs(number.value)
    if number.value > 0:
        direction = 1
    else:
        direction = -1
    while steps_to_move > 0:
        result_array, target_position = move_step(result_array, number.value, current_position, direction, i)
        current_position = target_position
        steps_to_move-=1

    a, b = get_right_and_left(result_array,current_position)

    #if number.value == 0:
    #    print(f' {number.value} does not move \n {result_array} \n')
    #else:
    #    print(f' {number.value} moves between {a} and {b} \n {result_array} \n')
coords = get_grove_coordinates(result_array)
print(f'Part 1: The grave coordinates are {coords}')