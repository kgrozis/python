import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

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

# create named tuple using Card
cards = Card('7', 'diamonds')
print(cards)

# create an object called deck using class FrenchDeck
deck = FrenchDeck()
# call __len__
print(len(deck))
# call __getitem__
print(deck[0])
print(deck[-1])
# use choice method to randomize
print(choice(deck))
# __getitem__ method delegates [] and supports slicing
print(deck[:3])
print(deck[12::13])
# __getitem__ method makes object iterable
for card in deck:
  print(card)
# iterate in reverse
for card in reversed(deck):
  print(card)
# can overload 'in' operator using __contains__ method
# if __contains__ is not specified, __getitem__ is.  'in' operator will perform
# a seq scan
print(Card('Q', 'hearts') in deck)

# sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]
for card in sorted(deck, key=spades_high):
  print(card)

