import collections
from random import choice

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


