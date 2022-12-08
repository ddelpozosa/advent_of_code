import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

grid = []
for line in lines:
    grid_line = []
    for number in line.strip():
        grid_line.append(int(number))
    grid.append(grid_line)

### Part 1 ###
def checkIfVisible(grid, i_tree, j_tree):
    ### Check if corner ###
    if i_tree == 0 or j_tree == 0 or i_tree == len(grid)-1 or j_tree == len(grid[0])-1:
        #print(f'[{i_tree},{j_tree}] is an edge and therefore it is visible.')
        return True

    ### Visible from Top ###
    visible = True
    for i in range(i_tree-1,-1,-1):
        if grid[i][j_tree] >= grid[i_tree][j_tree]:
            visible = False
    if visible == True:
        #print(f'[{i_tree},{j_tree}] is visible from the top.')
        return visible

    ### Visible from Left ###
    visible = True
    for j in range(j_tree-1,-1,-1):
        if grid[i_tree][j] >= grid[i_tree][j_tree]:
            visible = False
    if visible == True:
        #print(f'[{i_tree},{j_tree}] is visible from the left.')
        return visible

    ### Visible from Bottom ###
    visible = True
    for i in range(i_tree+1,len(grid)):
        if grid[i][j_tree] >= grid[i_tree][j_tree]:
            visible = False
    if visible == True:
        #print(f'[{i_tree},{j_tree}] is visible from the bottom.')
        return visible

    ### Visible from Right ###
    visible = True
    for j in range(j_tree+1,len(grid[0])):
        if grid[i_tree][j] >= grid[i_tree][j_tree]:
            visible = False
    if visible == True:
        #print(f'[{i_tree},{j_tree}] is visible from the right.')
        return visible
    return visible

visibleTrees = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if checkIfVisible(grid,i,j) == True:
            visibleTrees += 1

print(f'There are {visibleTrees} visible trees in the grid.')

### Part 2 ###

def getScenicScore(grid, i_tree, j_tree):

    scenicScore = 0
    ### Check if corner ###
    if i_tree == 0 or j_tree == 0 or i_tree == len(grid)-1 or j_tree == len(grid[0])-1:
        #print(f'[{i_tree},{j_tree}] is an edge and therefore it is visible.')
        return scenicScore
    
    ### Top score ###
    scoreTop = 0
    for i in range(i_tree-1,-1,-1):
        scoreTop += 1
        if grid[i][j_tree] >= grid[i_tree][j_tree]:
            break
    
    scoreLeft = 0
    for j in range(j_tree-1,-1,-1):
        scoreLeft += 1
        if grid[i_tree][j] >= grid[i_tree][j_tree]:
            break

    scoreBottom = 0
    for i in range(i_tree+1,len(grid)):
        scoreBottom += 1
        if grid[i][j_tree] >= grid[i_tree][j_tree]:
            break

    scoreRight = 0
    for j in range(j_tree+1,len(grid[0])):
        scoreRight += 1
        if grid[i_tree][j] >= grid[i_tree][j_tree]:
            break
    
    scenicScore = scoreTop * scoreLeft * scoreBottom * scoreRight
    return scenicScore

highestScenicScore = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        scenicScore = getScenicScore(grid,i,j)
        if scenicScore > highestScenicScore:
            highestScenicScore = scenicScore

print(f'The tree with the highest scenic score has the following score: {highestScenicScore}')