import random

from .constants import SUITS, RANKS, VALUES
from Card import Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                value = VALUES[rank]
                self.deck.append(Card(
                    suit=suit, rank=rank, value=value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))
        return str(cards)

    def __len__(self):
        return len(self.deck)
