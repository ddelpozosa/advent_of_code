import argparse
from pathlib import Path
import sys
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

def parse(lines):
    mirrors = []
    for line in lines:
        l = []
        for char in line.strip():
            l.append(char)
        mirrors.append(l)
    energies = []
    for line in mirrors:
        l = []
        for char in line:
            l.append(0)
        energies.append(l)
    return mirrors, energies

def print_table(table):
    for line in table:
        l = ""
        for char in line:
            l+=str(char)
        printtest(l)

def print_energies(energies):
    for line in energies:
        l = ""
        for i in line:
            if i > 0:
                l+="#"
            else:
                l+="."
        printtest(l)

def count_energies(energies):
    total = 0
    for line in energies:
        for i in line:
            if i > 0:
                total += 1
    return total


def get_next_dir(curx, cury, mirrors, dir):
    match dir:
        case "down":
            if cury+1 < len(mirrors):
                return curx, cury+1
        case "up":
            if cury-1 >= 0:
                return curx, cury-1
        case "left":
            if curx-1 >= 0:
                return curx-1, cury
        case "right":
            if curx+1 < len(mirrors[0]):
                return curx+1, cury
    return -1,-1

directions = []
# dir = [down, top, left, right]
def travel_through(curx, cury, mirrors, energies, dir):
    s = str(cury) + str(curx) + dir
    print(s)
    if cury != -1 and curx != -1 and s not in directions:
        #printtest("I am on " + mirrors[cury][curx] +" and I am going " + dir)
        #current field is energized:
        cur_field = mirrors[cury][curx]
        energies[cury][curx] +=1
        directions.append(s)
        
        nextx1,nexty1 = -1, -1
        nextx2,nexty2 = -1, -1
        match cur_field:
            case ".":
                nextx1,nexty1 = get_next_dir(curx, cury, mirrors, dir)
                #printtest("cur field is: " + str(curx) + "," + str(cury))
               # printtest("next field is: " + str(nextx) + "," + str(nexty))
                printtest("I am on . and I will go " + dir + " next")
                #travel_through(nextx,nexty, mirrors, energies, dir)
            case "|":
                #print("aaaaa")
                nextx1,nexty1 = get_next_dir(curx, cury, mirrors, "up")
                printtest("I am on | and I will go up next")
                #travel_through(nextx,nexty, mirrors, energies, "up")
                nextx2,nexty2 = get_next_dir(curx, cury,  mirrors, "down")
                printtest("I am on | and I will go down next")
                #travel_through(nextx,nexty, mirrors, energies, "down")
            case "-":
                nextx1,nexty1 = get_next_dir(curx, cury, mirrors, "left")
                #travel_through(nextx,nexty, mirrors, energies, "left")
                
                nextx2,nexty2 = get_next_dir(curx, cury, mirrors, "right")
                printtest("I am on - and I will go right next to: " + str(nextx) + ", " + str(nexty) + " which is " + mirrors[nexty][nextx])
                #travel_through(nextx,nexty, mirrors, energies, "right")
            case "/":
                newdir = ""
                if dir == "down":
                    newdir = "left"
                elif dir == "up":
                    newdir = "right"
                elif dir == "right":
                    newdir = "up"
                elif dir == "left":
                    newdir = "down"
                printtest("I am on / and I will go " + newdir + " next")
                nextx1,nexty1 = get_next_dir(curx, cury, mirrors, newdir)
                
                #travel_through(nextx,nexty, mirrors, energies, newdir)
            case "\\":
                newdir = ""
                if dir == "down":
                    newdir = "right"
                elif dir == "up":
                    newdir = "left"
                elif dir == "right":
                    newdir = "down"
                elif dir == "left":
                    newdir = "up"
                nextx1,nexty1 = get_next_dir(curx, cury, mirrors, newdir)
                printtest("I am on \\ and I will go " + newdir + " next to: " + str(nextx) + ", " + str(nexty) + " which is " + mirrors[nexty][nextx])
                #travel_through(nextx,nexty, mirrors, energies, newdir)
    return nextx1, nexty1, nextx2, nexty2

def add_places(next_places, nextx1, nexty1, nextx2, nexty2):
    if nextx1 != 1 and nexty1 != -1:
        next_places.append((nextx1,nexty2))
    if nextx2 != 1 and nexty2 != -1:
        next_places.append((nextx2,nexty2))
    return next_places
#Solution to Part 1
def part1(lines):
    mirrors, energies = parse(lines)
    end = False
    nextx1, nexty1, nextx2, nexty2 = travel_through(0, 0, mirrors, energies, "right")
    next_places = []
    next_places = add_places(next_places,nextx1, nexty1, nextx2, nexty2)
    print(nextx1)
    while end == False:
        if len(next_places) == 0:
            end == True
        for place in next_places:
            nextx1, nexty1, nextx2, nexty2 = travel_through(place[0],place[1], mirrors, energies, "right")
            add_places(next_places,nextx1, nexty1, nextx2, nexty2)
       
    print_energies(energies)
    total = count_energies(energies)
    print("The total number of energized fields is: " + str(total))

#Solution to Part 2
def part2(lines):
        
    print(lines)

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