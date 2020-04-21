import os

markers = ['X', 'O']
winning_placements = [
    # horizontal
    (1,2,3),
    (4,5,6),
    (7,8,9),
    # vertical
    (1,4,7),
    (2,5,8),
    (3,6,9),
    # diagonal
    (1,5,9),
    (3,5,7)
]
player1 = {
    'string': 'Player 1',
    'mark': 'a',
    'places': []
}
player2 = {
    'string': 'Player 2',
    'mark': 'a',
    'places': []
}
current_player = player1
ended = False

def print_board():
    os.system('clear')
    def c(num):
        if num in player1['places']:
            mark = player1['mark']
            return f' {mark} '

        elif num in player2['places']:
            mark = player2['mark']
            return f' {mark} '

        else:
            return f'[{num}]'

    print(f"""
         |     |
     {c(1)} | {c(2)} | {c(3)}
    _____|_____|_____
         |     |
     {c(4)} | {c(5)} | {c(6)}
    _____|_____|_____
         |     |
     {c(7)} | {c(8)} | {c(9)}
         |     |
    """)

def take_input():
    placement = None
    prompt = f"""Type the number of the space where you’d like to place your mark.
{current_player['string']} ({current_player['mark']}) [#]: """

    # check that the placement is valid
    while not placement:
        placement = check_valid(input(prompt))

    # add it to the current player’s placements
    current_player['places'].append(placement)

    check_end()

def check_valid(placement):
    # cast to integer; invalid if not possible
    try:
        placement = int(placement)
    except:
        print("Enter a number.")
        return False

    # invalid if not between 1 and 9
    if placement < 1 or placement > 9:
        print("Make sure your number is between 1 and 9.")
        return False

    # invalid if already taken
    taken = player1['places'] + player2['places']
    if placement in taken:
        print("That space is already taken. Choose another.")
        return False

    # otherwise, valid!
    return placement

def check_end():
    global ended

    # did this player win?
    for wp in winning_placements:
        if all(elem in current_player['places'] for elem in wp):
            ended = True
            print_board()
            print(f"\nTHE {current_player['mark']}s WIN!!! Good job, {current_player['string']}.")
            break

    # is the board full? (tie)
    if not ended and len(player1['places'] + player2['places']) >= 9:
        ended = True
        print("\nCat’s game. No one wins.")

def switch_player():
    global current_player

    if current_player == player1:
        current_player = player2

    elif current_player == player2:
        current_player = player1

################################################################################
# TIC TAC TOE
# This code runs the game

os.system('clear')
print("Welcome to Tic Tac Toe.")

# Set player markers
while player1['mark'] not in markers:
    player1['mark'] = input(f"{player1['string']}, please select X or O as your marker [x/o]: ").upper()

markers.remove(player1['mark'])
player2['mark'] = markers[0]

print(f"\n{player1['string']}, you are {player1['mark']}.")
print(f"{player2['string']}, you are {player2['mark']}.")

# A turn
while not ended:
    print_board()
    take_input()
    switch_player()
