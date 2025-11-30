# Advent of Code 2025

Solutions for Advent of Code 2025 challenges with automated testing and efficient day management.

## Project Structure

```
2025
├── src
│   ├── lib.py          # Utility functions and classes for common patterns and data 
│   ├── commands.py     # Command-line functionalities to manage the Advent of Code days
│   ├── templates
│   │   └── solution.py # template solution file for day generation
│   └── days
│       └── day_01
│           ├── input.txt  # Input data for Day 1
│           └── solution.py # Solution logic for Day 1
├── README.md           # Documentation for the project
└── requirements.txt     # List of dependencies required for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd 2025
   ```

2. Install the required dependencies:
   ```
    python -m pip install -r requirements.txt
   ```

## Usage Examples

- To start a new day, use the command:
  ```
  start_day(1)      # Creates day_01 with templates
  start_day()       # Uses today's date
  ```

- Define tests on the day_x/solution.py:
  ```
  TESTS = [
      {"input": "input_test_1.txt", "part1": 10, "part2": None},  # Tests only part1
      {"input": "input_test_2.txt", "part1": 20, "part2": 30},    # Tests both parts
  ]
  ```
- To run a specific day's solution in test mode:
  ```
  run_day(1, 't') - runs all defined tests
  run_day(1, 't', test_num=0)  # Runs only first test
  run_day(1, 't', test_num=1)  # Runs only second test
  ```

- To run a specific day's solution in production mode:
  ```
  run_day(1, 'p') - runs both parts
  run_day(1, 'p', part=1) - runs only part 1
  run_day(1, 'p', part=2) - runs only part 2
  ```