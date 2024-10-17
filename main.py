from maze import Maze
from solver import Solver

def main():
    # Create a simple maze (1 = wall, 0 = path)
    maze_data = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    # Create Maze and Solver objects
    maze = Maze(maze_data)
    solver = Solver(maze)

    # Print the maze before solving
    print("Maze before solving:")
    maze.print_maze()

    # Find path from (1, 1) to (3, 3)
    start = (1, 1)
    end = (3, 3)

    if solver.solve(start, end):
        print("\nPath found!")
        # Print the maze with the path
        print("Maze after solving:")
        maze.print_maze_with_path(solver.path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
