from pathlib import Path
import ast

p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

class Pair(object):
    def __init__(self, left, right):
        self.left = ast.literal_eval(left)
        self.right = ast.literal_eval(right)

### Returns TRUE if inputs are in the right order ###
def compare_pairs(left_list, right_list,indentation): 
    #print(f'{" "*indentation}- Compare {left} vs {right}')
    left = left_list[:]
    right = right_list[:]
    while len(left) > 0:
        if len(right) == 0:
            indentation+=1
            #print(f'{" "*indentation}- Right ran out of items, so inputs are in the wrong order')
            return False
        left_item = left.pop(0)
        right_item = right.pop(0)
        
        
        if type(left_item) == int and type(right_item) == int:
            #print(f'{" "*(indentation+1)}- Compare {left_item} vs {right_item}')
            if left_item < right_item:
                #print(f'{" "*(indentation+2)}- Left side is smaller, so inputs are in the right order')
                return True
            elif left_item > right_item:
                #print(f'{" "*(indentation+2)}- Right side is smaller, so inputs are in the wrong order')
                return False

        elif type(left_item) == list or type(right_item == list):
            if type(left_item) == int:
                #print(f'{" "*(indentation+1)}- Mixed types; convert right to {left_item} and retry comparison')
                left_item = [left_item]
            if type(right_item) == int:
                #print(f'{" "*(indentation+1)}- Mixed types; convert right to {right_item} and retry comparison')
                right_item = [right_item]
            
            result = compare_pairs(left_item,right_item, indentation+1)
            if type(result) == bool:
                return result
    if len(left) == 0 and len(right) == 0:#
        return None
    else:
        return True
    #print(f'{" "*indentation}- Left ran out of items, so inputs are in the right order')
    #return True 

def parse_input(input):
    pairs = []
    left = ""
    right = ""
    for i, line in enumerate(lines):     
        if i%3==0:
            left = line.strip()
        elif i%3==1:
            right = line.strip()
            pairs.append(Pair(left,right))
            
    return pairs

pairs = parse_input(lines)

sum_of_right_indexes = 0
for i, pair in enumerate(pairs):
    #print(f'== Pair {i+1} ==')
    if compare_pairs(pair.left,pair.right,0)==True:
        sum_of_right_indexes += (i+1)

print(f'(Part 1) - The sum of all the right indexes is: {sum_of_right_indexes}')
packets = []
ordered_packets = []

for pair in pairs:
    packets.append(pair.left)
    packets.append(pair.right)
packets.append([[2]])
packets.append([[6]])


for packet in packets:
    if len(ordered_packets) == 0:
        ordered_packets.append(packet)
    elif compare_pairs(packet,ordered_packets[0],0)==True:
        #print(f'Packet {packet} is smaller than the smallest packet {ordered_packets[0]} ')
        ordered_packets.insert(0,packet)
    elif compare_pairs(ordered_packets[-1],packet,0) == True:
        #print(f'Packet {packet} is larger than the largest packet {ordered_packets[-1]} ')
        ordered_packets.append(packet)
    else:
        for i, o_p in enumerate(ordered_packets):
            if compare_pairs(ordered_packets[i],packet,0) == True and compare_pairs(packet,ordered_packets[i+1],0) == True:
                #print(f'Packet {packet} is larger than {ordered_packets[i]} and smaller than {ordered_packets[i+1]} ')
                ordered_packets.insert(i+1,packet)
                break

index_2 = 0
index_6 = 0
for i, packet in enumerate(ordered_packets):
    #print(packet)
    if packet == [[2]]:
        index_2 = i+1
    elif packet == [[6]]:
        index_6 = i+1

print(f'(Part 2) - Divider packets are in the {index_2}th and {index_6}th positions so the decoder key is: {index_2*index_6}')

#print(compare_pairs(p.left, p.right, 0))

#print(compare_pairs([[0, 0], 2],[[0, 0], 1],0))
#print(compare_pairs([[0, 0], 1],[[0, 0], 2],0))