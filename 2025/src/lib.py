from collections import defaultdict, deque
import heapq

# Debugging utility
_test_mode = False
def set_test_mode(is_test):
    global _test_mode
    _test_mode = is_test

def debug(*args, **kwargs):
    if _test_mode:
        print(*args, **kwargs)

# Directions for grid traversal
DIRECTIONS = {
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0),
    'diag': [(-1, -1), (-1, 1), (1, -1), (1, 1)]
}

def neighbors(grid, x, y, include_diag=False):
    dirs = [DIRECTIONS[d] for d in ['up', 'down', 'left', 'right']]
    if include_diag:
        dirs += DIRECTIONS['diag']
    return [(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)]

def bfs(start, goal, neighbors_func):
    #Breadth-first search
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        for neighbor in neighbors_func(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def dijkstra(start, goal, neighbors_func, cost_func):
    #Dijkstra's shortest path
    pq = [(0, start)]
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        if node == goal:
            return cost
        visited.add(node)
        for neighbor in neighbors_func(node):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + cost_func(node, neighbor), neighbor))
    return float('inf')

def lcm(a, b):
    #Least common multiple
    from math import gcd
    return abs(a * b) // gcd(a, b)

def gcd(a, b):
    #Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def calculate_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def parse_lines(data):
    #Parse input as list of lines
    return data.strip().split('\n')

def parse_grid(data):
    #Parse input as 2D grid (list of lists)
    return [list(line) for line in data.strip().split('\n')]

def parse_numbers(data):
    #Parse input as list of integers
    return [int(x) for x in data.strip().split()]

def parse_groups(data):
    #Parse input as groups separated by blank lines
    return data.strip().split('\n\n')

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        #Add edge from u to v with optional weight
        self.edges[u].append((v, weight))
    
    def neighbors(self, node):
        #Get neighbors of a node
        return [v for v, _ in self.edges[node]]
    
    def cost(self, u, v):
        #Get cost between u and v
        for neighbor, weight in self.edges[u]:
            if neighbor == v:
                return weight
        return float('inf')