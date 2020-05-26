class Player:
    def __init__(self):
        self.hand = []


    def hand_value(self):
        value = sum([card.value for card in self.hand])

        if any(card.is_ace() for card in self.hand) and value <= 11:
            value += 10

        return value


    def hand_display(self):
        return ', '.join([str(card) for card in self.hand])


class Dealer(Player):
    def __init__(self):
        Player.__init__(self)


    def hand_display(self, reveal=False):
        hand = self.hand.copy()
        if not reveal:
            hand[1] = '??'

        return ', '.join([str(card) for card in hand])


class Human(Player):
    def __init__(self, name):
        Player.__init__(self)
        self.name = name
        # # TODO: Implment betting!
        # self.money = 50
        # self.bet = 0
