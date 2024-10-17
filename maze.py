import random

class Maze:
    def __init__(self, size):
        self.rows = size
        self.cols = size
        self.grid = [[1 for _ in range(size)] for _ in range(size)]  # 1 represents walls
        self._generate_maze_with_path((1, 1), (size - 2, size - 2))  # Ensure start to end path

    def is_valid(self, row, col):
        """Check if the cell (row, col) is within bounds and is a path (0)."""
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def _generate_maze_with_path(self, start, end):
        """Generate a maze that guarantees a path from start to end."""
        # Step 1: Carve a direct path from start to end
        self._carve_path(start, end)

        # Step 2: Randomly branch out to create additional complexity in the maze
        stack = [start]
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Move by 2 to carve the path

        while stack:
            current = stack[-1]
            random.shuffle(directions)  # Shuffle directions to randomize path carving

            carved = False
            for dr, dc in directions:
                new_row, new_col = current[0] + dr, current[1] + dc
                if 1 <= new_row < self.rows - 1 and 1 <= new_col < self.cols - 1 and self.grid[new_row][new_col] == 1:
                    self.grid[current[0] + dr // 2][current[1] + dc // 2] = 0  # Knock down the wall
                    self.grid[new_row][new_col] = 0  # Mark the new cell as path
                    stack.append((new_row, new_col))
                    carved = True
                    break

            if not carved:
                stack.pop()  # Backtrack if no carving is possible

    def _carve_path(self, start, end):
        """Directly carve a path from start to end to guarantee solvability."""
        current = start
        self.grid[current[0]][current[1]] = 0  # Mark start as path
        while current != end:
            if current[0] < end[0]:  # Move downwards
                current = (current[0] + 1, current[1])
            elif current[1] < end[1]:  # Move rightwards
                current = (current[0], current[1] + 1)
            self.grid[current[0]][current[1]] = 0  # Carve the path

    def print_maze(self):
        """Print the maze with walls (■) and paths (spaces)."""
        for row in self.grid:
            print("".join('■' if cell == 1 else ' ' for cell in row))

    def print_maze_with_path(self, path, end):
        """Print the maze with the path and mark the end point."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) in path:
                    row_str += "P "  # Mark the path with 'P'
                elif (r, c) == end:
                    row_str += "E "  # Mark the end point with 'E'
                else:
                    row_str += '■ ' if self.grid[r][c] == 1 else '  '
            print(row_str)

    def print_maze_with_player(self, player_pos, end):
        """Print the maze with the player position marked as 'P' and the end as 'E'."""
        for r in range(self.rows):
            row_str = ""
            for c in range(self.cols):
                if (r, c) == player_pos:
                    row_str += "P "  # Mark the player with 'P'
                elif (r, c) == end:
                    row_str += "E "  # Mark the end point with 'E'
                else:
                    row_str += '■ ' if self.grid[r][c] == 1 else '  '
            print(row_str)
