file1 = open('c:/Users/dpozo/Documents/test/advent_of_code_2021/10/input1.txt', 'r')
lines = file1.readlines()

markers = {">":"<","}":"{",")":"(","]":"["}
prices = {">":25137,"]":57,")":3, "}":1197}

totalPrice = 0
newLines = []
for line in lines:
    openings = []
    #print(line)
    error = False
    for character in line.replace("\n",""):
        if character in ["<","{","(","["]:
            openings.append(character)
        else:
            if markers[character] != openings[len(openings) - 1]:
                error = True
            else:
                openings = openings[0:len(openings)-1]
            
        if error:
            print("Expected " + str(list(markers.keys())[list(markers.values()).index(openings[len(openings) - 1])]) + " but found " + character + " instead")
            totalPrice += prices[character]
            break
    if error == False:
        newLines.append(line)
lines = newLines
print("The total price is: " + str(totalPrice))
print(newLines)
prices = {">":4,"]":2,")":1, "}":3}
scores = []
for line in lines:
    openings = []
    error = False
    for character in line.replace("\n",""):
        if character in ["<","{","(","["]:
            openings.append(character)
        else:
            openings = openings[0:len(openings)-1]
    #print(openings)
    score = 0
    for i in range(len(openings)-1,-1,-1):
        letter = list(markers.keys())[list(markers.values()).index(openings[i])]
        score = score * 5
        score += prices[letter]
        #line += letter
        #print(letter)
    scores.append(score)
    #print(line)

scores = sorted(scores)
print("The middle value of the line scores is: " + str(scores[int((len(scores)-1)/2)]))