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

def printAnswer(path):
    resp = ""
    for node in path:
        if node.startswith("@"):
            resp += "@"
        else:
            resp += node
    return resp

def printAnswer2(path):
    resp = ""
    for node in path:
        resp += node[0]
    return resp

def buildGraph(lines):
    graph = {}
    apple_index = 1
    apples = []
    for line in lines:
        source = line.strip().split(":")[0]
        paths = []
        for item in line.strip().split(":")[1].split(","):
            if item == '@':
                paths += [item + str(apple_index)]
                apples += [item + str(apple_index)]
                apple_index+=1
            else:
                paths += [item]
        graph[source] = paths
    return graph, apples

def find_path(graph,start,end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return None

#Solution to Part 1
def part1(lines):
    graph, apples = buildGraph(lines)
    printtest(graph)
    paths = []
    for apple in apples:
        paths += [find_path(graph, "RR", apple)]
    printtest("All possible paths are: " + str(paths))
    paths_grouped_by_length = {}
    for path in paths:
        if len(path) not in paths_grouped_by_length:
            paths_grouped_by_length[len(path)] = [path]
        else:
            paths_grouped_by_length[len(path)] += [path]
    printtest(paths_grouped_by_length)
    for length in paths_grouped_by_length:
        if len(paths_grouped_by_length[length]) == 1:
            printtest(paths_grouped_by_length[length])
            print("The path to the most powerfull apple is " + printAnswer(paths_grouped_by_length[length][0]))

#Solution to Part 2
def part2(lines):
    printtest(printAnswer2(["RR","ABAB","CDCD","EFEF","ROLO","@2"]))
    graph, apples = buildGraph(lines)
    printtest(graph)
    paths = []
    for apple in apples:
        paths += [find_path(graph, "RR", apple)]
    printtest("All possible paths are: " + str(paths))
    paths_grouped_by_length = {}
    for path in paths:
        if len(path) not in paths_grouped_by_length:
            paths_grouped_by_length[len(path)] = [path]
        else:
            paths_grouped_by_length[len(path)] += [path]
    for length in paths_grouped_by_length:
        if len(paths_grouped_by_length[length]) == 1:
            printtest(paths_grouped_by_length[length])
            print("The path to the most powerfull apple is " + printAnswer2(paths_grouped_by_length[length][0]))

#Solution to Part 3
def part3(lines):
    printtest(printAnswer2(["RR","ABAB","CDCD","EFEF","ROLO","@2"]))
    graph, apples = buildGraph(lines)
    printtest(graph)
    paths = []
    printtest(apples)
    for apple in apples:
        paths += [find_path(graph, "RR", apple)]
    printtest("All possible paths are: " + str(paths))
    paths_grouped_by_length = {}
    for path in paths:
        if len(path) not in paths_grouped_by_length:
            paths_grouped_by_length[len(path)] = [path]
        else:
            paths_grouped_by_length[len(path)] += [path]
    for length in paths_grouped_by_length:
        if len(paths_grouped_by_length[length]) == 1:
            printtest(paths_grouped_by_length[length])
            print("The path to the most powerfull apple is " + printAnswer2(paths_grouped_by_length[length][0]))
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