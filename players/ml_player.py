from players.player_interface import PlayerInterface
from random import shuffle
from players.normal_player import NormalPlayer
from game_manager import GameManager
from players.random_player import RandomPlayer


class MLPlayer(PlayerInterface):

    def __init__(self):
        super().__init__()
        self.state_map = {}
        for num1 in ['0', '1', '2']:
            for num2 in ['0', '1', '2']:
                for num3 in ['0', '1', '2']:
                    for num4 in ['0', '1', '2']:
                        for num5 in ['0', '1', '2']:
                            for num6 in ['0', '1', '2']:
                                for num7 in ['0', '1', '2']:
                                    for num8 in ['0', '1', '2']:
                                        for num9 in ['0', '1', '2']:
                                            state = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
                                            self.state_map[state] = (0, 0, 100)

        print('Training for 100000 games...')
        for i in range(100000):
            player2 = NormalPlayer() #if i % 2 == 1 else RandomPlayer()
            gm = GameManager()
            winner = gm.play_game(self, player2)
            for board_state in gm.get_board_states():
                state = self.map_board_to_state(board_state)
                wins, losses, draws = self.state_map[state]
                if winner == '1':
                    self.state_map[state] = (wins + 1, losses, draws)
                elif winner == '2':
                    self.state_map[state] = (wins, losses + 1, draws)
                else:
                    self.state_map[state] = (wins, losses, draws + 1)

    def play_move(self, board):
        best_score = -999
        best_next_state = None
        for state in self.get_possible_next_states(board):
            wins, losses, draws = self.state_map[state]
            next_state_score = (wins - losses) / (wins + losses + draws)
            if next_state_score > best_score:
                best_next_state = state
                best_score = next_state_score
        return self.play_move_from_state(board, best_next_state)

    def print_state_map(self):
        for state, scores in sorted(self.state_map.items(), key=lambda x: (x[1][0] - x[1][1]) / (x[1][0] + x[1][1] + x[1][2])):
            if (scores[0] + scores[1] + scores[2]) > 1:
                print('{}: {}'.format(state, str(scores)))

    def play_move_from_state(self, board, state):
        marker_list = []
        for row in board:
            for space in row:
                if space == self.marker:
                    marker_list.append('1')
                elif space is not None:
                    marker_list.append('2')
                else:
                    marker_list.append('0')
        for i in range(len(marker_list)):
            if state[i] != marker_list[i]:
                return i // 3, i % 3

    def get_possible_next_states(self, board):
        # need to check for unallowed spaces
        next_states = []
        for [rowIdx, row] in enumerate(board):
            for [spaceIdx, space] in enumerate(row):
                if space is None:
                    new_board = [[y for y in x] for x in board]
                    new_board[rowIdx][spaceIdx] = self.marker
                    next_states.append(self.map_board_to_state(new_board))
        return next_states

    def map_board_to_state(self, board):
        marker_list = []
        for row in board:
            for space in row:
                if space == self.marker:
                    marker_list.append('1')
                elif space is not None:
                    marker_list.append('2')
                else:
                    marker_list.append('0')
        return ''.join(marker_list)
