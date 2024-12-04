import numpy as np

def find_directional_pattern(graph, x, y):
    height, width = graph.shape
    directions = [
        (0, 1),   # Up
        (0, -1),  # Down
        (-1, 0),  # Left
        (1, 0),   # Right
        (-1, 1),  # Up-Right
        (-1, -1), # Up-Left
        (1, 1),   # Down-Right
        (1, -1)   # Down-Left
    ]

    valid_patterns_count = 0

    for dx, dy in directions:
        # Check for 'M' in the direction of (dx, dy)
        mx, my = x + dx, y + dy
        if 0 <= mx < width and 0 <= my < height and graph[my, mx] == 'M':
            # Check for 'A' in the same direction
            ax, ay = mx + dx, my + dy
            if 0 <= ax < width and 0 <= ay < height and graph[ay, ax] == 'A':
                # Check for 'S' in the same direction
                sx, sy = ax + dx, ay + dy
                if 0 <= sx < width and 0 <= sy < height and graph[sy, sx] == 'S':
                    valid_patterns_count += 1
                    print(f"Valid pattern found at X({x}, {y}) -> M({mx}, {my}) -> A({ax}, {ay}) -> S({sx}, {sy})")  # Debugging line

    return valid_patterns_count

def search_pattern(graph):
    height, width = graph.shape
    total_valid_patterns = 0

    for y in range(height):
        for x in range(width):
            if graph[y, x] == 'X':
                total_valid_patterns += find_directional_pattern(graph, x, y)

    return total_valid_patterns

# Convert to numpy array
grid = np.genfromtxt('input.txt', dtype=str, delimiter=1, comments=None)

# Print the grid for verification
print("Grid:")
print(grid)

# Count valid patterns
valid_patterns_count = search_pattern(grid)
print(f"Number of valid patterns: {valid_patterns_count}")


def find_x_shape_pattern(graph):
    height, width = graph.shape
    valid_patterns_count = 0

    def is_valid_position(y, x):
        return 0 <= y < height and 0 <= x < width

    # Check for the pattern around each 'A'
    for y in range(height):
        for x in range(width):
            if graph[y, x] == 'A':
                # Check if all required positions are within bounds
                if not all(is_valid_position(ny, nx) for ny, nx in [
                    (y-1, x-1), (y-1, x+1),  # top-left, top-right
                    (y+1, x-1), (y+1, x+1)   # bottom-left, bottom-right
                ]):
                    continue  # Skip if any position is out of bounds

                # Get all diagonal positions
                top_left = graph[y-1, x-1]
                top_right = graph[y-1, x+1]
                bottom_left = graph[y+1, x-1]
                bottom_right = graph[y+1, x+1]

                print(f"\nChecking A at ({x}, {y})")
                print(f"top_left: {top_left}")
                print(f"top_right: {top_right}")
                print(f"bottom_left: {bottom_left}")
                print(f"bottom_right: {bottom_right}")

                # Check for complete X pattern - need both diagonals
                if ((top_right == 'M' and bottom_left == 'S' and top_left == 'M' and bottom_right == 'S') or
                    (top_right == 'M' and bottom_left == 'S' and top_left == 'S' and bottom_right == 'M') or
                    (top_right == 'S' and bottom_left == 'M' and top_left == 'M' and bottom_right == 'S') or
                    (top_right == 'S' and bottom_left == 'M' and top_left == 'S' and bottom_right == 'M')):
                    valid_patterns_count += 1
                    print(f"Complete X pattern found at A({x}, {y})")

    return valid_patterns_count

# Count valid patterns
valid_patterns_count = find_x_shape_pattern(grid)
print(f"\nNumber of valid patterns: {valid_patterns_count}")

