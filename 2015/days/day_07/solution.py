from lib import *
import re

TESTS = [
    {"input": "input_test_1.txt", "part1": 0, "part2": None}
]

def parse(data):
    circuit = parse_lines(data)
    operations = []
    for op in circuit:
        # Pattern: "input -> output" or "input1 GATE input2 -> output"
        match = re.match(r'(.+)\s->\s(.+)$', op)

        instruction = match.group(1)
        wire = match.group(2)
        # Check operation type
        if "NOT" in instruction:
            input_wire = instruction.split("NOT ")[1]
            operations.append(("NOT", input_wire, None, wire))
        
        elif " AND " in instruction:
            parts = instruction.split(" AND ")
            operations.append(("AND", parts[0], parts[1], wire))
        
        elif " OR " in instruction:
            parts = instruction.split(" OR ")
            operations.append(("OR", parts[0], parts[1], wire))
        
        elif " LSHIFT " in instruction:
            parts = instruction.split(" LSHIFT ")
            operations.append(("LSHIFT", parts[0], int(parts[1].strip()), wire))
        
        elif " RSHIFT " in instruction:
            parts = instruction.split(" RSHIFT ")
            operations.append(("RSHIFT", parts[0].strip(), int(parts[1]), wire))
        
        else:  # Direct assignment
            operations.append(("ASSIGN", instruction, None, wire))
    
    return operations

def emulate_circuit(operations, override_b=None):
    memo = {}
    
    # Build wire_to_op
    wire_to_op = {}
    for action, op_1, op_2, wire in operations:
        wire_to_op[wire] = (action, op_1, op_2, wire)
    
    # Override b if specified (for part 2)
    if override_b is not None:
        wire_to_op["b"] = ("ASSIGN", str(override_b), None, "b")
    
    #Recursively get value
    def get_value(val):
        # If it's a number, return it
        if val.isdigit():
            return int(val)
        
        # If already computed, return cached value
        if val in memo:
            return memo[val]
        
        # If not in operations, return 0 (shouldn't happen)
        if val not in wire_to_op:
            return 0
        
        # Compute the operation
        action, op_1, op_2, wire = wire_to_op[val]
        
        if action == 'ASSIGN':
            result = get_value(op_1)
        elif action == 'NOT':
            result = ~get_value(op_1) & 0xFFFF
        elif action == 'AND':
            result = get_value(op_1) & get_value(op_2)
        elif action == 'OR':
            result = get_value(op_1) | get_value(op_2)
        elif action == 'LSHIFT':
            result = get_value(op_1) << op_2
        elif action == 'RSHIFT':
            result = get_value(op_1) >> op_2
        
        memo[val] = result
        return result


    # Compute all wires
    for wire in wire_to_op:
        if wire not in memo:
            get_value(wire)

    

    return memo

# for testing
def get_final_state(circuit):
    final_state = ""
    for wire in circuit:
        final_state += (wire + ": " + str(circuit[wire]) + "\n") 
    return final_state

def part1(data):
    operations = parse(data)
    circuit = emulate_circuit(operations)
    debug(get_final_state(circuit))
    if "a" in circuit:
        return circuit["a"]
    else:
        return 0 #for test case

def part2(data):
    operations = parse(data)
    circuit1 = emulate_circuit(operations)
    a_signal = circuit1["a"]
    
    circuit2 = emulate_circuit(operations, override_b=a_signal)
    return circuit2["a"]
