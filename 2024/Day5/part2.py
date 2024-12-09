from copy import deepcopy

# map_input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

with open('input.txt', 'r') as file:
    map_input = file.read()

# Transforming map_input into a grid
original_map = [list(row) for row in map_input.splitlines()]
rows = len(original_map)
cols = len(original_map[0])

# Find the guard's starting position
for i in range(rows):
    for j in range(cols):
        if original_map[i][j] in '^>V<':
            starting_pos = (i, j)
            starting_facing = {'^': 'N', '>': 'E', 'V': 'S', '<': 'W'}[original_map[i][j]]
            break

# Possible obstruction positions (excluding starting position and existing obstructions)
possible_positions = []
for i in range(rows):
    for j in range(cols):
        if original_map[i][j] == '.' and (i, j) != starting_pos:
            possible_positions.append((i, j))

class GuardPatrol:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    DELTAS = { 'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1) }

    def __init__(self, map_grid, starting_pos, starting_facing) -> None:
        self._map = map_grid
        self._rows = len(map_grid)
        self._cols = len(map_grid[0])
        self._starting_pos = starting_pos
        self._current_pos = starting_pos
        self._facing = starting_facing

    def rotate_right_90(self):
        idx = self.DIRECTIONS.index(self._facing)
        self._facing = self.DIRECTIONS[(idx + 1) % len(self.DIRECTIONS)]

    def takes_steps_until_exit_or_loop(self):
        visited_states = set()
        rotations = 0

        while True:
            state = (self._current_pos, self._facing)
            if state in visited_states:
                # The guard is stuck in a loop
                return True
            else:
                visited_states.add(state)

            (i, j) = self._current_pos
            (di, dj) = self.DELTAS[self._facing]
            new_pos = (i + di, j + dj)

            # Check if the new position is within bounds
            if 0 <= new_pos[0] < self._rows and 0 <= new_pos[1] < self._cols:
                if self._map[new_pos[0]][new_pos[1]] == '#':
                    # Obstacle, rotate
                    self.rotate_right_90()
                    rotations += 1
                    if rotations == 4:
                        # Guard is trapped and can't move
                        return False  # Guard can't move, but it's not a loop
                else:
                    # Move to the new position
                    self._current_pos = new_pos
                    rotations = 0  # Reset rotations
            else:
                # Out of bounds: guard exits the map
                return False

loop_count = 0

for obstruction_pos in possible_positions:
    # Create a deep copy of the map
    map_copy = [row[:] for row in original_map]
    # Place the new obstruction
    map_copy[obstruction_pos[0]][obstruction_pos[1]] = '#'

    # Create a GuardPatrol instance with the modified map
    guard = GuardPatrol(map_copy, starting_pos, starting_facing)

    # Simulate the guard's movement
    if guard.takes_steps_until_exit_or_loop():
        # The guard got stuck in a loop
        loop_count += 1

print("Number of positions that cause the guard to get stuck in a loop:", loop_count)