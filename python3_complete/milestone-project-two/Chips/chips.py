class Chips:
    ATTRIBUTES = ['buy_in', 'place_bet', 'win_bet', 'lose_bet']

    def __init__(self):
        self.total = 0
        self.bet = 0

    def buy_in(self, total):
        self.total = total

    def place_bet(self, bet):
        if bet <= self.total:
            self.bet = bet

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0
