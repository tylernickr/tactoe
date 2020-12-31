from players.player_interface import PlayerInterface
from random import shuffle


class RandomPlayer(PlayerInterface):

    def play_move(self, board):
        column_choices = [0, 1, 2]
        row_choices = [0, 1, 2]

        # Randomize attempt order
        shuffle(column_choices)
        shuffle(row_choices)

        # Try all moves until one works
        for column in column_choices:
            for row in row_choices:
                if board[row][column] is None:
                    return row, column

        raise RuntimeError("The board is full, cannot play a move")
