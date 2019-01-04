from Player import Player


class CpuPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def should_hit(self):
        return self.hand.get_value() < 17
