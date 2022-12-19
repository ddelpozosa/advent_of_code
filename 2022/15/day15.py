from pathlib import Path
import ast

p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

sensors = []
beacons = []
not_beacons = set()


def parse_input(input):
    for line in input:
        sensors.append( (int(line.strip().split(" ")[2].split("=")[1].split(",")[0]),int(line.strip().split(" ")[3].split("=")[1].split(":")[0])) )
        beacons.append( (int(line.strip().split(" ")[8].split("=")[1].split(",")[0]),int(line.strip().split(" ")[9].split("=")[1])) )

def print_simulation():
    for y in range(-2,23):
        line = ""
        for x in range(-2,26):
            if (x,y) in sensors:
                line+="S"
            elif (x,y) in beacons:
                line+="B"
            elif (x,y) in not_beacons:
                line+="#"
            else:
                line+="."
        print(line)

def find_not_beacons_all(target_y):
    for i in range(len( sensors)):
        find_not_beacons(i,target_y)
        

def find_not_beacons(i,target_y):
    sx,sy = sensors[i]
    bx,by = beacons[i]
    distance = abs(sx-bx) + abs(sy-by)
    print(f'Beacon {i+1}/{len(sensors)} (len of non_beacons={len(not_beacons)})')
    for x in range(sx-distance,sx+distance+1):
        for y in range(target_y,target_y+1): 
            if abs(sx-x) + abs(sy-y) <= distance:
                #print(f'Adding {x,y}')
                not_beacons.add((x,y))
    #print(f'The distance between {sensors[i]} and {beacons[i]} is {distance}')

def get_number_of_non_beacon(target_y):
    result = 0
    for non_beacon in not_beacons:
        if non_beacon[1] == target_y and non_beacon not in beacons and non_beacon not in sensors:
            result+=1
    return result


parse_input(lines)
#print(sensors)
#print(beacons)

#print_simulation()
#target_y = 10
target_y = 2000000
find_not_beacons_all(target_y)


print(f'Part 1: The number of positions where there can not be a beacon on y={target_y} is {get_number_of_non_beacon(target_y)}')

#print_simulation()