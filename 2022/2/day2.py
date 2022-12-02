import os

from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()

scores = {"X":1,"Y":2, "Z":3}

wins = {"A":"Y", "B":"Z", "C":"X"}
loses = {"A":"Z", "B":"X", "C":"Y"}
draws = {"A":"X", "B":"Y", "C":"Z"}

guide = {"X":loses, "Y":draws, "Z":wins}


### Part One ###
totalScore = 0
for i, line in enumerate(lines):
    round = 0
    opponent = line.split(" ")[0]
    player = line.strip().split(" ")[1]
    round += scores[player]
    if wins[opponent] == player:
        round += 6
    elif draws[opponent] == player:
        round += 3
    print(f'Round {i+1}. Player score is {round}')
    totalScore+=round

print(f'Player total score according to Part 1: {totalScore}')

### Part Two ###
totalScore = 0
for i, line in enumerate(lines):
    round = 0
    opponent = line.split(" ")[0]
    player = line.strip().split(" ")[1]

    strat = guide[player]
    round += scores[strat[opponent]]
    if strat == wins:
        round += 6
    elif strat == draws:
        round += 3

    print(f'Round {i+1}. Player score is {round}')
    totalScore+=round

print(f'Player total score according to Part 2: {totalScore}')
