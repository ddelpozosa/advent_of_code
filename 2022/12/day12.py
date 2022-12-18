import os
from pathlib import Path
from collections import deque as queue
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()


class Cell(object):
    def __init__(self, height):
        self.height = height
        self.visited = False
        self.representation = "."

def printGrid(grid):
    output = ""
    for row in grid:
        for cell in row:
            output += cell.representation
        output += "\n"
    print(output)

def initGrid(input):
    grid = []
    starts = []
    destination = (-1, -1)
    for i, line in enumerate(input):
        row = []
        line = line.strip()
        for j, char in enumerate(line.strip()):
            if char == "S" or char == "a":
                starts.append( (i,j) )
                row.append(Cell(ord("a")))
            elif char == "E":
                destination = (i,j)
                row.append(Cell(ord("z")))
            else:
                row.append(Cell(ord(char)))
        grid.append(row)
    return grid, starts, destination

def isValid(grid, current_node, next_node, visited):
    sx,sy = current_node
    tx,ty = next_node
    if (tx,ty) in visited:
        #print("next node has already been visited. Skipping...")
        return False
    elif(tx < 0 or ty < 0 or tx > (len(grid)-1) or ty > (len(grid[0])-1) ):
        #print("next node out of bounds")
        return False
    elif(grid[tx][ty].height - grid[sx][sy].height) > 1:
        #print(f'{(tx,ty)}-{(sx,sy)} ---- {grid[tx][ty].height} - {grid[sx][sy].height}')
        return False
    else:
        return True
class Queue_object(object):
    def __init__(self, ancestors, current):
        self.ancestors = ancestors
        self.current = current

def bfs(grid, source, destination):
    q = queue()
    visited = set()
    q.append(Queue_object([],source))
    
    while len(q) > 0:
        queue_object = q.popleft()
        nx, ny = queue_object.current
        #print(f'My ancestors are: {queue_object.ancestors}')
        if (nx, ny) == destination:
            return queue_object.ancestors
        # check right
        
        if isValid(grid, (nx,ny), (nx,ny+1), visited):
            l = queue_object.ancestors[:]
            l.append((nx,ny))
            q.append(Queue_object(l,(nx,ny+1)))
            visited.add((nx,ny+1))
        # check left
        if isValid(grid, (nx,ny), (nx,ny-1), visited):
            l = queue_object.ancestors[:]
            l.append((nx,ny))
            q.append(Queue_object(l,(nx,ny-1)))
            visited.add((nx,ny-1))
        # check up
        if isValid(grid, (nx,ny), (nx-1,ny), visited):
            l = queue_object.ancestors[:]
            l.append((nx,ny))
            q.append(Queue_object(l,(nx-1,ny)))
            visited.add((nx-1,ny))
        # check down
        if isValid(grid, (nx,ny), (nx+1,ny), visited):
            l = queue_object.ancestors[:]
            l.append((nx,ny))
            q.append(Queue_object(l,(nx+1,ny)))
            visited.add((nx+1,ny))
    return []

grid, starts, destination = initGrid(lines)

a = set()
a.add( (1,1) )

#print(starts)
print(f'(Part One) The shortest path starting from S is: {len(bfs(grid, starts[0], destination))}.' )
shortest_path = 0 
for start in starts:
    path_len = len(bfs(grid, start, destination))
    #print(f'Start: {start}. Len: {path_len}')
    if shortest_path == 0 or path_len < shortest_path:
        if path_len != 0:
            shortest_path = path_len

print(f'(Part Two) The shortest path starting any S or a is: {shortest_path}.' )