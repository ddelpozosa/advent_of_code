def simulate_dance(grid, rounds=1000000):
    """
    Simulate the dance for a specified number of rounds.
    Returns the maximum number shouted at the end of any round.
    """
    num_columns = len(grid[0])
    num_rows = len(grid)
    max_number = 0

    def combine_front_numbers():
        """Combine the first numbers of each column to form a single number."""
        return int(''.join(str(grid[0][c]) for c in range(num_columns)))

    def move_clapper(clapper_col):
        """Move the Clapper and update the column configuration."""
        # Clapper moves to the next column
        target_col = (clapper_col + 1) % num_columns
        clapper_number = grid[0][clapper_col]

        # High-fiving around the column
        for direction in ['left', 'right']:
            # 'left' starts from the top to bottom, 'right' from bottom to top
            if direction == 'left':
                for i in range(num_rows):
                    if clapper_number == i + 1:
                        # Absorb the Clapper in front of this person
                        grid = grid[:i] + [[clapper_number] + grid[i][target_col:]] + grid[i + 1:]
                        return
            else:  # direction == 'right'
                for i in reversed(range(num_rows)):
                    if clapper_number == i + 1:
                        # Absorb the Clapper behind this person
                        grid = grid[:i] + [grid[i][target_col:] + [clapper_number]] + grid[i + 1:]
                        return

    # Run the simulation for a large number of rounds
    for round_number in range(1, rounds + 1):
        # Calculate the number at the end of this round
        current_number = combine_front_numbers()
        # Update the maximum number seen so far
        max_number = max(max_number, current_number)

        # Determine the current Clapper column (round_number - 1 % number of columns)
        clapper_col = (round_number - 1) % num_columns
        move_clapper(clapper_col)

    return max_number

# Example Input
grid = [
    [2, 3, 4, 5],
    [6, 7, 8, 9]
]

# Run the simulation
max_number = simulate_dance(grid)
print(f"The highest number shouted in the final dance is: {max_number}")
