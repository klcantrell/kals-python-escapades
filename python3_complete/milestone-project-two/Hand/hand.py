class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.high_aces = 0

    def get_value(self):
        return self.value

    def get_cards(self):
        return self.cards

    def get_high_aces(self):
        return self.high_aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.high_aces += 1

    def adjust_for_ace(self):
        if self.high_aces > 0:
            self.high_aces -= 1
            self.value -= 10
