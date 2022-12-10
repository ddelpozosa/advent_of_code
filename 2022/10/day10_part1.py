import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()
cycle = 1
x = 1

sum_of_signal_strengths = 0

def print_cycle():
    print(f'its cycle {cycle} and the register value is {x}')

def check_signal_strength():
    if (cycle+20) % 40 == 0:
        print(f'its cycle {cycle} and the signal strength is {cycle*x}')
        return cycle * x
    return 0

for line in lines:
    if line.strip() == "noop":
        cycle += 1 ##end of cycle
        sum_of_signal_strengths += check_signal_strength()
        #print_cycle()
    else:
        cycle += 1
        sum_of_signal_strengths += check_signal_strength()
        #print_cycle()
        x += int(line.strip().split(" ")[1])
        cycle += 1
        sum_of_signal_strengths += check_signal_strength()
        #print_cycle()

print(f'The total sum of signal strengths is: {sum_of_signal_strengths}')