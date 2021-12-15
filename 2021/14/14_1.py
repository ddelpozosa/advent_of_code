from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "test1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

template = lines[0]
pairs = {}
letterCount = {}
for line in lines [2:]:
    pairs[line.split(" -> ")[0]] = line.split(" -> ")[1]


step = 0
while step < 10:
    char1 = template[0]
    final_string = char1
    for char in template[1:]:
        char2 = char
        pair = char1 + char2
        middleLetter = pairs[pair]
        final_string += middleLetter + char2
        char1 = char2
    step +=1
    template = final_string
    print("Step " + str(step) + " completed")


print("Template complete after " + str(step) + " steps. Template length: " + str(len(template)))

for char in template:
    if char not in list(letterCount.keys()):
        letterCount[char] = 1
    else:
        letterCount[char] += 1

max = ["",0]
min = ["",99999999999]

for count in letterCount:
    if letterCount[count] > max[1]:
        max[0] = count
        max[1] = letterCount[count]
    elif letterCount[count] < min[1]:
        min[0] = count
        min[1] = letterCount[count]
print(letterCount)
print("Most common: " + str(max))
print("Least comon: " + str(min))
print("Difference: " + str(max[1]-min[1]))

stop = timeit.default_timer()

print('Time: ', stop - start)  