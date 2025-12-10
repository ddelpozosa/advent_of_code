from lib import *
from collections import deque
import re
from scipy.optimize import linprog

TESTS = [
    {"input": "input_test_1.txt", "part1": 7, "part2": None},
    {"input": "input_test_1.txt", "part1": None, "part2": 33}
]

# Get regex for in-between parantheses, brackets and curlys
# Machines = [.##., [(1, 2), (2)], [1,2,3,4]]
# basically [target, buttons, joltage] of type list(char), list(tuple(int), list(int))
# return the list of machines 
def parse(data):
    lines = parse_lines(data)
    machines = []
    for line in lines:
        parens = re.findall(r'\(([^)]*)\)', line)
        brackets = re.search(r'\[([^\]]*)\]', line).group(1) 
        curlies = re.search(r'\{([^}]*)\}', line).group(1)

        target = brackets

        buttons = []
        for button in parens:
            buttons.append(tuple(int(button) for button in button.split(',')))

        power = [int(joltage) for joltage in curlies.split(',')]

        machines.append((target, buttons, power))
    # Custom logic here
    return machines 

# Part 1 can be solved with a BFS approach (finds shortest path)
def find_min_pushes(initial_state, goal_state, buttons):
    queue = deque([(initial_state, 0)])  # (state, num_pushes)
    visited = {initial_state}
    
    while queue:
        current_state, pushes = queue.popleft()
        
        # Check if goal reached
        if current_state == goal_state:
            return pushes
        
        # Try each button
        for button in buttons:
            next_state = apply_button(current_state, button)
            
            # Only explore unvisited states
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, pushes + 1))
    
    return -1  # Goal unreachable

def apply_button(state, button):
    state_list = list(state)
    for wire in button:
        if state_list[wire] == '.':
            state_list[wire] = '#'
        else:
            state_list[wire] = '.'
    return "".join(state_list)


def part1(data):
    machines = parse(data)
    total = 0
    for target, buttons, power in machines:
        initial_state = '.' * len(target)
        total += find_min_pushes(initial_state, target, buttons)
    return total

# Part 2 is a linear algebra problem, requiring linear optimization
def solve_linear_optimization(buttons, power):
    num_buttons = len(buttons)
    num_wires = len(power)
    
    # Build coefficient matrix A where A[wire][button] = 1 if button affects wire
    A = [[0 for _ in range(num_buttons)] for _ in range(num_wires)]
    for button_idx, button in enumerate(buttons):
        for wire in button:
            A[wire][button_idx] = 1
    
    # Objective: minimize sum of button presses
    c = [1 for _ in range(num_buttons)]
    
    # Solve with integer constraint
    # c = what to minimize (weight of 1 to all variables = minimum number)
    # A_eq = equality constraint (variables)
    # b_eq = target values 
    # integrality = forces results to be integers
    # bounds=(0, None) forces results to be positive
    result = linprog(c, A_eq=A, b_eq=power, integrality=1, bounds=(0, None))
    
    if not result.success:
        return -1
    
    return sum(result.x)

def part2(data):
    machines = parse(data)
    total = 0
    
    for state, buttons, power in machines:
        presses = solve_linear_optimization(buttons, power)
        if presses == -1:
            return -1  # No solution found
        total += presses
    
    return total
