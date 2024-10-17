import random

class Maze:
    def __init__(self, size):
        self.rows = size
        self.cols = size
        self.grid = [[1 for _ in range(size)] for _ in range(size)]  # 1 represents walls
        self._generate_maze(1, 1)

    def is_valid(self, row, col):
        """Check if the cell (row, col) is within bounds and is a path (0)."""
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def _generate_maze(self, row, col):
        """Generate a random maze using recursive backtracking."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        random.shuffle(directions)  # Shuffle directions to ensure randomness

        self.grid[row][col] = 0  # Mark the current cell as a path

        for dr, dc in directions:
            new_row, new_col = row + 2 * dr, col + 2 * dc
            if 0 < new_row < self.rows - 1 and 0 < new_col < self.cols - 1 and self.grid[new_row][new_col] == 1:
                self.grid[row + dr][col + dc] = 0  # Knock down the wall
                self._generate_maze(new_row, new_col)

    def print_maze(self):
        """Print the maze with walls and paths."""
        for row in self.grid:
            print("".join('█' if cell == 1 else ' ' for cell in row))

    def print_maze_with_path(self, path):
        """Print the maze with the path marked."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) in path:
                    row_str += "P "  # Mark the path with 'P'
                else:
                    row_str += '█ ' if self.grid[r][c] == 1 else '  '
            print(row_str)

    def print_maze_with_player(self, player_pos):
        """Print the maze with the player position marked as 'P'."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) == player_pos:
                    row_str += "P "  # Mark the player with 'P'
                else:
                    row_str += '█ ' if self.grid[r][c] == 1 else '  '
            print(row_str)
