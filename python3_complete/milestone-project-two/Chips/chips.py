class Chips:
    ATTRIBUTES = ['buy_in', 'place_bet', 'win_bet',
                  'lose_bet', 'reset_bet', 'is_bet_valid', 'no_chips']

    def __init__(self):
        self.total = 0
        self.bet = 0

    def buy_in(self, total):
        self.total = total

    def place_bet(self, bet):
        self.bet = bet

    def is_bet_valid(self):
        return 0 < self.bet <= self.total

    def reset_bet(self):
        self.bet = 0

    def no_chips(self):
        return self.total == 0

    def win_bet(self):
        self.total += self.bet
        self.reset_bet()
        print(f"You've got {self.total}!\n")

    def lose_bet(self):
        self.total -= self.bet
        self.reset_bet()
        print(f"You're down to {self.total}\n")
