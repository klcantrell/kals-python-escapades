from Deck import suits, ranks, values
from Card import card


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                value = values[rank]
                self.deck.append(card.Card(suit=suit, rank=rank, value=value))

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))
        return str(cards)
