file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/9/input1.txt', 'r')
lines = file1.readlines()

surface = []
for line in lines:
    row = []
    for number in line.replace("\n",""):
        row.append(int(number))
    surface.append(row)

minCoordinates = []
for r in range(0,len(surface)):
    for c in range(0,len(surface[0])):
        min = True
        if r-1 >= 0:
            if surface[r-1][c] <= surface[r][c]:
                min = False
        if r+1 < len(surface):
            if surface[r+1][c] <= surface[r][c]:  
                min = False  
        if c-1 >= 0:
            if surface[r][c-1] <= surface[r][c]:
                min = False
        if c+1 < len(surface[0]):
            if surface[r][c+1] <= surface[r][c]:  
                min = False  
        if min == True:
            minCoordinates.append([r,c])
print("The coordinates of the min points are: " + str(minCoordinates))

def get_smaller_neighbour_coordinates(minX, minY, surface):
    smaller_neighbours = []
    if minX-1 >= 0:
        if surface[minX-1][minY] > surface[minX][minY] and surface[minX-1][minY] < 9:
                smaller_neighbours.append([minX-1,minY])
    if minX+1 < len(surface):
        if surface[minX+1][minY] > surface[minX][minY] and surface[minX+1][minY] < 9:  
                smaller_neighbours.append([minX+1,minY])
    if minY-1 >= 0:
        if surface[minX][minY-1] > surface[minX][minY] and surface[minX][minY-1] < 9:
                smaller_neighbours.append([minX,minY-1])
    if minY+1 < len(surface[0]):
        if surface[minX][minY+1] > surface[minX][minY] and surface[minX][minY+1] < 9:  
                smaller_neighbours.append([minX,minY+1])
    return smaller_neighbours

largestBasins = [0,0,0]
for minPoint in minCoordinates:
    print("Calculating basin for point " + str(minPoint))
    basin = [minPoint]
    neighbours_to_analyze = [minPoint]
    while len(neighbours_to_analyze) > 0:
        #print(neighbours_to_analyze)
        temp_neighbours_to_analyze = []
        for neighbour in neighbours_to_analyze:
            smaller_neigbours = get_smaller_neighbour_coordinates(neighbour[0],neighbour[1],surface)
            for smaller_neigbour in smaller_neigbours:
                if smaller_neigbour not in basin:
                    basin.append(smaller_neigbour)
                    temp_neighbours_to_analyze.append(smaller_neigbour)
        neighbours_to_analyze = temp_neighbours_to_analyze
    print("The basin size is:  " + str(len(basin)))       
    largestBasins.append(len(basin))
    largestBasins = sorted(largestBasins, reverse=True)[0:3]

print("Largest Basins sizes are: " + str(largestBasins))
mult = largestBasins[0] * largestBasins[1] * largestBasins[2]
print("Multiplication result: " + str(mult))
        


