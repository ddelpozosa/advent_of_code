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

def getMatches(line):
    matches = 0
    winNumbers = line.split(":")[1].split("|")[0].strip().split(" ")
    myNumbers = line.split(":")[1].split("|")[1].strip().split(" ")
    winNumbers = list(filter(None, winNumbers))
    myNumbers = list(filter(None, myNumbers))
    for number in winNumbers:
        if number in myNumbers:
            matches += 1
    return matches

#Solution to Part 1
def part1(lines):
    totalPoints = 0
    for line in lines:
        points = 0
        cardName = line.split(":")[0].strip()
        
        matches = getMatches(line)
        printtest(cardName + " has " + str(matches) + " matches")
        if matches > 0:
            temp = matches - 1
            points = 2**temp
        totalPoints += points
        printtest(cardName + " is worth " + str(points) + " points")
    print("The total number of points is " + str(totalPoints))

def addCard(cards, card, amount):
    if card in cards:
        cards[card] += amount
    else:
        cards[card] = amount
def getAmount(cards, card):
    if card in cards:
        return cards[card]
    else:
        return 0

#Solution to Part 2
def part2(lines):
    cards = {}

    for line in lines:
        cardNumber = line.split(":")[0].strip().split(" ")[-1].strip()
        addCard(cards, cardNumber, 1)
        matches = getMatches(line)
        
        printtest(cardNumber + " has " + str(matches) + " matches")
        for i in range(int(cardNumber) + 1, int(cardNumber) + 1 + matches, 1):
            amount = getAmount(cards,cardNumber)
            addCard(cards, str(i), amount)
    total = 0
    for card in cards:
        total += cards[card]

    print("The total number of cards is " + str(total))

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