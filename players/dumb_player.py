from players.player_interface import PlayerInterface
from constants import WINNING_PLACEMENTS
from random import shuffle


class DumbPlayer(PlayerInterface):
    # Will play to block 3 in a row but otherwise plays randomly

    def play_move(self, board):
        blocking_space = self.get_blocking_space(board)
        if blocking_space is not None:
            return blocking_space[0], blocking_space[1]
        else:
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

    def get_blocking_space(self, board):
        blocking_space = None
        for winning_placement in WINNING_PLACEMENTS:
            opponent_spaces = 0
            my_spaces = 0
            empty_spaces = 0
            for space in winning_placement:
                marker = board[space[0]][space[1]]
                if marker is None:
                    empty_spaces += 1
                    blocking_space = space
                elif marker == self.marker:
                    my_spaces += 1
                else:
                    opponent_spaces += 1
            if opponent_spaces == 2 and empty_spaces == 1:
                break
            else:
                blocking_space = None
        return blocking_space
