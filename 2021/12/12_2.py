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
def check_for_flashes(connections, current_point, already_visited, smallVisit):
    possible_positions = []
    smaller_caves = []
    for connection in connections:
        if current_point in connection:
            dest_point = get_other_point(connection,current_point)
            if dest_point == dest_point.upper():
                possible_positions.append(dest_point)
            elif dest_point not in already_visited:
                possible_positions.append(dest_point)
            elif dest_point == dest_point == dest_point.lower() and dest_point in already_visited and smallVisit == False and dest_point!="end" and dest_point != "start":
                possible_positions.append(dest_point)
                #print(dest_point + " has already been visited. Adding again because smallVisit is " + str(smallVisit))
                smaller_caves.append(dest_point)
    if len(possible_positions) != 0:
        for possible_position in possible_positions:
            new_already_visited = already_visited.copy()
            new_already_visited.append(possible_position)
            if possible_position == "end":
                journeys.append(new_already_visited)
            else:
                #print("the smaller caves are " + str(smaller_caves) + " and the possible position is " + possible_position)
                if possible_position in smaller_caves and smallVisit == False:
                    #print("Its a small cave")
                    check_for_flashes(connections, possible_position, new_already_visited, True)
                else:
                    check_for_flashes(connections, possible_position, new_already_visited, smallVisit)

     

trips = []
print("Lets start!")
check_for_flashes(connections,"start",["start"],False)
#print(journeys)
print("There are " + str(len(journeys)) + " possible journeys")

stop = timeit.default_timer()

print('Time: ', stop - start)  
        