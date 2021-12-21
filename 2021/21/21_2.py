from os import path
import timeit
from itertools import product

die_values = [1,2,3]
possible_values = {3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for die1 in die_values:
    for die2 in die_values:
        for die3 in die_values:
            #print("Permutation: [" + str(die1) + "," + str(die2) + "," + str(die3) + "] Total: " + str(die1+die2+die3))
            possible_values[die1+die2+die3] += 1

MAX_SCORE = 21

# player = number of current player
# wins = number of times each player has won so far
# scores = current scores for both players
# positions = current positions for both players
# total_times = total number of times this can occur
def play_game(scores_, positions_, player):
    wins = [0,0]
    for roll,times in possible_values.items():
        #print("Player " + str(player) + " rolls " + str(roll))
        positions = list(positions_)
        scores = list(scores_)
        #print(positions)
        positions[player] = (roll + positions[player] - 1) % 10 + 1
        
        #print(positions[player])
        scores[player] += positions[player]
        if scores[player] >= MAX_SCORE:
            wins[player] += times
            #print("Player " + str(player) + " wins " + str(total_times) + " times.")
        else:
            player_new = (player+1)%2
            theWins = play_game(tuple(scores), tuple(positions), player_new)
            for i in range(2):
                wins[i] += theWins[i]*times
    return wins
    

start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input.txt"))

print(possible_values)

with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


positions = [int(lines[0].split(":")[1].strip()) , int(lines[1].split(":")[1].strip())]
print(positions)
scores = [0,0]

wins = play_game(scores, positions,0)

print("Wins: " + str(wins))

stop = timeit.default_timer()

print(" ")
print('Time: ', stop - start)  