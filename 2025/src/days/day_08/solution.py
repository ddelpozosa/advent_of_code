from lib import *
import itertools
import math

TESTS = [
    {"input": "input_test_1.txt", "part1": 40, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 25272}
]

def parse(data):
    nodes = parse_lines(data)

    # Every node starts as its own circuit
    circuits = [set([node]) for node in nodes]
    edges = []
    for node_a, node_b in itertools.combinations(nodes, 2):
        # Parse nodes string into a tuple of 3 coords (x,y,z)
        p1,p2 = tuple(map(int,node_a.split(','))), tuple(map(int,node_b.split(','))) 
        # Built-in efficient function to get distance between two points
        distance = math.dist(p1, p2) 
        edges.append((distance, node_a, node_b))
    # Sorts on distance
    edges.sort()
    return circuits, edges

def merge_circuits(node_a, node_b, circuits):
    set_a = next(s for s in circuits if node_a in s)
    set_b = next(s for s in circuits if node_b in s)
    if set_a != set_b:
        set_a.update(set_b)
        circuits.remove(set_b)

# 1. Each junction starts as its own individual circuit
# 2. Find the two junctions closest to each other (skip if they are already part of the same circuit)
# 3. Connect the juntions (and the circuit they are a part of)
# 4. Return the size of the three largest circuits after connecting all pairs

# For test: process the first 10 closest pairs, whether already connected or not
# For prod: process the first 1000 closest pairs, whether already connected or not

def part1(data):
    circuits, edges = parse(data)
    
    edges = edges[:1000] # We just care about the 10 (test) or 1000 (prod) closest pairs
    for edge in edges:
        merge_circuits(edge[1], edge[2], circuits)

    sizes = sorted([len(c) for c in circuits], reverse=True)
    result = 1
    for size in sizes[:3]:
        result *= size
    return result

def get_x(node):
    return int(node.split(",")[0])

# Simply iterate until all nodes belong to the same circuit, then return the product of the x coordinates of the edge
def part2(data):
    circuits, edges = parse(data)
    
    for edge in edges:
        merge_circuits(edge[1], edge[2], circuits)
        if len(circuits) == 1:
            return get_x(edge[1]) * get_x(edge[2])

