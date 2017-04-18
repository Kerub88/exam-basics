import random

class Card(object):
    colors = ["Clubs", "Diamonds", "Hearts", "Spades"]
    value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.card = {self.color : self.value}

    def card_info(self):
        return str(self.card[0]) + " " + str(self.card[1])

class Deck(Card):

    def __init__(self, number_of_cards = 4):
        self.number_of_cards = number_of_cards
        self.deck_cards = []
        while self.number_of_cards > 0:
            random_colors = random.randrange(0, 3)
            random_value = random.randrange(0, 13)
            card_color = ""
            card_value = ""
            for i in range(len(Card.colors)):
                if i == random_colors:
                    card_color += Card.colors[i]
                    break
            for v in range(len(Card.value)):
                if v == random_value:
                    card_value += Card.value[v]
                    break
            card = Card(card_color, card_value)
            self.deck_cards.append(card)
            self.number_of_cards -= 1

    def count_cards(self, color_or_value):
        number = 0
        for i in self.deck_cards:
            for k, v in i:
                if k == color_or_value:
                    number += 1
                elif v == color_or_value:
                    number += 1
        return number

    def get_info(self):
        return str(len(self.deck_cards)) + " cards - " + str(self.count_cards("Clubs")) + " Clubs, " + str(self.count_cards("Diamonds")) + " Diamonds, " + str(self.count_cards("Hearts")) + " Hearts, " + str(self.count_cards("Spades")) + " Spades"
