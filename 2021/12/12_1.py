from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input1.txt"))
octopuses = []
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

connections = []    
for line in lines:
    connections.append([line.split("-")[0],line.split("-")[1]])

def get_other_point(connection,current_point):
    for point in connection:
        if point != current_point:
            return point

journeys = []
def find_possible_journeys(connections, current_point, already_visited):
    possible_positions = []
    for connection in connections:
        if current_point in connection:
            dest_point = get_other_point(connection,current_point)
            if dest_point == dest_point.upper():
                possible_positions.append(dest_point)
            elif dest_point not in already_visited:
                possible_positions.append(dest_point)
    if len(possible_positions) != 0:
        for possible_position in possible_positions:
            new_already_visited = already_visited.copy()
            new_already_visited.append(possible_position)
            if possible_position == "end":
                journeys.append(new_already_visited)
            else:
                find_possible_journeys(connections, possible_position, new_already_visited)

     

trips = []
print("Lets start!")
find_possible_journeys(connections,"start",["start"])
#print(journeys)
print("There are " + str(len(journeys)) + " possible journeys")

stop = timeit.default_timer()

print('Time: ', stop - start)  
        