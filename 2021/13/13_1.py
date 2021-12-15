from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))

def get_maxes(points):
    xmax=0
    ymax=0
    for point in points:
        if point[0] > xmax:
            xmax = point[0]
        if point[1] > ymax:
            ymax = point[1]

    return xmax,ymax

def print_points(points):
    xmax,ymax = get_maxes(points)
    for y in range(0,ymax+1):
        line = ""
        for x in range(0,xmax+1):
            if (x,y) in points:
                line += "#"
            else:
                line += " "
        print(line)

with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

points = []
folds = []
for line in lines:
    if "," in line:
        points.append((int(line.split(",")[0]),int(line.split(",")[1])))
    if "=" in line:
        interestingPart = line.split(" ")[2]
        folds.append((interestingPart.split("=")[0],int(interestingPart.split("=")[1])))

#print("Folds:" + str(folds))
#print("Fancy points: ")
#print_points(points)

for fold in folds[0:1]:
    newPoints = []
    xmax, ymax = get_maxes(points)
    if fold[0] == "x":
        print("Folding to the left on x=" + str(fold[1]))
        for point in points:
            if point[0] < fold[1]:
                if point not in newPoints:
                    newPoints.append(point)
            else:
                delta = point[0] - fold[1]
                newX = fold[1] - delta
                if (newX,point[1]) not in newPoints:
                    newPoints.append((newX,point[1]))
    elif fold[0] == "y":
        print("Folding up on y=" + str(fold[1]))
        for point in points:
            if point[1] < fold[1]:
                if point not in newPoints:
                    newPoints.append(point)
            else:
                delta = point[1] - fold[1]
                newY = fold[1] - delta
                if (point[0],newY) not in newPoints:
                    newPoints.append((point[0],newY))
        #fold the paper up
    #print_points(newPoints)
    print("There are " + str(len(newPoints)) + " visible dots.")
    points = newPoints.copy()

print("Folding complete")
print_points(points)
stop = timeit.default_timer()

print('Time: ', stop - start)  