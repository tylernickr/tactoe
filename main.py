from game_manager import GameManager
from players.random_player import RandomPlayer
from players.dumb_player import DumbPlayer
from players.normal_player import NormalPlayer
from players.ml_player import MLPlayer
from players.smart_player import SmartPlayer

if __name__ == '__main__':

    p1_wins = 0
    p2_wins = 0
    draws = 0
    player1 = SmartPlayer()  # This is your player
    # player1 = DumbPlayer()  # Uncomment this line if you want to see how play works

    # These are what you're playing against. DumbPlayer < NormalPlayer < MLPlayer. None play perfect so you should be
    # able to beat them all if you make a really good player.
    player2 = RandomPlayer()  # Plays random moves always
    # player2 = DumbPlayer()  # Only blocks winning moves
    # player2 = NormalPlayer()  # Will play winning moves and block winning moves
    # player2 = MLPlayer()  # Machine learning based player, should be a bit better than the other two.
    print('Playing 100,000 games...')
    for i in range(100000):
        winner = GameManager().play_game(player1, player2)
        if winner == '1':
            p1_wins += 1
        elif winner == '2':
            p2_wins += 1
        else:
            draws += 1

    print('Player 1 wins: {}'.format(p1_wins))
    print('Player 2 wins: {}'.format(p2_wins))
    print('Draws: {}'.format(draws))
