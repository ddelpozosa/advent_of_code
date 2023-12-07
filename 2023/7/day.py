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
values2 = {
        "J": 2,
        "2": 3,
        "3": 4,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "T": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

def addToHigherType(types, cardCount):
    forbidden = ""
    if types[cardCount["J"]] == 1:
        forbidden = cardCount["J"]
        #print(str(forbidden) + " is forbidden")
    for type in types:
        if types[type]!=0 and type != forbidden:
            types[type+cardCount["J"]] += 1
            types[type] -= 1
            types[cardCount["J"]] -= 1
            return types
    return types

def getHandScore2(hand):
    cardCount = dict((i, hand.count(i)) for i in hand)
    types = {5:0,4:0,3:0,2:0,1:0}
    for i in cardCount:
        if cardCount[i] in types:
            types[cardCount[i]]+=1
    score = 0
    printtest(hand)
    printtest(types)

    if "J" in cardCount:
        types = addToHigherType(types,cardCount)
    printtest(types)
    if types[5] == 1:
        score += 8*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is pentakill")
    elif types[4] == 1:
        score += 7*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is four")
    elif types[3] >= 1 and types[2] >= 1:
        score += 6*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is full house")
    elif types[3] >= 1:
        score += 5*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is trio")
    elif types[2] >= 2:
        score += 4*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is two pair")
    elif types[2] == 1:
        score += 3*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is one pair")
    else:
        score += 2*pow(10,10)
        if "J" in cardCount:
            printtest(hand + " is high card")
    return score

def getCardsScore2(hand):
    score = 0
    for i in range(0,5):
        score += values2[hand[i]]*pow(10,2*(4-i))
    return score

def getScore2(line):
    hand = line.split(" ")[0]
    bid = int(line.split(" ")[1].strip())
    
    score = getHandScore2(hand)
    score += getCardsScore2(hand)

    return score, bid

def getHandScore(hand):
    
    cardCount = dict((i, hand.count(i)) for i in hand)
    types = {5:0,4:0,3:0,2:0,1:0}
    score = 0
    for i in cardCount:
        if cardCount[i] in types:
            types[cardCount[i]]+=1
    if types[5] == 1:
        score += 8*pow(10,10)
    elif types[4] == 1:
        score += 7*pow(10,10)
    elif types[3] == 1 and types[2] == 1:
        score += 6*pow(10,10)
    elif types[3] == 1:
        score += 5*pow(10,10)
    elif types[2] == 2:
        score += 4*pow(10,10)
    elif types[2] == 1:
        score += 3*pow(10,10)
    else:
        score += 2*pow(10,10)
    return score

def getCardsScore(hand):
    score = 0
    for i in range(0,5):
        score += values[hand[i]]*pow(10,2*(4-i))
    return score

def getScore(line):
    hand = line.split(" ")[0]
    bid = int(line.split(" ")[1].strip())
    
    score = getHandScore(hand)
    score += getCardsScore(hand)

    return score, bid

#Solution to Part 1
def part1(lines):
    hands = []
    result = 0
    for line in lines:
        score, bid = getScore(line)
        hands.append((score,bid))
        #printtest(score)
    sortedHands = sorted(hands)
    for i in range(0, len(sortedHands)):
        result += sortedHands[i][1] * (i+1)
    print("The result is: " + str(result))

#Solution to Part 2
def part2(lines):
    hands = []
    result = 0
    for line in lines:
        score, bid = getScore2(line)
        hands.append((score,bid))
        #printtest(score)
    sortedHands = sorted(hands)
    for i in range(0, len(sortedHands)):
        result += sortedHands[i][1] * (i+1)
    print("The result is: " + str(result))

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