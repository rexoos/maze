# Maze Solver Game

## Overview

The Maze Solver Game is a simple Python game where a player navigates through a randomly generated maze to reach the end. The game supports keyboard inputs (`WASD` and arrow keys) to move the player through the maze, avoiding walls and finding the exit.

The game also features random maze generation and ensures that there is always a solvable path between the start and the end.

## Features

- Randomly generated mazes of varying sizes.
- Guaranteed solvable mazes.
- Player-controlled movement using `WASD` keys and arrow keys.
- Visual representation of walls, paths, player, and the exit point.
- Supports customizable maze sizes (odd numbers greater than or equal to 5).

## Controls

- **W / ↑**: Move up
- **A / ←**: Move left
- **S / ↓**: Move down
- **D / →**: Move right

## How to Play

1. Clone the repository:
    ```bash
    git clone https://github.com/rexoos/maze_game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd maze_game
    ```

3. Run the game:
    ```bash
    python main.py
    ```

4. Enter the maze size (must be an odd number ≥ 5) and navigate the player (`P`) through the maze to reach the exit (`E`).

## Maze Representation

- `■`: Wall
- `  `: Open path
- `P`: Player
- `E`: Exit

## Example Maze

```text
■■■■■■■■■■
■   ■    ■
■ ■ ■ ■■ ■
■ ■     ■
■ ■■■■ ■ ■
■     P  ■
■■■■■■■E■
