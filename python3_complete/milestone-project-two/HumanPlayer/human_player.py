from Player import Player
from Chips import Chips


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.chips = Chips()

    def __getattr__(self, attr):
        if attr in Chips.ATTRIBUTES:
            return getattr(self.chips, attr)
