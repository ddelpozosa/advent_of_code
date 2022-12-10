import os
from pathlib import Path
p = Path(__file__).with_name('input.txt')

f = p.open('r')
lines = f.readlines()
cycle = 1
x = 1
crt = ""
sum_of_signal_strengths = 0

def print_cycle():
    print(f'its cycle {cycle} and the register value is {x}')

def check_signal_strength():
    if (cycle+20) % 40 == 0:
        print(f'its cycle {cycle} and the signal strength is {cycle*x}')
        return cycle * x
    return 0

def check_end_of_row():
    if (cycle-1) % 40 == 0:
        return "\n"
    return ""

def print_crt():

    if cycle%40 == x or cycle%40 == x+1 or cycle%40 == x+2:
        return("#")
    else:
        return(".")

for line in lines:
    if line.strip() == "noop":
        print_cycle()
        crt += print_crt()
        cycle += 1 ##end of cycle
        crt += check_end_of_row()
        
    else:
        print_cycle()
        crt += print_crt()
        cycle += 1
        crt += check_end_of_row()
        
        print_cycle()
        crt += print_crt()
        x += int(line.strip().split(" ")[1])
        cycle += 1
        crt += check_end_of_row()
        print_cycle()

print(crt)
