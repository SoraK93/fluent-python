import collections
from random import choice

# Here, we are using collections to create a new Card class, without all the extra code.
Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
print(beer_card)

deck = FrenchDeck()

# Happens because we have mentioned __len__() inside the class. 
# len(deck) is calling deck.__len__(), which is a simple method call now.
print(len(deck))

# similarly when calling deck[], its internally calls deck.__getitem__()
print(deck[0])
print(deck[-1])
# Because __getitem__ delegates to [] operator, it automatically supports slicing
print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)
print()
for card in reversed(deck):
    print(card)
print()

# random.choice() is used to randomly select element from a sequence
print(choice(deck))
print(choice(deck))
print(choice(deck))

# 'in' works with our FrenchDeck Class because it is iterable.
print(Card("Q", "hearts") in deck)
print(Card("7", "beasts") in deck)
print()

# Sorting cards: racking cards is by rank (with aces being the highest), then by suit in the order of spades, hearts, diamonds, and clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# FrenchDeck implicitly inherits from the object class, but most of its functional ability is not inherited.
# Implementing special methods __len__ & __getitem__ helps FrenchDeck behave like a standard Python sequence
# Benefits like iteration, slicing, reversed, sorted
def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)