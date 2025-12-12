from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 25, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 286}
]

# x,y
# order of directions -> E, S, W, N [(1,0), (0,-1), (-1,0), (0,1)]
# parse with index 0, 1, 2, 3
# 0 90 180 270 -> current + 0, 1, 2, 3 respectevely
# if current angle < 0, current angle + 360
# (current angle % 360 // 90)

DIRECTIONS = {'E':0, 'S':1, 'W':2, 'N':3}
DIRECTIONS_VECTOR = [(1,0), (0,-1), (-1,0), (0,1)]

def parse(data):
    lines = parse_lines(data)
    instructions = []
    for line in lines:
        op, amount = line[0], int(line[1:])
        instructions.append((op,amount))
    return instructions

def part1(data):
    instructions = parse(data)
    current_angle = 0 # in degrees. 0 faces east
    position = (0,0) # initial position
    for op, amount in instructions:
        # Move in an arbitrary direction
        if op in DIRECTIONS:
            dx, dy = DIRECTIONS_VECTOR[DIRECTIONS[op]]
            position = (position[0] + dx*amount, position[1] + dy*amount)
        # Moving in the direction currently facing
        elif op == 'F':
            dx, dy = DIRECTIONS_VECTOR[(current_angle // 90)]
            position = (position[0] + dx*amount, position[1] + dy*amount)
        elif op == 'R':
            current_angle = (current_angle + amount) % 360
        elif op == 'L':
            current_angle = (current_angle - amount + 360) % 360
    # Return Manhattan distance
    return abs(position[0]) + abs(position[1])

def rotate_waypoint(waypoint, degrees):
    x, y = waypoint
    # Normalize to 90-degree rotations 
    # (right = clockwise = degrees>0, left = counter-clockwise = degrees<0)
    rotations = (degrees // 90) % 4
    for _ in range(rotations):
        x, y = y, -x
    return (x,y)

def part2(data):
    instructions = parse(data)
    boat_pos = (0,0)
    waypoint_pos = (10,1) # Position relative to the boat
    for op, amount in instructions:
        # Move the waypoint in a cardinal direction
        if op in DIRECTIONS:
            dx, dy = DIRECTIONS_VECTOR[DIRECTIONS[op]]
            waypoint_pos = (waypoint_pos[0] + dx*amount, waypoint_pos[1] + dy*amount)
        # Move the boat to the Waypoint position x amount of times
        elif op == 'F':
            dx, dy = waypoint_pos
            boat_pos = (boat_pos[0] + dx*amount, boat_pos[1] + dy*amount)
        elif op == 'R':
            waypoint_pos = rotate_waypoint(waypoint_pos, amount)
        elif op == 'L':
            waypoint_pos = rotate_waypoint(waypoint_pos, -amount)
    # Return Manhattan distance
    return abs(boat_pos[0]) + abs(boat_pos[1])
