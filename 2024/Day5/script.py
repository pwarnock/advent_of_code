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
map = [list(row) for row in map_input.splitlines()]



visited = set()

class GuardPatrol:
    DIRECTIONS = { 'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1) }

    def __init__(self, map) -> None:
        self._map = map
        self._rows = len(map)
        self._cols = len(map[0])
        for i in range(self._rows):
            for j in range(self._cols):
                if map[i][j] == '^':
                    self._starting_pos = (i, j)
                    self._current_pos = (i, j)
                    self._facing = 'N'
    
    def rotate_right_90(self):
        directions = list(self.DIRECTIONS.keys())
        current_index = directions.index(self._facing)
        self._facing = directions[(current_index + 1) % len(directions)]
        print(guard.map_to_text)

    def take_steps(self):
        initial_direction = self._facing
        rotations = 0

        while True:
            (i, j) = self._current_pos
            (di, dj) = self.DIRECTIONS[self._facing]
            new_pos = (i + di, j + dj)

            # Check if the new position is within bounds
            if 0 <= new_pos[0] < self._rows and 0 <= new_pos[1] < self._cols:
                if self._map[new_pos[0]][new_pos[1]] == '#':
                    # Obstacle, rotate and increment rotations
                    self.rotate_right_90()
                    rotations += 1
                    # Break if we've rotated 4 times (360 degrees)
                    if rotations == 4:
                        break
                else:
                    # Mark the current position with 'X' before moving
                    self.mark_visited((i, j))  # Mark the old position as visited

                    # Move to the new position
                    self._current_pos = new_pos
                    self.orient_guard(new_pos)

                    rotations = 0  # Reset rotations after a valid move
            else:
                # new_pos is out of bounds; guard steps off the map
                # Mark the current position before leaving
                self.mark_visited((i, j))
                break  # Exit the loop as guard has left the mapped area

    def orient_guard(self, new_pos):
        # Set the new position symbol based on direction
        if self._facing == 'N':
            self._map[new_pos[0]][new_pos[1]] = '^'
        elif self._facing == 'E':
            self._map[new_pos[0]][new_pos[1]] = '>'
        elif self._facing == 'S':
            self._map[new_pos[0]][new_pos[1]] = 'V'
        elif self._facing == 'W':
            self._map[new_pos[0]][new_pos[1]] = '<'

    def mark_visited(self, coords):
        print(f'Visited {coords}')
        visited.add(coords)
        self._map[coords[0]][coords[1]] = 'X'


    @property
    def map_to_text(self):
        return '\n'.join(''.join(row) for row in self._map)
    


print(map_input)
guard = GuardPatrol(map)
guard.take_steps()

print('Count: ' + str(len(visited)))

