import os
from pathlib import Path
from collections import deque as queue
p = Path(__file__).with_name('test.txt')

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
    start = (-1,-1)
    destination = (-1, -1)
    for i, line in enumerate(input):
        row = []
        line = line.strip()
        for j, char in enumerate(line.strip()):
            if char == "S":
                start = (i,j)
                row.append(Cell(ord("a")))
            elif char == "E":
                destination = (i,j)
                row.append(Cell(ord("z")))
            else:
                row.append(Cell(ord(char)))
        grid.append(row)
    return grid, start, destination

def isValid(grid, current_node, next_node, visited):
    sx,sy = current_node
    tx,ty = next_node
    if (tx,ty) in visited:
        print("next node has already been visited. Skipping...")
        return False
    elif(tx < 0 or ty < 0 or tx > (len(grid)-1) or ty > (len(grid[0])-1) ):
        #print("next node out of bounds")
        return False
    elif(grid[tx][ty].height - grid[sx][sy].height) > 1:
        #print(f'{(tx,ty)}-{(sx,sy)} ---- {grid[tx][ty].height} - {grid[sx][sy].height}')
        return False
    else:
        return True

def bfs(grid, source, destination):
    q = queue()
    visited = set()
    q.append(source)
    
    while len(q) > 0:
        nx, ny = q.popleft()
        
        
        if (nx, ny) == destination:
            return visited
        # check right
        if isValid(grid, (nx,ny), (nx,ny+1), visited):
            q.append((nx,ny+1))
            visited.add((nx,ny+1))
        # check left
        if isValid(grid, (nx,ny), (nx,ny-1), visited):
            q.append((nx,ny-1))
            visited.add((nx,ny-1))
        # check up
        if isValid(grid, (nx,ny), (nx-1,ny), visited):
            q.append((nx-1,ny))
            visited.add((nx-1,ny))
        # check down
        if isValid(grid, (nx,ny), (nx+1,ny), visited):
            q.append((nx+1,ny))
            visited.add((nx+1,ny))
    return "NO DESTINATION FOUND"

grid, start, destination = initGrid(lines)

a = set()
a.add( (1,1) )


print(len(bfs(grid, start, destination)))