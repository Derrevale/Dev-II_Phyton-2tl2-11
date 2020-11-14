class Joueur:
    """documentation classe joueur test"""

    def __init__(self, name, board, wallet_amount=150):
        self.player_name = name
        self.player_board = board
        self.player_wallet = wallet_amount

    @property
    def name(self):
        return self.player_name