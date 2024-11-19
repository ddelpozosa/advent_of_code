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

def parseInput(lines):
    population = {}
    reproduction = {}
    for line in lines:
        dad = line.strip().split(":")[0]
        population[dad] = 0
        reproduction[dad] = []
        reproduction[dad] = line.strip().split(":")[1].split(",")

    return population,reproduction

def addGeneration(population,reproduction):
    nextGen = dict(population)
    for dadType in population:
        kids = reproduction[dadType]
        for kid in kids:
            nextGen[kid] += population[dadType]
        nextGen[dadType] -= population[dadType]
    return nextGen

def countPopulation(population):
    count = 0
    for dadType in population:
        count += population[dadType]
    return count

#Solution to Part 1
def part1(lines):
    population,reproduction = parseInput(lines)
    population["A"] = 1
    days = 1
    while days <=4:
        population = addGeneration(population,reproduction)
        printtest("After " + str(days) +" days, there is a population of: " + str(countPopulation(population)))
        days += 1
    print("After " + str(days-1) +" days, there is a population of: " + str(countPopulation(population)))

#Solution to Part 2
def part2(lines):
    population,reproduction = parseInput(lines)
    population["Z"] = 1
    days = 1
    while days <=10:
        population = addGeneration(population,reproduction)
        printtest("After " + str(days) +" days, there is a population of: " + str(countPopulation(population)))
        days += 1
    print("After " + str(days-1) +" days, there is a population of: " + str(countPopulation(population)))

#Solution to Part 3
def part3(lines):
    populationOrg,reproduction = parseInput(lines)
    populations = []
    for dad in reproduction:
        population = dict(populationOrg)
        population[dad] = 1
        days = 1
        while days <=20:
            population = addGeneration(population,reproduction)
            days += 1
        printtest("After " + str(days-1) +" days for " + dad +", there is a population of: " + str(countPopulation(population)))
        populations += [countPopulation(population)]
    print("The population difference is: " + str(max(populations)-min(populations)))

if __name__ == "__main__":
    if args.test == "true":
        lines = getLines("test"+args.part+".txt")
    else:
        lines = getLines("input"+args.part+".txt")
    if args.part == "1":
        part1(lines)
    elif args.part == "2":
        part2(lines)
    elif args.part == "3":
        part3(lines)
    else:
        print("Error: Part number invalid: " + args.part)