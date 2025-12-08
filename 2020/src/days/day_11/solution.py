from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 37, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 26}
]

DIRS = [DIRECTIONS[d] for d in ['up', 'down', 'left', 'right']] + DIRECTIONS['diag']

def parse(data):
    lines = parse_lines(data)
    seats = dict()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == "L":
                seats[(x,y)] = 0
    return seats

def game_of_seats(seats):
    return -1

# Returns the number of adjacent occupied seats
def get_adjacent(seat, seats):
    adjacent = 0
    x, y = seat
    for dx, dy in DIRS:
        neighbor = (x + dx, y + dy)
        if neighbor in seats:  # If neighbor exists and is occupied
            adjacent += seats[neighbor]
    return adjacent

def get_visible_adjacent(seat, seats, boundaries):
    adjacent = 0
    x, y = seat
    max_x, max_y = boundaries
    for dx, dy in DIRS:
        neighbor = (x + dx, y + dy)
        # While on bounds, check further in the same direction
        while neighbor[0] >= 0 and neighbor[0] <= max_x and neighbor[1] >= 0 and neighbor[1] <= max_y:
            # If neighbor exists, add its value and check next dir
            if neighbor in seats:  
                adjacent += seats[neighbor]
                break
            neighbor = (neighbor[0] + dx, neighbor[1] + dy)
    return adjacent

def do_round(seats):
    final_seats = seats.copy()
    changed = False
    for seat in seats:
        adjacent = get_adjacent(seat, seats)
        if seats[seat] == 0 and adjacent == 0: # Free sit
            final_seats[seat] = 1
            changed = True
        elif seats[seat] == 1 and adjacent >= 4: # Occupied sit
            final_seats[seat] = 0
            changed = True
    return final_seats, changed

def do_round_part_2(seats, boundaries):
    final_seats = seats.copy()
    changed = False
    for seat in seats:
        adjacent = get_visible_adjacent(seat, seats, boundaries)
        if seats[seat] == 0 and adjacent == 0: # Free sit
            final_seats[seat] = 1
            changed = True
        elif seats[seat] == 1 and adjacent >= 5: # Occupied sit
            final_seats[seat] = 0
            changed = True
    return final_seats, changed

def print_layout(seats):
    # Find grid boundaries
    max_x = max(x for x, y in seats.keys())
    max_y = max(y for x, y in seats.keys())
    layout = ""
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in seats:
                layout += "#" if seats[(x, y)] == 1 else "L"
            else:
                layout += "."
        layout += "\n"
    
    return layout

def get_occupied_seats(seats):
    return sum([seats[seat] for seat in seats])

def part1(data):
    seats = parse(data)
    changed = True
    while changed == True:
        seats, changed = do_round(seats)
        debug(print_layout(seats))
    return get_occupied_seats(seats)

def part2(data):
    seats = parse(data)
    max_x = max(x for x, y in seats.keys())
    max_y = max(y for x, y in seats.keys())
    changed = True
    while changed == True:
        seats, changed = do_round_part_2(seats, (max_x, max_y))
        debug(print_layout(seats))
    return get_occupied_seats(seats)
