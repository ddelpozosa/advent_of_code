# Advent of Code 2025

This repository contains solutions for the Advent of Code 2025 challenges. Each day has its own directory with input data and solution scripts.

## Project Structure

```
2025
├── src
│   ├── lib.py          # Utility functions and classes for common patterns and data structures
│   ├── commands.py     # Command-line functionalities to manage the Advent of Code days
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
   pip install -r requirements.txt
   ```

## Usage Examples

- To start a new day, use the command:
  ```python
  from commands import start_day
  start_day(day_number)
  ```

- To run a specific day's solution in test mode:
  ```python
  from commands import run_day
  run_day(day_number, mode='test')
  ```

- To run a specific day's solution in production mode:
  ```python
  run_day(day_number, mode='production')
  ```

## Contributing

Feel free to submit issues or pull requests for improvements or additional features. Happy coding!