class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = []
        self.path = []

    def solve(self, start, end):
        """Use DFS to solve the maze from start to end."""
        self.visited = [[False] * self.maze.cols for _ in range(self.maze.rows)]
        self.path = []
        return self._dfs(start[0], start[1], end)

    def _dfs(self, row, col, end):
        """Recursive depth-first search."""
        if (row, col) == end:
            self.path.append((row, col))
            return True
        
        if not self.maze.is_valid(row, col) or self.visited[row][col]:
            return False

        # Mark the current cell as visited
        self.visited[row][col] = True

        # Explore the neighboring cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        for dr, dc in directions:
            if self._dfs(row + dr, col + dc, end):
                self.path.append((row, col))  # Add cell to the path
                return True

        # Unmark if no path is found (backtracking)
        self.visited[row][col] = False
        return False
