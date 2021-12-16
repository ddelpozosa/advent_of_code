from os import path
import timeit
import sys

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

def get_version_of_packet(packet_str):
    total_version = int(packet_str[0:3],2)
    print("Analyzing --- " + packet_str)
    type_ID = int(packet_str[3:6],2)
    current_index = -1
    if type_ID == 4:
        print("Type ID is 4 so this is a literal and version is " + str(total_version))
        current_index = 6
        end = False
        while end == False:
            if packet_str[current_index] == "1":    
                current_index += 5
            else:
                end = True
                current_index += 5
        return total_version, current_index
    else:
        print("Type ID is " + str(type_ID) + " so this is an operator and version is " + str(total_version))
        length_type_ID = packet_str[6]
        if length_type_ID == "0":
            print("Length ID is 0")
            total_packet_length = int(packet_str[7:22],2)
            end_index = total_packet_length + 22
            print("Total packet length is " + str(total_packet_length) + ". Rest of packet string: " + packet_str[22:end_index])
            last_packet_index = 22
            next_packet_index = -1
            next_literal = packet_str[last_packet_index+next_packet_index:end_index]
            while next_literal != "":
                sub_packet_version, next_packet_index = get_version_of_packet(packet_str[last_packet_index:end_index])
                print("The subpacket version was " + str(sub_packet_version) + " and the next packet starts at index " + str(last_packet_index+next_packet_index) + ". Its literal would be: " + packet_str[last_packet_index+next_packet_index:end_index])
                total_version += sub_packet_version
                next_literal = packet_str[last_packet_index+next_packet_index:end_index]
                last_packet_index = last_packet_index+next_packet_index
            return total_version, last_packet_index
        else:
            number_of_subPackets = int(packet_str[7:18],2)
            print("Length ID is 1. It contains " + str(number_of_subPackets) + ". Rest of packet string: " + packet_str[18:])
            last_packet_index = 18
            next_packet_index = -1
            for i in range(0,number_of_subPackets):
                print("sub packet " + str(i+1) + "/" + str(number_of_subPackets))
                sub_packet_version, next_packet_index = get_version_of_packet(packet_str[last_packet_index:])
                print("The subpacket version was " + str(sub_packet_version) + " and the next packet starts at index " + str(last_packet_index+next_packet_index) + ". Its literal would be: " + packet_str[last_packet_index+next_packet_index:])
                total_version += sub_packet_version
                last_packet_index = last_packet_index+next_packet_index
                i+=1
            return total_version, last_packet_index

total_version_sum = 0
for line in lines:
    bin_str = hex_to_bin(line)
    version_sum = get_version_of_packet(bin_str)[0]
    total_version_sum += version_sum
    print("")
    print("Total version of line " + line + " is: " + str(version_sum))
    print("")

print("Total version sum of all of them is " + str(total_version_sum))

stop = timeit.default_timer()

print('Time: ', stop - start)  