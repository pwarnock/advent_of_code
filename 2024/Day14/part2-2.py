from functools import reduce
import numpy as np
import operator
import os
import re


def get_quadrants(grid):
    # Get dimensions
    rows, cols = grid.shape

    # Find middle indices
    mid_row = rows // 2
    mid_col = cols // 2

    # Extract quadrants (excluding middle row and column)
    top_left = grid[:mid_row, :mid_col]
    top_right = grid[:mid_row, mid_col+1:]
    bottom_left = grid[mid_row+1:, :mid_col]
    bottom_right = grid[mid_row+1:, mid_col+1:]

    return top_left, top_right, bottom_left, bottom_right

def sum_quadrants(grid):
    rows, cols = grid.shape

    # Find middle indices
    mid_row = rows // 2
    mid_col = cols // 2

    # Calculate sums for each quadrant
    top_left_sum = np.sum(grid[:mid_row, :mid_col])
    top_right_sum = np.sum(grid[:mid_row, mid_col+1:])
    bottom_left_sum = np.sum(grid[mid_row+1:, :mid_col])
    bottom_right_sum = np.sum(grid[mid_row+1:, mid_col+1:])

    return {
        'top_left': top_left_sum,
        'top_right': top_right_sum,
        'bottom_left': bottom_left_sum,
        'bottom_right': bottom_right_sum
    }

# input = '''p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3'''

def read_input():

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to input.txt
    input_file_path = os.path.join(script_dir, 'input.txt')

    with open(input_file_path, 'r') as file:
        input = file.read()
    
    return input

robots = []
for line in read_input().strip().split('\n'):
    match = re.match(r'p=([-0-9]+),([-0-9]+) v=([-0-9]+),([-0-9]+)', line)
    if match:
        robots.append({
            'position': [int(match.group(1)), int(match.group(2))],
            'velocity': [int(match.group(3)), int(match.group(4))]
        })

# s = (11,7)  # shape of grid
s = (101, 103)  # shape of grid
grid = np.zeros(s)  # fill with zeros

# plot robots
for robot in robots:
    x, y = robot['position']
    grid[x, y] += 1

# print(grid)

def check_robot_overlap(grid):
    return not np.any(grid > 1)

for _ in range(1, 10000):
    # print(f"After {_} seconds:")
    if _ % 25 == 0:
        print(_) 
    for robot in robots:
        x, y = robot['position']
        vx, vy = robot['velocity']
        grid[x, y] -= 1
        x = (x + vx) % s[0]
        y = (y + vy) % s[1]
        robot['position'] = [x, y]
        grid[x, y] += 1
        if check_robot_overlap(grid):
            print(f'------{_}------')
            



