from random import shuffle

class Card:
    def __init__(self, display_value, suit):
        self.display = display_value
        self.value = self.calculate_value(display_value)
        self.suit = suit


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        return f"{self.display}{self.suit}"


    def is_ace(self):
        return self.display == "A"


    def calculate_value(self, display_value):
        try:
            return int(display_value)
        except:
            if display_value in ["J", "Q", "K"]:
                return 10
            elif self.is_ace():
                # The special behavior of aces is handled in Player.hand_value
                return 1
