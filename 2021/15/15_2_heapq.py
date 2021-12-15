from os import path
import timeit
from collections import defaultdict
from heapq import *

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

# Found in https://gist.github.com/kachayev/5990802
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None
rows, cols = len(lines), len(lines[0])


rows, cols = len(lines), len(lines[0])
lastNode = ((rows*5-1),(cols*5-1))
startNode = (0,0)

edges = []

for row in range(0,rows*5):
    for col in range(0,cols*5):
        current_node = (row,col)
        nextRow = row
        nextCol = col
        #print(current_node + ":")
        if row + 1 < rows*5:
            nextRow = row + 1
            qRow = nextRow // rows
            modRow = nextRow % rows
            qCol = nextCol // cols
            modCol = nextCol % cols

            #print("1next row is " + str(nextRow) + " and its mod is " + str(modRow))
            #print("1next col is " + str(nextCol) + " and its mod is " + str(modCol))
            value = ( int(lines[modRow][modCol]) + (qRow + qCol) ) % 9
            if value == 0:
                value = 9
            #print("value is: " + str(value))
            next_node = (nextRow,nextCol)
            edges.append((current_node,next_node,value))
        nextRow = row
        if col + 1 < cols*5:
            nextCol = col + 1
            qRow = nextRow // rows
            modRow = nextRow % rows
            qCol = nextCol // cols
            modCol = nextCol % cols
            #print("2next row is " + str(nextRow) + " and its mod is " + str(modRow))
            #print("2next col is " + str(nextCol) + " and its mod is " + str(modCol))
            value = ( int(lines[modRow][modCol]) + (qRow + qCol) ) % 9
            if value == 0:
                value = 9
            #print("value is: " + str(value))
            next_node = (nextRow,nextCol)
            edges.append((current_node,next_node,value))
        nextCol = col
        if row - 1 >= 0:
            nextRow = row - 1
            qRow = nextRow // rows
            modRow = nextRow % rows
            qCol = nextCol // cols
            modCol = nextCol % cols
            #print("3next row is " + str(nextRow) + " and its mod is " + str(modRow))
            #print("3next col is " + str(nextCol) + " and its mod is " + str(modCol))
            value = ( int(lines[modRow][modCol]) + (qRow + qCol) ) % 9
            if value == 0:
                value = 9
            #print("value is: " + str(value))
            next_node = (nextRow,nextCol)
            edges.append((current_node,next_node,value))
        nextRow = row
        if col - 1 >= 0:
            nextCol = col - 1
            qRow = nextRow // rows
            modRow = nextRow % rows
            qCol = nextCol // cols
            modCol = nextCol % cols
            #print("4next row is " + str(nextRow) + " and its mod is " + str(modRow))
            #print("4next col is " + str(nextCol) + " and its mod is " + str(modCol))
            value = ( int(lines[modRow][modCol]) + (qRow + qCol) ) % 9
            if value == 0:
                value = 9
            #print("value is: " + str(value))
            next_node = (nextRow,nextCol)
            edges.append((current_node,next_node,value))

#print(shortest_path)
print(dijkstra(edges, startNode, lastNode)[0])
#print(previous_nodes)

stop = timeit.default_timer()

print('Time: ', stop - start)  