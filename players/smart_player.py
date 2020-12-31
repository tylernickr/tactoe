from players.player_interface import PlayerInterface


class SmartPlayer(PlayerInterface):

    def play_move(self, board):
        '''
        This is the only function you should need to implement for now. The game manager will handle the flow of the
        game, deciding if there is a winner, etc. 'board' will be a list of three lists, so you can access a space by
        doing board[row][column] i.e board[0][1] would be the top middle piece of the board. That will return either a
        symbol (X or O) or None (pythons null) if there is no piece there. The symbol that represents you for a given
        game can be accessed with 'self.marker' so you can do something like self.marker == board[1][1] if you wanted
        to see if the middle space was occupied by you. This is implemented in the PlayerInterface class if you really
        want to see how its done, but you don't need to understand how that gets set to make this work.
        I've stubbed out a return statement for you so you can see the format of how the function needs to answer
        its call. Basically you're just returning the row and column of where you want to play your next move, and the
        rest is handled for you. There are a few examples of this being done in the other player class files which could
        act as a guide.
        '''
        row = 0
        column = 0
        return (row, column)

