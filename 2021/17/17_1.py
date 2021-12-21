from os import path
import timeit

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input.txt"))
with open(filepath, "r") as fp:
    target_str = [line.rstrip() for line in fp.readlines()][0]

def simulate_trajectory(x_v, y_v, target):
    x_pos = 0
    y_pos = 0
    max_y_pos = 0
    target_reached = False
    while ( (x_v >= 0 and x_pos < target["x2"]) or (x_v <= 0 and x_pos > target["x1"]) ) and y_pos > target["y1"]:
        
        x_pos += x_v
        y_pos += y_v
        if y_pos > max_y_pos:
            max_y_pos = y_pos
        if (x_pos >= target["x1"] and x_pos <= target["x2"]) and (y_pos >= target["y1"] and y_pos <= target["y2"]):
            target_reached = True
            #print("We arrived to the target zone!")
            break

        #drag
        if x_v > 0:
            x_v-=1
        elif x_v > 0:
            x_v+=1

        #gravitiy
        y_v -= 1
    return max_y_pos, target_reached

x_values = sorted(list(map(int,target_str.split("=")[1].split(",")[0].split(".."))))
y_values = sorted(list(map(int,target_str.split("=")[2].split(".."))))

target = {"x1" : x_values[0], "x2" : x_values[1], "y1" : y_values[0], "y2": y_values[1]}

max_y_pos = {"y":0,"x_v":0,"y_v":0}

for x in range(-99,target["x2"]):
    y = 0
    for y in range (1,99):
        #print("Trying init_x_v = " + str(x) + " and init_y_v=" + str(y))
        init_x_v = x
        init_y_v = y
        y_pos, target_reached = simulate_trajectory(init_x_v, init_y_v, target)
        if target_reached and (y_pos > max_y_pos["y"]):
            max_y_pos["y"] = y_pos
            max_y_pos["x_v"] = init_x_v
            max_y_pos["y_v"] = init_y_v
        y += 1
print("The maximum achieved position was " + str(max_y_pos["y"]) + " with an initial speed of x_v=" + str(max_y_pos["x_v"]) + " and y_v=" + str(max_y_pos["y_v"]))



print(simulate_trajectory(19,43,target))



stop = timeit.default_timer()

print('Time: ', stop - start)  