from os import path
import timeit
from typing_extensions import final
import ast

def find_left_number(pair_string, index_left):
    size = 0
    index = None
    for i in range(index_left-1, 0, -1):
        if pair_string[i].isnumeric():
            index = i
            size +=1
        if pair_string[i].isnumeric() == False and index != None:
            break
    return index, size

def find_right_number(pair_string, index_right):
    size = 0
    index = None
    for i in range(index_right+1, len(pair_string)):
        if pair_string[i].isnumeric():
            if index == None:
                index = i
            size +=1
        if pair_string[i].isnumeric() == False and index != None:
            break
    return index, size

def explode_pair(pair_string):
    current_depth = -1
    for i in range(0, len(pair_string)):
        if pair_string[i] == "[":
            current_depth +=1
        elif pair_string[i] == "]":
            current_depth -=1
        elif current_depth >= 4 and pair_string[i+2].isnumeric() and pair_string[i].isnumeric():
            left_delta = 0
            right_delta = 0
            pair_length = 4
            if pair_string[i-1].isnumeric():
                #print("Left explode is size 2")
                left_delta -=1
                pair_length +=1
                pair_left = pair_string[i-1:i+1]
            else:
                pair_left = pair_string[i]
            if pair_string[i+3].isnumeric():
                #print("Right explode is size 2")
                right_delta += 1
                pair_length +=1
                pair_right = pair_string[i+2:i+4]
            else:
                pair_right = pair_string[i+2]

            #print("depth is " + str(current_depth) + " and exploding pair is " + pair_string[i+left_delta:i+3 + right_delta])
            
            #print(pair_string)

            index_right, size = find_right_number(pair_string, i+2 + right_delta)
            #print(index_right,size)
            # Add right pair to the first right number
            if index_right != None:
                intRight = int(pair_string[index_right:index_right+size])
                intRight += int(pair_right)
                if len(str(intRight)) > size:
                    #print("Right length increased, increasing right delta")
                    right_delta += 1
                pair_string = pair_string[:index_right] + str(intRight) + pair_string[index_right+size:]
                #print("Summed Right: " + pair_string)

            index_left, size = find_left_number(pair_string, i+left_delta)
            # Add left pair to the first left number
            if index_left != None:
                intLeft = int(pair_string[index_left:index_left+size])
                intLeft += int(pair_left)
                if len(str(intLeft)) > size:
                    #print("Left length increased, increasing left delta")
                    left_delta += 1
                pair_string = pair_string[:index_left] + str(intLeft) + pair_string[index_left+size:]
                #print("Summing " + pair_left + " to " + pair_string[index_left:index_left+size] + ": " + pair_string)
            
            
            
            # Replace whole pair [a,b] with 0
            pair_string = pair_string[:i-1+left_delta] + "0" + pair_string[i+pair_length+left_delta:]
            #print("After explode: " + pair_string)
            return pair_string

def split_pair(pair_string):
    index = None
    for i in range(0, len(pair_string)):
        if pair_string[i].isnumeric() and pair_string[i+1].isnumeric():
            index = i
            break
    if index != None:
        #print("Number to split found: " + str(pair_string[index:index+2]))
        number_to_split = int(pair_string[index:index+2])
        if number_to_split % 2 == 0:
            left = int(number_to_split/2)
            right = left
        else:
            left = int(number_to_split/2)
            right = int(number_to_split/2) + 1
        pair_string = pair_string[:index] + "[" + str(left) + "," + str(right) + "]" + pair_string[index+2:]
        #print("After split: " + pair_string)
        return pair_string

def calc_magnitude(array):
    if type(array[0]) != list:
        first_digit = int(array[0])
    else:
        first_digit = calc_magnitude(array[0])
    if type(array[1]) != list:
        second_digit = int(array[1])
    else:
        second_digit = calc_magnitude(array[1])
    total = 3*first_digit + 2*second_digit
    return total

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

max_magnitude = 0
for i in range(0,len(lines)):
    for j in range(0, len(lines)):
        if j != i:
            print("Summing " + lines[i] + " + " + lines[j])
            pair_string = "[" + lines[i] + "," + lines[j] + "]"
            end = False
            while end == False:
                new_pair_str = explode_pair(pair_string)
                if new_pair_str == None:
                    new_pair_str = split_pair(pair_string)
                    if new_pair_str == None:
                        print("It has been reduced")
                        end = True
                if new_pair_str != None:
                    pair_string = new_pair_str
            print("Sum finished: " + pair_string)
            res = ast.literal_eval(pair_string)
            magnitude = calc_magnitude(res)
            print("Magnitude: " + str(magnitude))
            if magnitude > max_magnitude:
                max_magnitude = magnitude
                print("Is max magnitude! ")

print("The absolute max magnitude is " + str(max_magnitude))


stop = timeit.default_timer()

print(" ")
print('Time: ', stop - start)  
#print(explode_pair(test_StrSnailFish))
