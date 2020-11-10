class Joueur:
    """documentation classe joueur test"""

    def __init__(self, name, board):
        self.player_name = name
        self.player_board = board
    @property
    def name(self):
        return self.player_name