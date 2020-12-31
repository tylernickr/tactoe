class PlayerInterface(object):

    def __init__(self):
        self.marker = None

    def set_marker(self, marker):
        self.marker = marker

    def play_move(self, board):
        raise NotImplementedError("You need to implement the play_move function in your player.")
