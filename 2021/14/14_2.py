from types import new_class
from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

#Initialize polymer template
template = lines[0]
pair_rules = {}
pairs_output = {}
letterCount = {}

#Initialize pair rules
for line in lines [2:]:
    pair_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]

#Count the number of pairs in template
char1 = template[0]
for char in template[1:]:
    char2 = char
    pair = char1 + char2
    if pair not in list(pairs_output.keys()):
        pairs_output[pair] = 1
    else:
        pairs_output[pair] += 1
    char1 = char2

step = 0
while step < 40:
    #print("Step " + str(step+1) + ":")

    #Calculate the new number of pairs (if rule is XY->Z then the pair XY turns into XZ and ZY)
    new_pairs_output = {}
    for pair in list(pairs_output.keys()):
        middleletter = pair_rules[pair]
        new_pair_1 = pair[0] + middleletter
        new_pair_2 = middleletter + pair[1]
        #print(pair + " --> " + new_pair_1 + " and " + new_pair_2)
        if new_pair_1 not in list(new_pairs_output.keys()):
            new_pairs_output[new_pair_1] = pairs_output[pair]
        else:
            new_pairs_output[new_pair_1] += pairs_output[pair]
        if new_pair_2 not in list(new_pairs_output.keys()):
            new_pairs_output[new_pair_2] = pairs_output[pair]
        else:
            new_pairs_output[new_pair_2] += pairs_output[pair]
    pairs_output = new_pairs_output.copy()
    step +=1

print(pairs_output)

#We just count the first letter of each pair
for pair in list(pairs_output.keys()):
    char1 = pair[0]
    if char1 not in list(letterCount.keys()):
        letterCount[char1] = pairs_output[pair]
    else:
        letterCount[char1] += pairs_output[pair]
#...and add the original last letter (which is always the same)
letterCount[template[len(template)-1]] += 1

max = ["",0]
min = ["",-1]

for count in letterCount:
    if letterCount[count] > max[1]:
        max[0] = count
        max[1] = letterCount[count]
    elif letterCount[count] < min[1] or min[1] == -1:
        min[0] = count
        min[1] = letterCount[count]
print(letterCount)
print("Most common: " + str(max))
print("Least common: " + str(min))
print("Difference: " + str(max[1]-min[1]))

stop = timeit.default_timer()

print('Time: ', stop - start)  