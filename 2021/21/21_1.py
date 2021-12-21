from os import path
import timeit

def roll_dice(die):
    total = 0
    for i in range(3):
        if die < 100:
            total += die
            die += 1
        else:
            total += die
            die = 1
    return total, die


start = timeit.default_timer()
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "input.txt"))
with open(filepath, "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]

player_1_pos = int(lines[0].split(":")[1].strip())
player_2_pos = int(lines[1].split(":")[1].strip())

player_1_score = 0
player_2_score = 0

die = 1
total_rolls = 0
while player_1_score < 1000 and player_2_score < 1000:
    total, die = roll_dice(die)
    player_1_pos += total
    #print(total)
    player_1_pos = player_1_pos % 10
    if player_1_pos == 0:
        player_1_pos = 10
    player_1_score += player_1_pos
    total_rolls += 3
    print("Player 1 total score: " + str(player_1_score))

    if player_1_score < 1000:
        total, die = roll_dice(die)
        player_2_pos += total
        player_2_pos = player_2_pos % 10
        if player_2_pos == 0:
            player_2_pos = 10
        player_2_score += player_2_pos
        total_rolls += 3
        print("Player 2 total score: " + str(player_2_score))
    

if player_1_score >= 1000:
    losing_player = ("2",player_2_score)
else:
    losing_player = ("1",player_1_score)
print("Losing player is " + losing_player[0] + " with a score of " + str(losing_player[1]) + " after the die has been rolled " + str(total_rolls) + " time. Total: " + str(total_rolls*losing_player[1]))

stop = timeit.default_timer()

print(" ")
print('Time: ', stop - start)  