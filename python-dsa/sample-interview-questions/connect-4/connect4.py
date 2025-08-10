"""
We’d like you to implement a class-based simulation of the classic two-player game Connect Four.
 The game is played on a vertical 6-row by 7-column grid. Players take turns dropping discs into one of the columns, 
 and the disc occupies the lowest available slot in that column. The first player to form a horizontal, vertical, or diagonal 
 line of four of their discs wins the game.

Your Task:
Design an object-oriented system to simulate a Connect Four game.

Handle input parsing from a file or function that provides the list of column choices for each move.

Prevent illegal moves (e.g., if a column is full).

Track the board state and determine when a player has won.

At the end, output:

the final board

the winner (or declare a draw if no one wins after all moves).
"""

game_input = {
    "players": ["X", "O"],
    "moves": [3, 4, 3, 4, 3, 4, 3]  # drops into column 3, column 4, tc
}

game_board = [["" for i in range(3)] for i in range(5)]
game_board[2][1] = "3"
starting_position = game_board[2][1]
print(starting_position)