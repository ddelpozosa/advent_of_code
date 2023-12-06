import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", default = "false", help="Use test file")
parser.add_argument("-p", "--part", dest="part", default = "1", help= "Problem part to run")
args = parser.parse_args()

def printtest(text):
    if args.test == "true":
        print(text)

def getLines(file):
    p = Path(__file__).with_name(file)
    f = p.open('r')
    lines = f.readlines()
    return lines

class Map:
    def __init__(self, destStart, sourceStart, range):
        self.destStart = destStart
        self.sourceStart = sourceStart
        self.range = range
    def __str__(self):
        return f"Dest: {self.destStart}, Source: {self.sourceStart}, Length: {self.range}"

class MapArray:
    def __init__(self, source, dest, maps):
        self.source = source
        self.dest = dest
        self.maps = maps
    def addMap(self, map):
        self.maps.append(map)
    def __str__(self):
        return f"Source: {self.source} -- Dest: {self.dest}"

def getSeeds1(lines):
    seeds = []
    for number in lines[0].split(": ")[1].split(" "):
        seeds.append(int(number))
    return seeds

def getSeeds2Smart(lines):
    seeds = []
    start = -1
    for i, number in enumerate(lines[0].split(": ")[1].split(" ")):
        if i%2 == 0:
            start = int(number)
        else:
           seeds.append((start,int(number)))
    return seeds

def getSeeds2(lines):
    seeds = []
    for i, number in enumerate(lines[0].split(": ")[1].split(" ")):
        if i%2 == 0:
            seeds.append(int(number))
        else:
            for i in range(seeds[-1] + 1, seeds[-1] + int(number),  1):
                seeds.append(i)
    return seeds

def parse(lines):
    maps = []
    tempMap = MapArray("","",[])
    for line in lines[1:]:
        if line.strip()=="":
            if tempMap.dest != "":
                maps.append(tempMap)
            tempMap = MapArray("","",[])
        elif line.split(" ")[1].strip()=="map:":
            tempMap.source=line.split(" ")[0].split("-")[0]
            tempMap.dest=line.split(" ")[0].split("-")[2]
        else:
            mapRow = []
            for number in line.strip().split(" "):
                mapRow.append(int(number))
            map = Map(mapRow[0],mapRow[1],mapRow[2])
            tempMap.addMap(map)
    maps.append(tempMap)
    return maps

def getLocation(source, currentLocation, maps):
    dest = ""
    if(source == "location"):
        return currentLocation
    for mapArray in maps:
        if mapArray.source == source:
            dest = mapArray.dest
            loc = -1
            for map in mapArray.maps:
                if currentLocation >= map.sourceStart and currentLocation < (map.sourceStart+map.range):
                    loc = currentLocation + (map.destStart - map.sourceStart)
            if loc == -1:
                loc = currentLocation
            return getLocation(dest, loc, maps)

    return -1

def getLocation2(source, currentTuple, maps):
    dest = ""
    if(source == "location"):
        return currentTuple
    for mapArray in maps:
        if mapArray.source == source:
            dest = mapArray.dest
            loc = -1
            for map in mapArray.maps:
                if currentTuple[0] >= map.sourceStart and (currentTuple[0] + currentTuple[1] - 1) < (map.sourceStart+map.range):
                    print(currentTuple)
            if loc == -1:
                loc = currentTuple
            return getLocation(dest, loc, maps)


    return -1

#Solution to Part 1
def part1(lines):
    seeds = getSeeds1(lines)
    maps = parse(lines)
    printtest("Seeds: " + str(seeds))
    for map in maps:
        printtest(map)
    
    lowest = 9999999999999999
    for seed in seeds:
        location = getLocation("seed", seed, maps)
        if location < lowest:
            lowest = location
        printtest("Seed " + str(seed) + " ends in location " + str(location))
    
    print("The lowest location number is " + str(lowest))

#Solution to Part 2
def part2(lines):
    seedTuple = getSeeds2Smart(lines)   
    for tuple in seedTuple:
        print(tuple)
    
    print("The lowest location number is ")

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test.txt")
    else:
        lines = getLines("input.txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    else:
        print("Error: Part number invalid: " + args.part)