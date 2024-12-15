class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.position = self._find_robot()

    def _find_robot(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    return (i, j)
        raise ValueError("No robot (@) found in grid")

    def _get_next_position(self, direction, row=None, col=None):
        if row is None or col is None:
            row, col = self.position

        if direction == '^':  # up
            return row - 1, col
        elif direction == 'v':  # down
            return row + 1, col
        elif direction == '<':  # left
            return row, col - 1
        elif direction == '>':  # right
            return row, col + 1
        return row, col

    def can_move(self, direction):
        curr_row, curr_col = self.position
        next_row, next_col = self._get_next_position(direction)

        # Check bounds
        if not (0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0])):
            return False

        # Empty space
        if self.grid[next_row][next_col] == '.':
            return True

        # Box pushing - check if we can push the box
        if self.grid[next_row][next_col] == 'O':
            box_next_row, box_next_col = self._get_next_position(direction, next_row, next_col)

            # Check if next position is within bounds
            if not (0 <= box_next_row < len(self.grid) and 0 <= box_next_col < len(self.grid[0])):
                return False

            # Check if next position is empty or another box that can be pushed
            return (self.grid[box_next_row][box_next_col] == '.' or 
                   (self.grid[box_next_row][box_next_col] == 'O' and 
                    self._can_push_box_chain(box_next_row, box_next_col, direction)))

        return False

    def _can_push_box_chain(self, row, col, direction):
        """Check if a chain of boxes can be pushed by checking if there's eventually an empty space"""
        current_row, current_col = row, col
        boxes = [(row, col)]

        while True:
            next_row, next_col = self._get_next_position(direction, current_row, current_col)

            # Check bounds
            if not (0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0])):
                return False

            # If we find an empty space, the chain can be pushed
            if self.grid[next_row][next_col] == '.':
                return True

            # If we find another box, continue checking
            if self.grid[next_row][next_col] == 'O':
                boxes.append((next_row, next_col))
                current_row, current_col = next_row, next_col
                continue

            # If we find anything else, we can't push
            return False

    def move(self, direction):
        if not self.can_move(direction):
            return False

        curr_row, curr_col = self.position
        next_row, next_col = self._get_next_position(direction)

        # Simple move to empty space
        if self.grid[next_row][next_col] == '.':
            self.grid[curr_row][curr_col] = '.'
            self.grid[next_row][next_col] = '@'
            self.position = (next_row, next_col)
            return True

        # Push boxes
        if self.grid[next_row][next_col] == 'O':
            # Collect chain of boxes
            check_row, check_col = next_row, next_col
            boxes = []

            while (0 <= check_row < len(self.grid) and 
                   0 <= check_col < len(self.grid[0]) and 
                   self.grid[check_row][check_col] == 'O'):
                boxes.append((check_row, check_col))
                check_row, check_col = self._get_next_position(direction, check_row, check_col)

            # Move boxes starting from the last box
            for box_row, box_col in reversed(boxes):
                next_box_row, next_box_col = self._get_next_position(direction, box_row, box_col)
                self.grid[next_box_row][next_box_col] = 'O'
                self.grid[box_row][box_col] = '.'

            # Move robot
            self.grid[curr_row][curr_col] = '.'
            self.grid[next_row][next_col] = '@'
            self.position = (next_row, next_col)
            return True

        return False

    def print_grid(self):
        print('┌' + '─' * len(self.grid[0]) + '┐')
        for row in self.grid:
            print('│' + ''.join(row) + '│')
        print('└' + '─' * len(self.grid[0]) + '┘')