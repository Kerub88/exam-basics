import collections

C, H, D, S = "CLUBS", "HEARTS", "DICE", "SPADE"
Card = collections.namedtuple("Card", "suit value")

hand = []

hand.append(Card(C, 3))
hand.append(Card(H, "A"))
hand.append(Card(D, 10))
hand.append(Card(S, "Q"))

for card in hand:
    print(card.value, card.suit)
    
