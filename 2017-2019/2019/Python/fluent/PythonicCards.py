import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]


deck = FrenchDeck()
print(len(deck))
print(choice(deck))
print(deck[:3])
print(Card('Q', 'hearts') in deck)
for card in sorted(deck, key=spades_high):
    print(card)