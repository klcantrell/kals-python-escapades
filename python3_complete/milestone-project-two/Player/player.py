from Hand import Hand


class Player:
    def __init__(self, name):
        self.hand = Hand()
        self.name = name

    def take_card(self, card):
        self.hand.add_card(card)

    def get_score(self):
        return self.hand.get_value()

    def has_busted(self):
        return self.hand.get_value() > 21

    def has_high_aces(self):
        return self.hand.get_high_aces() > 0

    def adjust_for_ace(self):
        self.hand.adjust_for_ace()

    def show_some(self):
        last_card = self.hand.get_cards()[-1]
        print(f"\n{self.name}'s Card")
        print('================')
        print(f'{last_card.rank} of {last_card.suit}')
        print('================\n')

    def show_all(self):
        cards = self.hand.get_cards()
        print(f"\n{self.name}'s Cards")
        print('================')
        for index, card in enumerate(cards, start=1):
            print(f'Card {index}:')
            print(f'{card.rank} of {card.suit}')
        print('================\n')
