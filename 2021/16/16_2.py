from os import path
import timeit
import sys
from typing_extensions import final

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

hexa = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def hex_to_bin(hex_str):
    bin_str = ""
    for char in hex_str:
        bin_str += hexa[char]
    return bin_str

def calc_value(value_array,typeID):
    final_value = 0
    # Sum of all elements
    if typeID == 0:
        for value in value_array:
            final_value = final_value + value
    # Product of all elements
    elif typeID == 1:
        final_value = 1
        for value in value_array:
            final_value = final_value * value
    elif typeID == 2:
        final_value = min(value_array)
    elif typeID == 3:
        final_value = max(value_array)
    elif typeID == 5:
        if value_array[0] > value_array[1]:
            final_value = 1
        else:
            final_value = 0
    elif typeID == 6:
        if value_array[0] < value_array[1]:
            final_value = 1
        else:
            final_value = 0
    elif typeID == 7:
        if value_array[0] == value_array[1]:
            final_value = 1
        else:
            final_value = 0

    return final_value

def get_values_of_packet(packet_str):

    print("Analyzing --- " + packet_str)
    type_ID = int(packet_str[3:6],2)
    current_index = -1
    if type_ID == 4:
        current_index = 6        
        end = False
        final_bin_num = ""
        while end == False:
            print("Type ID is 4 so this is a literal and its value is " + str(packet_str[current_index:(current_index+5)]))
            final_bin_num += packet_str[(current_index+1):(current_index+5)]
            if packet_str[current_index] == "1":    
                current_index += 5
            else:
                end = True
                current_index += 5
        
        value = int(final_bin_num,2)
        print("The final number is " + final_bin_num + ", which is decimal is: " + str(value))
        return value, current_index
    else:
        #print("Type ID is " + str(type_ID) + " so this is an operator and version is ")
        length_type_ID = packet_str[6]
        if length_type_ID == "0":
            #print("Length ID is 0")
            total_packet_length = int(packet_str[7:22],2)
            end_index = total_packet_length + 22
            #print("Total packet length is " + str(total_packet_length) + ". Rest of packet string: " + packet_str[22:end_index])
            last_packet_index = 22
            next_packet_index = -1
            next_literal = packet_str[last_packet_index+next_packet_index:end_index]
            value_array = []
            while next_literal != "":
                value, next_packet_index = get_values_of_packet(packet_str[last_packet_index:end_index])
                #print("The next packet starts at index " + str(last_packet_index+next_packet_index) + ". Its literal would be: " + packet_str[last_packet_index+next_packet_index:end_index])
                value_array.append(value)
                next_literal = packet_str[last_packet_index+next_packet_index:end_index]
                last_packet_index = last_packet_index+next_packet_index
            
            #calculate
            value = calc_value(value_array,type_ID)
            print("Value array is : " + str(value_array) + " and type ID is " + str(type_ID))
            print("Value is: " + str(value))
            return value, last_packet_index
        else:
            number_of_subPackets = int(packet_str[7:18],2)
            #print("Length ID is 1. It contains " + str(number_of_subPackets) + ". Rest of packet string: " + packet_str[18:])
            last_packet_index = 18
            next_packet_index = -1
            value_array = []
            for i in range(0,number_of_subPackets):
                #print("sub packet " + str(i+1) + "/" + str(number_of_subPackets))
                value, next_packet_index = get_values_of_packet(packet_str[last_packet_index:])
                #print("The next packet starts at index " + str(last_packet_index+next_packet_index) + ". Its literal would be: " + packet_str[last_packet_index+next_packet_index:])
                value_array.append(value)
                last_packet_index = last_packet_index+next_packet_index
                i+=1
            
            #calculate
            value = calc_value(value_array,type_ID)
            print("Value array is : " + str(value_array) + " and type ID is " + str(type_ID))
            print("Value is: " + str(value))
            return value, last_packet_index


bin_str = hex_to_bin(lines[0])
total_value, index = get_values_of_packet(bin_str)

print("Final value: " + str(total_value))
stop = timeit.default_timer()

print('Time: ', stop - start)  

print(calc_value([0],1))