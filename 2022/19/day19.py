import os
from pathlib import Path
from copy import deepcopy
p = Path(__file__).with_name('test.txt')

f = p.open('r')
lines = f.readlines()

blueprints = []
class Blueprint(object):
    def __init__(self, id):
        self.id = id
        self.robots = []
    
    def add_robot(self, robot):
        self.robots.append(robot)

class Robot(object):
    def __init__(self, robot_name, ore_cost, clay_cost, obsidian_cost):
        self.robot_name = robot_name
        self.ore_cost = ore_cost
        self.obsidian_cost = obsidian_cost
        self.clay_cost = clay_cost

def get_robot_from_line(line):
    robot_name = line.split(" ")[1]
    ore_cost, clay_cost, obsidian_cost = 0,0,0
    if "ore" in line.split("robot")[1]:
        ore_cost = int(line.split("robot")[1].split("ore")[0].strip().split(" ")[-1])
    if "clay" in line.split("robot")[1]:
        clay_cost = int(line.split("robot")[1].split("clay")[0].strip().split(" ")[-1])
    if "obsidian" in line.split("robot")[1]:
        obsidian_cost = int(line.split("robot")[1].split("obsidian")[0].strip().split(" ")[-1])
    #print(f'  Robot {robot_name} costs {ore_cost} ore, {clay_cost} clay and {obsidian_cost} obsidian.')
    
    return Robot(robot_name, ore_cost, clay_cost, obsidian_cost)

def parse_input(input):
    blueprint = Blueprint(-1)
    for i,line in enumerate(input):
        line = line.strip()
        if i%6==0:
            id = int(line.split(" ")[1].split(":")[0])
            blueprint = Blueprint(id)
            #print(f'Blueprint {id}')
        elif i%6<=4:
            robot = get_robot_from_line(line)
            blueprint.add_robot(robot)
            if i%6==4:
                blueprints.append(blueprint)

def is_buyable(resources, robot: Robot):
    if robot.ore_cost <= resources[0] and robot.clay_cost <= resources[1] and robot.obsidian_cost <= resources[2]:
        return True
    return False

def get_buyable_robots(resources, robots):
    buyable_robots = []
    for i, robot in enumerate(robots):
        if is_buyable(resources,robot):
            buyable_robots.append(robot)
    return buyable_robots

def buy_robot(resources, robot: Robot):
    resources = (resources[0]-robot.ore_cost,resources[1]-robot.clay_cost,resources[2]-robot.obsidian_cost,resources[3])
    return resources

def robots_work(resources,current_robots):
    resources = (resources[0]+current_robots["ore"], resources[1]+current_robots["clay"], resources[2]+current_robots["obsidian"] ,resources[3]+current_robots["geode"])

    return resources

def get_maxes(robots):
    max_ore,max_clay,max_obsidian = 0,0,0
    for robot in robots:
        if robot.ore_cost > max_ore:
            max_ore = robot.ore_cost
        if robot.clay_cost > max_clay:
            max_clay = robot.clay_cost
        if robot.obsidian_cost > max_obsidian:
            max_obsidian = robot.obsidian_cost
    return max_ore, max_clay, max_obsidian


def sim_minute(current_minute, resources, current_robots, blueprint, largest_geode_count):
    ### if > 24 minutes, end simulation ###
    max_ore, max_clay, max_obsidian = get_maxes(blueprint.robots)
    if current_minute == 24:
        return largest_geode_count
    new_resources = deepcopy(resources)
    new_resources = robots_work(new_resources,current_robots)
    buyable_robots = get_buyable_robots(resources,blueprint.robots)

    if new_resources[3] > largest_geode_count[0]:
        print(f'YEEEES GEODES at minute {current_minute} and resources {new_resources} and current bots: {current_robots}')
        largest_geode_count[0] = new_resources[3]
        print(largest_geode_count[0])
    
    s = ""
    for robot in buyable_robots:
        s+=robot.robot_name + ","
    
    #print(f'We can buy 1 {len(buyable_robots)} robots!')
    for robot in buyable_robots:
        if (robot.robot_name == "ore" and current_robots["ore"] < max_ore) or (robot.robot_name == "clay" and current_robots["clay"] < max_clay) or (robot.robot_name == "obsidian" and current_robots["obsidian"] < max_obsidian) or robot.robot_name=="geode":
            print(f'Minute: {current_minute} --- Resources: {new_resources} --- Working Bots: {current_robots} --- Can buy: {s} --- will buy: {robot.robot_name}')
            new_resources = buy_robot(new_resources, robot)
            new_robots = current_robots.copy()
            new_robots[robot.robot_name] += 1
            #print(f'We can buy 1 {robot.robot_name} robot!')
            sim_minute(current_minute+1, new_resources, new_robots, blueprint, largest_geode_count)
    new_robots = current_robots.copy()
    new_resources = deepcopy(new_resources)
    sim_minute(current_minute+1, new_resources, new_robots, blueprint, largest_geode_count) ###choice of not buying any robot

parse_input(lines)
existing_robots = {"ore":1,"clay":0,"obsidian":0,"geode":0}
resources = (0,0,0,0)

blueprint = blueprints[0]
largest_geode_count = [0]
sim_minute(1,resources, existing_robots, blueprint, largest_geode_count)

print(resources)