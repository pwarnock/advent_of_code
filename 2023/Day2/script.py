import numpy as np
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

def parse_game(line):
    # Split into game ID and sets
    game_id_part, sets_part = line.split(':')
    game_id = int(game_id_part.split()[1])

    # Parse each set
    sets = sets_part.strip().split(';')
    max_cubes = {'red': 0, 'green': 0, 'blue': 0}

    for set_data in sets:
        # Parse each color count in the set
        colors = set_data.strip().split(',')
        for color_data in colors:
            count, color = color_data.strip().split()
            count = int(count)
            max_cubes[color] = max(max_cubes[color], count)

    return game_id, max_cubes

def is_game_possible(max_cubes, limits):
    return (max_cubes['red'] <= limits['red'] and
            max_cubes['green'] <= limits['green'] and
            max_cubes['blue'] <= limits['blue'])

# Cube limits
limits = {'red': 12, 'green': 13, 'blue': 14}

def calculate_power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']

# Read input from file
try:
    with open(input_path, 'r') as file:
        input_data = file.read().strip()
except FileNotFoundError:
    print("Error: input.txt file not found in the current directory")
    exit(1)

# Process games
possible_game_ids = []
powers = []
for line in input_data.split('\n'):
    if line.strip():  # Skip empty lines
        game_id, cubes = parse_game(line)
        if is_game_possible(cubes, limits):
            possible_game_ids.append(game_id)
        power = calculate_power(cubes)
        powers.append(power)

# Calculate sum using numpy
result = np.sum(possible_game_ids)
print(f"Sum of possible game IDs: {result}")

# Calculate sum of powers using numpy
result = np.sum(powers)
print(f"Sum of the power of minimum cube sets: {result}")