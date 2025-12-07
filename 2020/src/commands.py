import os
import shutil
from datetime import datetime
import importlib.util
import sys
import time

# Add parent directories to path to find lib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import set_test_mode

def format_time(seconds):
    #Format time nicely (ms, s, etc)
    #if seconds < 0.001:
    #    return f"{seconds * 1_000_000:.2f}µs"
    if seconds < 1:
        return f"{seconds * 1_000:.2f}ms"
    else:
        return f"{seconds:.2f}s"

def start_day(day_number=None):
    if day_number is None:
        day_number = datetime.now().day
    
    day_folder = f"days/day_{day_number:02d}"
    os.makedirs(day_folder, exist_ok=True)
    
    shutil.copy("templates/solution.py", f"{day_folder}/solution.py")
    open(f"{day_folder}/input.txt", "w").close()
    open(f"{day_folder}/input_test_1.txt", "w").close()
    
    print(f"Created Day {day_number:02d}")

def run_day(day_number=None, mode='test', test_num=None, part=None):
    if day_number is None:
        day_number = datetime.now().day
    
    day_folder = f"days/day_{day_number:02d}"
    solution_path = os.path.join(day_folder, "solution.py")
    
    if not os.path.exists(solution_path):
        print(f"Day {day_number:02d} not found at {solution_path}")
        return
    
    original_cwd = os.getcwd()
    sys.path.insert(0, original_cwd)
    sys.path.insert(0, os.path.join(original_cwd, ".."))  # Add parent directory to path
    
    try:
        os.chdir(day_folder)
        
        spec = importlib.util.spec_from_file_location("solution", "solution.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if mode in ['test', 't']:
            _run_tests(module, test_num)
        else:
            _solve_prod(module, part)
    finally:
        os.chdir(original_cwd)

def _run_tests(module, test_num=None):
    set_test_mode(True)
    tests = [module.TESTS[test_num]] if test_num is not None else module.TESTS
    for i, test in enumerate(tests):
        data = open(test["input"]).read()
        parts = []
        for part_name in ['part1', 'part2']:
            expected = test[part_name]
            if expected is not None:
                start = time.time()
                result = getattr(module, part_name)(data) # Calls a function by its literal string name (part1 or part2)
                elapsed = time.time() - start
                status = '✓' if result == expected else '✗'
                parts.append(f"{part_name.upper()}={result} {status} ({format_time(elapsed)})")
        print(f"Test {i+1}: {' '.join(parts)}")

def _solve_prod(module, part=None):
    set_test_mode(False)
    data = open("input.txt").read()
    if part in [None, 1]:
        start = time.time()
        result = module.part1(data)
        elapsed = time.time() - start
        print(f"Part 1: {result} ({format_time(elapsed)})")
    if part in [None, 2]:
        start = time.time()
        result = module.part2(data)
        elapsed = time.time() - start
        print(f"Part 2: {result} ({format_time(elapsed)})")