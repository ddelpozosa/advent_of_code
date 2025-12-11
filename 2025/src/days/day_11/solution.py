from lib import *

TESTS = [
    {"input": "input_test_1.txt", "part1": 5, "part2": None},
    {"input": "input_test_2.txt", "part1": None, "part2": 2}
]

def parse(data):
    lines = parse_lines(data)
    edges = {}
    for line in lines:
        node = line.split(": ")[0]
        connections = line.split(": ")[1].split(" ")
        edges[node] = connections
    # Custom logic here
    return edges

# DFS implementation to count paths
def get_number_of_paths(edges, start, end):
    
    stack = [(start, [start])]
    all_paths = []
    while stack:
        (node, path) = stack.pop()
        if node not in edges:
            continue
        for next_node in edges[node]:
            if next_node == end:
                all_paths.append(path + [next_node])
            else:
                # Prevent cycles in current path AND respect global visited nodes
                if next_node not in path:
                    stack.append((next_node, path + [next_node]))
    return all_paths

def part1(data):
    edges = parse(data)
    debug(edges)
    total_paths = get_number_of_paths(edges, "you", "out")
    return len(total_paths)

def part2(data):
    edges = parse(data)
    
    # Simple approach: since it's a DAG, the order is fixed
    # Check which order dac/fft appear by seeing if dac can reach fft or vice versa
    
    def count_paths(start, end):
        # Much more efficient: memoized DFS with depth limit
        memo = {}
        
        def dfs(node, target, depth=0):
            if depth > 20:  # Hard depth limit
                return 0
            if node == target:
                return 1
            if (node, target) in memo:
                return memo[(node, target)]
            if node not in edges:
                memo[(node, target)] = 0
                return 0
            
            total = 0
            for next_node in edges[node]:
                total += dfs(next_node, target, depth + 1)
            
            memo[(node, target)] = total
            return total
        
        return dfs(start, end)
    
    # Check the order: can dac reach fft or can fft reach dac?
    # First do quick reachability check to avoid infinite loops
    def can_reach(start, target):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node == target:
                return True
            if node in visited or node not in edges:
                continue
            visited.add(node)
            for next_node in edges[node]:
                if next_node not in visited:
                    stack.append(next_node)
        return False
    
    dac_can_reach_fft = can_reach("dac", "fft")
    fft_can_reach_dac = can_reach("fft", "dac")
    
    print(f"dac can reach fft: {dac_can_reach_fft}")
    print(f"fft can reach dac: {fft_can_reach_dac}")
    
    if dac_can_reach_fft:
        # Order is svr -> dac -> fft -> out
        svr_to_dac = count_paths("svr", "dac")
        dac_to_fft = count_paths("dac", "fft")
        fft_to_out = count_paths("fft", "out")
        result = svr_to_dac * dac_to_fft * fft_to_out
        print(f"Order: svr->dac->fft->out = {svr_to_dac} * {dac_to_fft} * {fft_to_out} = {result}")
    elif fft_can_reach_dac:
        # Order is svr -> fft -> dac -> out  
        svr_to_fft = count_paths("svr", "fft")
        fft_to_dac = count_paths("fft", "dac")
        dac_to_out = count_paths("dac", "out")
        result = svr_to_fft * fft_to_dac * dac_to_out
        print(f"Order: svr->fft->dac->out = {svr_to_fft} * {fft_to_dac} * {dac_to_out} = {result}")
    else:
        print("ERROR: No connection between dac and fft!")
        result = 0
    
    return result  