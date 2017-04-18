# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# deck = Deck(12)
# print(deck)
# # Should print out:
# # 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
# top_card = deck.draw()
# print(top_card)
# print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

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
