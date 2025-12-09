from lib import *
from itertools import combinations
from shapely.geometry import Polygon

TESTS = [
    {"input": "input_test_1.txt", "part1": 50, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 24}
]

# Simple formula to calculate the area of a rectangle defined by vertices tile1 and tile2
def get_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    return (max(y2, y1) - min(y2, y1) + 1) * (max(x2, x1) - min(x2, x1) + 1)

def parse(data):
    tiles = list(tuple(map(int, line.split(','))) for line in parse_lines(data))
    return tiles

# Returns a Shapely Polygon from two rectangle vertices
def get_rectangle_polygon(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
        
    # Create rectangle polygon
    return Polygon([
        (min_x, min_y),
        (max_x, min_y),
        (max_x, max_y),
        (min_x, max_y)
    ])

# Generate all rectangles with their areas
def get_all_rectangle_areas(red_tiles):
    rectangles = []
    for tile1, tile2 in combinations(red_tiles, 2):
        area = get_area(tile1, tile2)
        rectangles.append((area, tile1, tile2))
    return rectangles

# For part 1, iterate through all rectangle areas and get the max
def part1(data):
    red_tiles = parse(data)
    rectangles = get_all_rectangle_areas(red_tiles)
    return max(rectangles)[0]

# For part 2, I surrendered trying to figure out efficient ways of checking polygon boundaries
# So decided to use the Shapely boundary
def part2(data):
    red_tiles = parse(data)
    
    # Create polygon from red tiles
    polygon = Polygon(red_tiles)
    
    rectangles = get_all_rectangle_areas(red_tiles)

    # Major optimization! Sort by area descending
    rectangles.sort(reverse=True)
    
    # Check rectangles from largest to smallest
    for area, tile1, tile2 in rectangles:
        rect = get_rectangle_polygon(tile1, tile2)
        # Check if rectangle is within polygon
        if polygon.contains(rect):
            return area
    
    return 0

