from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 295, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 1068781}
]

def parse_1(data):
    lines = parse_lines(data)
    timestamp = int(lines[0])
    bus_ids = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    return timestamp, bus_ids

def get_time_to_next_arrival(timestamp, bus_id):
    next_arrival = bus_id * ((timestamp // bus_id) + 1) 
    return next_arrival - timestamp

def part1(data):
    timestamp, bus_ids = parse_1(data)
    arrivals = []
    for bus_id in bus_ids:
        arrivals.append((get_time_to_next_arrival(timestamp, bus_id), bus_id))
    
    time, bus_id = min(arrivals)
    return time * bus_id

def lcm(a, b):
    #Least common multiple
    from math import gcd
    return abs(a * b) // gcd(a, b)

# bus departs every bus_id minutes with an offset
# (t + offset) % bus_id = 0

def parse_2(data):
    lines = parse_lines(data)
    bus_departures = []
    for i, id in enumerate(lines[1].split(',')):
        if id != 'x':
            bus_departures.append((i,(int(id))))
    return bus_departures

def part2(data):
    bus_departures = parse_2(data)
    
    t = 0
    step = 1
    debug(bus_departures)
    for offset, bus_id in bus_departures:
        # Find first t that satisfies this bus constraint
        debug("Step: ",step)
        while (t + offset) % bus_id != 0:
            t += step
        # Once satisfied, future solutions must preserve ALL previous constraints
        # Step by LCM to maintain periodicity (reduces to multiplication if coprime)
        step = lcm(step, bus_id)
    
    return t
