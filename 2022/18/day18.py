import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

cubes = []
for line in lines:
    cubes.append((int(line.strip().split(",")[0]),int(line.strip().split(",")[1]),int(line.strip().split(",")[2])))

external_sides = 0
for cube in cubes:
    x,y,z = cube
    if (x+1,y,z) not in cubes:
        external_sides += 1
    if (x-1,y,z) not in cubes:
        external_sides += 1
    if (x,y+1,z) not in cubes:
        external_sides += 1
    if (x,y-1,z) not in cubes:
        external_sides += 1
    if (x,y,z+1) not in cubes:
        external_sides += 1
    if (x,y,z-1) not in cubes:
        external_sides += 1

print(f'Part 1: The surface area of the droplet is: {external_sides}')

min_x = min(cubes, key=lambda tup: tup[0])[0]
max_x = max(cubes, key=lambda tup: tup[0])[0]
min_y = min(cubes, key=lambda tup: tup[1])[1]
max_y = max(cubes, key=lambda tup: tup[1])[1]
min_z = min(cubes, key=lambda tup: tup[2])[2]
max_z = max(cubes, key=lambda tup: tup[2])[2]

visited = set()
def is_accessible_to_air(x,y,z):
    visited.add((x,y,z))
    if(x <= min_x or x >= max_x or y<= min_y or y>=max_y or z<=min_z or z>=max_z):
        return True
    if (x+1,y,z) not in cubes and (x+1,y,z) not in visited:
        a = is_accessible_to_air(x+1,y,z)
        if a == True:
            return a
    if (x-1,y,z) not in cubes and (x-1,y,z) not in visited:
        a=is_accessible_to_air(x-1,y,z)
        if a == True:
            return a
    if (x,y+1,z) not in cubes and (x,y+1,z) not in visited:
        a=is_accessible_to_air(x,y+1,z)
        if a == True:
            return a
    if (x,y-1,z) not in cubes and (x,y-1,z) not in visited:
        a=is_accessible_to_air(x,y-1,z)
        if a == True:
            return a
    if (x,y,z+1) not in cubes and (x,y,z+1) not in visited:
        a=is_accessible_to_air(x,y,z+1)
        if a == True:
            return a
    if (x,y,z-1) not in cubes and (x,y,z-1) not in visited:
        a=is_accessible_to_air(x,y,z-1)
        if a == True:
            return a

for x in range(min_x,max_x+1):
    for y in range(min_y,max_y+1):
        for z in range(min_z,max_z+1):
            if (x,y,z) not in cubes:
                current = is_accessible_to_air(x,y,z)
                visited = set()
                print((x,y,z))
                if current != True:
                    #print(f'({x},{y},{z}) is not accesible to air.')
                    if (x+1,y,z) in cubes:
                        external_sides -= 1
                    if (x-1,y,z) in cubes:
                        external_sides -= 1
                    if (x,y+1,z) in cubes:
                        external_sides -= 1
                    if (x,y-1,z) in cubes:
                        external_sides -= 1
                    if (x,y,z+1) in cubes:
                        external_sides -= 1
                    if (x,y,z-1) in cubes:
                        external_sides -= 1
print(f'Part 2: The external surface area of the droplet is: {external_sides}')