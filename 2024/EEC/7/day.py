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

def getChariots(lines):
    chariots = {}
    for line in lines:
        chariotName = line.strip().split(":")[0]
        orders = line.strip().split(":")[1].split(",")
        orders = orders + [10]
        chariots[chariotName] = orders
    return chariots

#Solution to Part 1
def part1(lines):
    chariots = getChariots(lines)
    segment = 1
    totalEssence = {}
    for chariot in chariots:
        totalEssence[chariot] = 0
    while segment <= 10:
        for chariot in chariots:
            index = ((segment-1) % (len(chariots[chariot]) - 1))
            symbol = chariots[chariot][index]
            if symbol == '+':
                chariots[chariot][-1] += 1
            elif symbol == '-':
                chariots[chariot][-1] -= 1
            totalEssence[chariot] += chariots[chariot][-1] 
            printtest("Segment " + str(segment) + " and chariot " + chariot + " collects " + str(chariots[chariot][-1]) + " essence.")
        segment += 1
    
    sortedEssence = dict(sorted(totalEssence.items(), key=lambda item: item[1], reverse=True ))
    output = ""
    for key in sortedEssence:
        output += key
    print("The final ranking is: " + output)

def getTrack(lines):
    track = []
    for sy in lines[0].strip():
        track += sy
    for line in lines[1:-1]:
        track += line.strip()[-1]
    for sy in reversed(lines[-1].strip()):
        track += sy
    for line in reversed(lines[1:-1]):
        track += line.strip()[0]
    track = track[1:] + ["S"]
    return track

def getRanking(totalEssence):
    sortedEssence = dict(sorted(totalEssence.items(), key=lambda item: item[1], reverse=True ))
    print(sortedEssence)
    output = ""
    for key in sortedEssence:
        output += key
    return output       

#Solution to Part 2
def part2(lines):
    chariots = getChariots(lines)
    if args.test == "true":
        lines2 = getLines("test"+args.part+args.part+".txt")
    else:
        lines2 = getLines("input"+args.part+args.part+".txt")
    track = getTrack(lines2)
    print(track)
    loops = 1
    totalEssence = {}
    for chariot in chariots:
        totalEssence[chariot] = 0
    while loops <= 10:
        printtest("Loop: " + str(loops))
        for segment in range(0,len(track)):
            for chariot in chariots:
                index = ((segment) % (len(chariots[chariot]) - 1))
                symbol = chariots[chariot][index]
                if track[segment]=="+" or track[segment]=="-":
                    symbol = track[segment]
                if symbol == '+':
                    chariots[chariot][-1] += 1
                elif symbol == '-':
                    chariots[chariot][-1] -= 1
                totalEssence[chariot] += chariots[chariot][-1] 
                printtest("Segment " + str(segment) + " and chariot " + chariot + " collects " + str(chariots[chariot][-1]) + " essence.")
        
        print("Ranking at loop " + str(loops) + " is: " + getRanking(totalEssence))
        loops += 1
    
   
    print("The final ranking is: " + getRanking(totalEssence))

#Solution to Part 3
def part3(lines):

    print(lines)

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