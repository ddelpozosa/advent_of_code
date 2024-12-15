import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def print_test(text):
    if args.test == "true":
        print(text)

def print_grid(grid):
    for line in grid:
        row = ""
        for item in line:
            row += item
        print(row)
    print()

def parse_input(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.read().split("\n")
    mid = -1
    for i,line in enumerate(lines):
        if line == "":
            mid = i
    grid = []
    for line in lines[:mid]:
        row = []
        for item in line:
            row += [item]
        grid += [row]
    instructions = []
    for line in lines[mid+1:]:
        for item in line:
            if item == "v":
                instructions += [(0,1)]
            elif item == "<":
                instructions += [(-1,0)]
            elif item == ">":
                instructions += [(1,0)]
            elif item == "^":
                instructions += [(0,-1)]
            else:
                print("ERROR")

    return grid, instructions

def parse_input_2(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.read().split("\n")
    mid = -1
    for i,line in enumerate(lines):
        if line == "":
            mid = i
    grid = []
    for line in lines[:mid]:
        row = []
        for item in line:
            if item == "@":
                row += [item,"."]
            elif item == "O":
                row += ["[","]"]
            else:
                row += [item,item]
        grid += [row]
    instructions = []
    for line in lines[mid+1:]:
        for item in line:
            if item == "v":
                instructions += [(0,1)]
            elif item == "<":
                instructions += [(-1,0)]
            elif item == ">":
                instructions += [(1,0)]
            elif item == "^":
                instructions += [(0,-1)]
            else:
                print("ERROR")

    return grid, instructions

def get_limits(grid):
    return len(grid[0]),len(grid)

def get_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                return (x,y)
    return -1

# if returns None, then
def calculate_movement(position, instruction, grid):
    next_position = (position[0] + instruction[0], position[1] + instruction[1])
    next_type = grid[next_position[1]][next_position[0]]
    if next_type == "#":
        return None
    elif next_type == ".":
        return next_position
    elif next_type == "O":
        return calculate_movement(next_position, instruction, grid)

def update_grid(grid,position,instruction, next_position):
    # case where next free spot is adjacent
    adjacent = (position[0] + instruction[0], position[1] + instruction[1])
    if next_position == adjacent:
        grid[position[1]][position[0]] = "."
        grid[next_position[1]][next_position[0]] = "@"
        return next_position
    # case where we need to push stuff
    else:
        grid[position[1]][position[0]] = "."
        grid[adjacent[1]][adjacent[0]] = "@"
        grid[next_position[1]][next_position[0]] = "O"
        return adjacent

def get_gps_sum(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                total += 100 * y + x
    return total

#Solution to Part 1
def part_1(grid, instructions):
    position = get_start(grid)
    for instruction in instructions:
        next_position = calculate_movement(position, instruction, grid)
        #print(f"Move {instruction} (I am in {position}):")
        if next_position != None:
            #print(f"next free position is {next_position}")
            next_position = update_grid(grid,position,instruction, next_position)
            position = next_position
        #print_grid(grid)   
    sum = get_gps_sum(grid)
    print(f"The sum of all boxes GPS is: {sum}")

def calculate_movement_2(position, instruction, grid):
    next_position = (position[0] + instruction[0], position[1] + instruction[1])
    next_type = grid[next_position[1]][next_position[0]]
    response = []
    if next_type == "#":
        response += [None]
    elif next_type == ".":
        response += [next_position]
    elif instruction[0] != 0: #right or left movement. easy
        response += calculate_movement_2(next_position, instruction, grid)
    #upwards or downwards. we need to take into account both
    elif next_type == "[":
        next_position_2 = (next_position[0] + 1, next_position[1] + 0)
        response += [next_position,calculate_movement_2(next_position, instruction, grid),next_position_2,calculate_movement_2(next_position_2, instruction, grid)]
    elif next_type == "]":
        next_position_2 = (next_position[0] - 1, next_position[1] + 0)
        response += [next_position,calculate_movement_2(next_position, instruction, grid),next_position_2,calculate_movement_2(next_position_2, instruction, grid)]
    return response

def flatten_recursive(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_recursive(item))
        else:
            flat_list.append(item)
    return list(set(flat_list))

def update_grid_2(grid,position,instruction, next_positions):
    # case where next free spot is adjacent
    adjacent = (position[0] + instruction[0], position[1] + instruction[1])
    if adjacent in next_positions:
        grid[position[1]][position[0]] = "."
        grid[next_positions[0][1]][next_positions[0][0]] = "@"
        return next_positions[0]
    # case where we need to push stuff
    else:
        # easy case (left to right)
        if len(next_positions) == 1:
            next_position = next_positions[0]
            y = next_position[1]
            #moving to the left
            if next_position[0] < position[0]:
                for x in range(next_position[0], adjacent[0]):
                    if grid[y][x] == ".":
                        grid[y][x] = "["
                    elif grid[y][x] == "[":
                        grid[y][x] = "]"
                    elif grid[y][x] == "]":
                        grid[y][x] = "["
            #moving to the right
            elif next_position[0] > position[0]:
                for x in range(adjacent[0]+1, next_position[0]+1):
                    if grid[y][x] == ".":
                        grid[y][x] = "]"
                    elif grid[y][x] == "[":
                        grid[y][x] = "]"
                    elif grid[y][x] == "]":
                        grid[y][x] = "["
            grid[position[1]][position[0]] = "."
            grid[adjacent[1]][adjacent[0]] = "@"
            return adjacent
        #top to bottom
        else:
            if next_positions[0][1] < position[1]:
                unique_dict = {}
                for x, y in next_positions:
                    if x not in unique_dict or y < unique_dict[x]:
                        unique_dict[x] = y

                # Convert back to a list of tuples
                next_positions = [(x, y) for x, y in unique_dict.items()]
            else:
                unique_dict = {}
                for x, y in next_positions:
                    if x not in unique_dict or y > unique_dict[x]:
                        unique_dict[x] = y

                # Convert back to a list of tuples
                next_positions = [(x, y) for x, y in unique_dict.items()]
            for next_position in next_positions:
                x = next_position[0]
                #going up
                distance = abs(next_position[0] - adjacent[0])//2
                if next_position[1] < position[1]:
                    #print(f"Going up. nextpos:{next_position},distance:{distance}")
                    for y in range(next_position[1] , adjacent[1]- distance):
                        grid[y][x] = grid[y+1][x]
                #going down
                elif next_position[1] > position[1]:
                    #print(f"Going down. nextpos:{next_position},distance:{distance}")
                    for y in range(next_position[1],adjacent[1] + distance,-1):
                        grid[y][x] = grid[y-1][x]
                if adjacent[0] == next_position[0]:
                    grid[position[1]][position[0]] = "."
                    grid[adjacent[1]][adjacent[0]] = "@"
                else:
                    if next_position[1] < position[1]:
                        grid[adjacent[1] - distance][next_position[0]] = "."
                    elif next_position[1] > position[1]:
                        grid[adjacent[1] + distance][next_position[0]] = "."
            return adjacent

def update_grid_2_bis(grid,position,instruction, next_positions):
    print("??")
    # case where next free spot is adjacent
    adjacent = (position[0] + instruction[0], position[1] + instruction[1])
    if adjacent in next_positions and len(next_positions)==0:
        grid[position[1]][position[0]] = "."
        grid[next_positions[0][1]][next_positions[0][0]] = "@"
        return next_positions[0]
    # case where we need to push stuff
    else:
        # easy case (left to right)
        if len(next_positions) == 1:
            next_position = next_positions[0]
            y = next_position[1]
            #moving to the left
            if next_position[0] < position[0]:
                for x in range(next_position[0], adjacent[0]):
                    if grid[y][x] == ".":
                        grid[y][x] = "["
                    elif grid[y][x] == "[":
                        grid[y][x] = "]"
                    elif grid[y][x] == "]":
                        grid[y][x] = "["
            #moving to the right
            elif next_position[0] > position[0]:
                for x in range(adjacent[0]+1, next_position[0]+1):
                    if grid[y][x] == ".":
                        grid[y][x] = "]"
                    elif grid[y][x] == "[":
                        grid[y][x] = "]"
                    elif grid[y][x] == "]":
                        grid[y][x] = "["
            grid[position[1]][position[0]] = "."
            grid[adjacent[1]][adjacent[0]] = "@"
            return adjacent
        #top to bottom
        else:
            #going up
            print("asd")
            if next_positions[0][1] < position[1]:
                for next_position in next_positions:
                    x = next_position[0]
                    y = next_position[1]
                    print("a")
                    if (x,y+1) in next_positions:
                        print("switching")
                        grid[y][x] = grid[y+1][x]
                    #going down
            elif next_positions[0][1] > position[1]:
                    #print(f"Going down. nextpos:{next_position},distance:{distance}")
                    for y in range(next_position[1],adjacent[1],-1):
                        grid[y][x] = grid[y-1][x]
            return adjacent

def get_gps_sum_2(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "[":
                total += 100 * y + x
    return total

#Solution to Part 2
def part_2(grid, instructions):
    #print_grid(grid)  
    position = get_start(grid)
    
    for instruction in instructions[:3590]:
        print(f"Move {instruction} (I am in {position}):")
        next_positions = calculate_movement_2(position, instruction, grid)
        next_positions = flatten_recursive(next_positions)
        if None not in next_positions:
            print(f"moving to: {next_positions}")
            next_position = update_grid_2(grid,position,instruction, next_positions)
            
            position = next_position
            #print(f"I will be in {position}")
            print_grid(grid) 
    print_grid(grid)  
    #print(grid, instructions)
    sum = get_gps_sum_2(grid)
    print(f"The sum of all boxes GPS is: {sum}")

if __name__ == "__main__":
    
    if args.part == "1":
        if args.test == "true":
            grid, instructions = parse_input("test"+args.part+".txt")
        else:
            grid, instructions = parse_input("input"+args.part+".txt")
        part_1(grid, instructions)
    elif args.part == "2":
        if args.test == "true":
            grid, instructions = parse_input_2("test"+args.part+".txt")
        else:
            grid, instructions = parse_input_2("input"+args.part+".txt")
        part_2(grid, instructions)
    else:
        print("Error: Part number invalid: " + args.part)