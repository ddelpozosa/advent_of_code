from lib import DIRECTIONS, parse_grid, neighbors, debug
TESTS = [
    {"input": "input_test_1.txt", "part1": 13, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 43}
]

def parse(data):
    grid= parse_grid(data)
    rolls_of_paper = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                rolls_of_paper.add((x,y))
    
    return rolls_of_paper, grid

def print_grid(rolls_of_paper, grid):
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if (x,y) in rolls_of_paper:
                row += "@"
            else:
                row += "."
        debug(row)

#(Deprecated) Initial solution for part 1 that checks all grid cells 
def get_accesible_neighbors(grid):
    accesible = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            adjacent_rolls = 0
            if grid[y][x] == ".": # only count rolls of paper
                continue
            debug(f"Checking cell ({x},{y}) with value {grid[y][x]}")
            for neighbor in neighbors(grid, x, y, True):    
                nx, ny = neighbor
                if grid[ny][nx] == "@":
                    adjacent_rolls += 1
            debug(f"Adjacent rolls: {adjacent_rolls}")
            if adjacent_rolls < 4:
                accesible += 1
    return accesible

def get_accesible_neighbors(rolls_of_paper, grid):
    accesible = 0
    rolls_to_delete = set()
    for roll in rolls_of_paper:
        x, y = roll
        adjacent_rolls = 0
        for neighbor in neighbors(grid, x, y, True):    
            nx, ny = neighbor
            if (nx,ny) in rolls_of_paper:
                adjacent_rolls += 1
        if adjacent_rolls < 4:
            accesible += 1
            rolls_to_delete.add(roll)
    for roll in rolls_to_delete:
        rolls_of_paper.discard(roll)
    return accesible

def part1(data):
    rolls_of_paper,grid = parse(data)
    accessible_neighbors = get_accesible_neighbors(rolls_of_paper, grid)
    debug(accessible_neighbors)
    return accessible_neighbors

def part2(data):
    rolls_of_paper, grid = parse(data)
    accessible_neighbors = -1 # to not count initial state
    total_accessible = 0
    while accessible_neighbors != 0:
        accessible_neighbors = get_accesible_neighbors(rolls_of_paper, grid)
        total_accessible += accessible_neighbors
        debug("Removed ", accessible_neighbors, " rolls of paper")
        print_grid(rolls_of_paper, grid)
    return total_accessible