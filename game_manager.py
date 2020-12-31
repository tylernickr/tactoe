from random import randint
from constants import WINNING_PLACEMENTS


class GameManager(object):

    def __init__(self):
        self.board_states = []

    def play_game(self, first_player, second_player):
        # Setup board
        board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

        # Randomize who goes first
        order = randint(0, 1)
        if order == 0:
            player1 = first_player
            player2 = second_player
        else:
            player2 = first_player
            player1 = second_player

        # Tell the players who they are
        player1.set_marker("X")
        player2.set_marker("O")

        # Loop turns
        moves_played = 0
        while self.get_winner(board) is None and not self.is_board_full(board):
            if moves_played % 2 == 0:
                row, column = player1.play_move(board)
                if board[row][column] is not None:
                    raise RuntimeError('Illegal move, {}, {} is already an occupied space'.format(row, column))
                board[row][column] = 'X'
            else:
                row, column = player2.play_move(board)
                if board[row][column] is not None:
                    raise RuntimeError('Illegal move, {}, {} is already an occupied space'.format(row, column))
                board[row][column] = 'O'
            self.board_states.append([[y for y in x] for x in board])
            moves_played += 1

        winner = self.get_winner(board)
        if first_player.marker == winner:
            return '1'
        elif second_player.marker == winner:
            return '2'
        else:
            return None

    def is_board_full(self, board):
        for row in board:
            for space in row:
                if space is None:
                    return False
        return True

    def get_winner(self, board):
        for winning_placement in WINNING_PLACEMENTS:
            sp1, sp2, sp3 = winning_placement
            marker1 = board[sp1[0]][sp1[1]]
            marker2 = board[sp2[0]][sp2[1]]
            marker3 = board[sp3[0]][sp3[1]]

            if marker1 == marker2 == marker3 == 'X':
                return 'X'
            elif marker1 == marker2 == marker3 == 'O':
                return 'O'
        return None

    def get_board_states(self):
        return self.board_states

    def print_board(self, board):
        row1, row2, row3 = board
        print([x if x else '_' for x in row1])
        print([x if x else '_' for x in row2])
        print([x if x else '_' for x in row3])
        print('\n')
