import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
import re


def read_input():

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to input.txt
    input_file_path = os.path.join(script_dir, 'input.txt')

    with open(input_file_path, 'r') as file:
        input = file.read()
    
    robots = []
    for line in input.strip().split('\n'):
        match = re.match(r'p=([-0-9]+),([-0-9]+) v=([-0-9]+),([-0-9]+)', line)
        if match:
            robots.append({
                'position': [int(match.group(1)), int(match.group(2))],
                'velocity': [int(match.group(3)), int(match.group(4))]
            })
    return robots


def visualize_simulation(robots, grid, s, output_dir='simulation_output'):
    # Calculate figure size maintaining aspect ratio
    # Scale down the grid dimensions to reasonable figure sizes
    scale = 0.1  # Adjust this value to make figure larger or smaller
    figsize_x = s[1] * scale  # width based on second dimension (103)
    figsize_y = s[0] * scale  # height based on first dimension (101)

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / 'simulation.txt', 'w') as f:
        for t in range(1, 10000):
            ok_to_write = (t == 6532)
            if t % 25 == 0:
                f.write(f"After {t} seconds:\n")

            # Update robot positions
            for robot in robots:
                x, y = robot['position']
                vx, vy = robot['velocity']
                grid[x, y] -= 1
                x = (x + vx) % s[0]
                y = (y + vy) % s[1]
                robot['position'] = [x, y]
                grid[x, y] += 1

            # # Write non-zero positions to text file
            # for i in range(grid.shape[0]):
            #     for j in range(grid.shape[1]):
            #         if grid[i, j] != 0:
            #             f.write(f"({i},{j}): {int(grid[i,j])} robots\n")
            # f.write("-" * 30 + "\n")

            # Create visualization with proper aspect ratio
            if ok_to_write:
                plt.figure(figsize=(figsize_x, figsize_y))
                plt.imshow(grid, cmap='YlOrRd', aspect='equal')  # ensure square cells
                plt.colorbar(label='Number of robots')
                plt.title(f'Robot Positions at t={t}s')
                plt.grid(True)

                # Adjust font size based on grid size
                font_size = min(figsize_x, figsize_y) * 2  # Adjust multiplier as needed

                # Add text annotations for non-zero positions
                for i in range(grid.shape[0]):
                    for j in range(grid.shape[1]):
                        if grid[i, j] != 0:
                            plt.text(j, i, int(grid[i,j]), 
                                    ha='center', va='center',
                                    color='black' if grid[i,j] < 3 else 'white',
                                    fontsize=font_size)

                # Tight layout to prevent cutting off elements
                plt.tight_layout()

                # Save the plot with proper DPI
                plt.savefig(output_dir / f'frame_{t:03d}.png', 
                        dpi=100,  # Adjust DPI as needed
                        bbox_inches='tight')
                plt.close()


# Example usage:
def main():
    # Define grid size
    grid_size = (101, 103)
    grid = np.zeros(grid_size, dtype=int)

    # Read robots from input.txt
    robots = read_input()

    # Run simulation
    visualize_simulation(robots, grid, grid_size)

if __name__ == "__main__":
    main()

