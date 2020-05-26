from random import shuffle

from .card import Card

class Deck:
    def __init__(self):
        # create the deck of 52 cards on __init__
        self.cards = self.create_deck()


    def __str__(self):
        return f"{self.remaining()}"


    def create_deck(self):
        SUITS = ["♠","♥","♦","♣"]
        VALUES = list(range(2,11)) + ["J", "Q", "K", "A"]

        cards = []
        for s in SUITS:
            for v in VALUES:
                cards.append(Card(v,s))

        shuffle(cards)
        return cards


    def remaining(self):
        return len(self.cards)


    def deal(self, num=1):
        hand = []
        for i in range(num):
            hand.append(self.cards.pop())

        return hand


    def hit(self):
        return self.deal(1)
