class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, row, col):
        """Check if the cell (row, col) is within bounds and is a path (0)."""
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def print_maze(self):
        """Print the maze without any path."""
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def print_maze_with_path(self, path):
        """Print the maze with the path marked."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) in path:
                    row_str += "P "  # Mark the path with 'P'
                else:
                    row_str += str(self.grid[r][c]) + " "
            print(row_str)

    def print_maze_with_player(self, player_pos):
        """Print the maze with the player position marked as 'P'."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) == player_pos:
                    row_str += "P "  # Mark the player with 'P'
                else:
                    row_str += str(self.grid[r][c]) + " "
            print(row_str)
