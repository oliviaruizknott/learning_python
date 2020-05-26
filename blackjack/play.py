import sys
import time

from .deck import Deck
from .player import Dealer, Human
from .art import blackjack_cards

def print_hands(reveal=False):
    print(f"""
The dealer has: {dealer.hand_display(reveal)}
You have:       {player.hand_display()}
    """)


def ask_for_choice():
    try:
        choice = input(f"{player.name}, would you like to hit or stand? [h/s]: ").lower()
        if not choice in ['h', 's']:
            raise
    except:
        print("Wups! Please enter 'h' for hit or 's' for stand.")
        ask_for_choice()
    else:
        return choice


def pause(seconds=2):
    time.sleep(seconds)

# # TODO: Implement betting!
# def ask_for_bet():
#     try:
#         bet = int(input(f"\nYou have ${player.money}. How much would you like to bet? [#]: "))
#         if bet < 1 or bet > player.money:
#             raise
#     except:
#         print(f"Wups! Please enter a number between 1 and {player.money}.")
#         ask_for_bet()
#     else:
#         print(f"Excellent. You’re betting ${bet}.")
#         return bet

################################################################################

print(blackjack_cards)
print("Welcome to Blackjack!")

# Make a deck
deck = Deck()

# Make a dealer and deal dealer’s hand
dealer = Dealer()
dealer.hand += deck.deal(2)

# Make a player and deal the player’s hand
name = input("What’s your name?: ")
player = Human(name)
player.hand += deck.deal(2)

# Players turn
hitting = True
while hitting:
    print_hands()

    if player.hand_value() == 21:
        print("Player hand == 21!")
        hitting = False
    elif player.hand_value() > 21:
        print("BUST!!!")
        hitting = False
        sys.exit()
    else:
        choice = ask_for_choice()
        if choice == 'h':
            print("You’ve chosen to hit.")
            player.hand += deck.hit()
        elif choice == 's':
            print("You’ve chosen to stand.")
            hitting = False


# Dealers turn
pause()
print("\nNow it’s the Dealer’s turn.")

dealer_hitting = True
while dealer_hitting:
    pause()
    print_hands(True)
    pause()

    if dealer.hand_value() < 17:
        print("The dealer hits.")
        dealer.hand += deck.hit()

    else:
        dealer_hitting = False
        if dealer.hand_value() == 21:
            print("Dealer hand == 21!")
        elif dealer.hand_value() > 21:
            print("The Dealer BUSTS!!!")
        else:
            print("The Dealer stands.")


if dealer.hand_value() < player.hand_value() <= 21:
    print("You win!!!")
elif player.hand_value() < dealer.hand_value() <= 21:
    print("The Dealer wins!")
elif dealer.hand_value() == player.hand_value():
    print("Tie!")
