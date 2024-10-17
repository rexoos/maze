import keyboard
import os
import time
from maze import Maze
from solver import Solver

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    size = int(input("Enter maze size (e.g., 10 for a 10x10 maze): "))
    maze = Maze(size)
    solver = Solver(maze)

    start = (1, 1)
    end = (size - 2, size - 2)

    print("Generating a solvable maze...")
    print("Choose how to solve the maze:")
    print("1. Let the solver find the path.")
    print("2. Solve the maze yourself.")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        # Let the solver solve the maze
        print("\nPath found!")
        maze.print_maze_with_path(solver.path, end)
    elif choice == '2':
        # Let the user solve the maze with real-time movement
        play_game(maze, start, end)
    else:
        print("Invalid choice. Exiting.")


def play_game(maze, start, end):
    player_pos = start
    maze.print_maze_with_player(player_pos, end)

    while player_pos != end:
        new_pos = player_pos

        # Move the player based on real-time key presses (supporting arrow keys and WASD)
        if keyboard.is_pressed('w') or keyboard.is_pressed('up'):  # Up
            new_pos = (player_pos[0] - 1, player_pos[1])
        elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):  # Left
            new_pos = (player_pos[0], player_pos[1] - 1)
        elif keyboard.is_pressed('s') or keyboard.is_pressed('down'):  # Down
            new_pos = (player_pos[0] + 1, player_pos[1])
        elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):  # Right
            new_pos = (player_pos[0], player_pos[1] + 1)

        if new_pos != player_pos:
            if maze.is_valid(new_pos[0], new_pos[1]):
                player_pos = new_pos
                clear_screen()
                maze.print_maze_with_player(player_pos, end)
            else:
                print("You hit a wall!")

        time.sleep(0.15)  # Delay to avoid multiple key presses being registered too quickly

    print("Congratulations! You've reached the goal!")

if __name__ == "__main__":
    main()
