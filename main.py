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

    start = (1, 1)
    end = (3, 3)

    print("Choose how to solve the maze:")
    print("1. Let the solver find the path.")
    print("2. Solve the maze yourself.")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        # Let the solver solve the maze
        if solver.solve(start, end):
            print("\nPath found!")
            maze.print_maze_with_path(solver.path)
        else:
            print("No path found.")
    elif choice == '2':
        # Let the user solve the maze
        play_game(maze, start, end)
    else:
        print("Invalid choice. Exiting.")

def play_game(maze, start, end):
    player_pos = start
    maze.print_maze_with_player(player_pos)

    while player_pos != end:
        move = input("Move (W/A/S/D): ").upper()

        if move == 'W':  # Up
            new_pos = (player_pos[0] - 1, player_pos[1])
        elif move == 'A':  # Left
            new_pos = (player_pos[0], player_pos[1] - 1)
        elif move == 'S':  # Down
            new_pos = (player_pos[0] + 1, player_pos[1])
        elif move == 'D':  # Right
            new_pos = (player_pos[0], player_pos[1] + 1)
        else:
            print("Invalid move! Use W, A, S, or D.")
            continue

        if maze.is_valid(new_pos[0], new_pos[1]):
            player_pos = new_pos
            maze.print_maze_with_player(player_pos)
        else:
            print("You hit a wall! Try a different direction.")

    print("Congratulations! You've reached the goal!")

if __name__ == "__main__":
    main()
