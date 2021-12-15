from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
octopuses = []
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]
    for line in lines:
        octopusLine = []
        for char in line:
            octopusLine.append(int(char))
        octopuses.append(octopusLine)


rows, cols = len(octopuses), len(octopuses[0])
deltas = [(0,1),(1,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]

def check_for_flashes(octopusArray, alreadyFlashed):
    newAlreadyFlashed = alreadyFlashed.copy()
    for row in range(0,rows):
        for col in range(0,cols):
            if octopusArray[row][col] > 9 and (row,col) not in alreadyFlashed:
                newAlreadyFlashed.append((row,col))
                ### add 1 to others
                for delta in deltas:
                    if row + delta[0] >= 0 and row + delta[0] < rows and col + delta[1] >= 0 and col + delta[1] < cols:
                        octopusArray[row + delta[0]][col + delta[1]] +=1
                                
    return octopusArray, newAlreadyFlashed

def print_array(array):
    for line in array:
        print(line)

step = 0
total_flashes = 0
while step < 100:
    print("Step " + str(step))
    alreadyFlashed = []
    #print(octopuses)
    ### Add 1 to all elements in the list
    for row in range(0,rows):
        for col in range(0,cols):
            octopuses[row][col] +=1

    ### Check for flashes
    octopuses, newAlreadyFlashed = check_for_flashes(octopuses,alreadyFlashed)
    while len(newAlreadyFlashed) != len(alreadyFlashed):
        alreadyFlashed = newAlreadyFlashed
        octopuses, newAlreadyFlashed = check_for_flashes(octopuses,alreadyFlashed)
    print("There was a total of " + str(len(alreadyFlashed)) + " flashes in this step.")
    total_flashes += len(alreadyFlashed)
    ### Set flashed elements to zero
    for flashed in newAlreadyFlashed:
        octopuses[flashed[0]][flashed[1]] = 0
    print_array(octopuses)
    step+=1

print("There was a total of " + str(total_flashes) + " after " + str(step) + " steps.")
stop = timeit.default_timer()

print('Time: ', stop - start)  