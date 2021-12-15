file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/2/input1.txt', 'r')
lines = file1.readlines()

horizontal = 0
depth = 0
for line in lines:
    keyword = line.split(" ")[0]
    value = int(line.split(" ")[1])
    #print(keyword + "-" + str(value))
    if keyword=="forward":
        horizontal += value
    elif keyword=="down":
        depth += value
    else:
        depth -= value
print(horizontal)
print(depth)
print(horizontal*depth)