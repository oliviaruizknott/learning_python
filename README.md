# learning_python
A collection of Python exercises.

Mid-pandemic, I started learning Python. This Udemy course was my guide: [Complete Python Bootcamp: Go from zero to hero in Python 3](https://www.udemy.com/course/complete-python-bootcamp/). This repo represents a collection of exercises I completed while going through the course.

If you want to run any of my programs, clone or download this repo and use Python to run the file you’re interested in:
```
python {file name}
```
For example:
```
python guessing_game.py
```
Note that these programs are written in Python 3, and you’ll need it to run them. I have to run these with:
```
python3 guessing_game.py
```

## guessing_game
```
python guessing_game.py
```
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

- If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
- On a player's first turn, if their guess is within 10 of the number, return "WARM!" further than 10 away from the number, return "COLD!"
- On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!" farther from the number than the previous guess, return "COLDER!"
- When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

## tic_tac_toe
```
python tic_tac_toe.py
```
Create a Tic Tac Toe game. Here are the requirements:

- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a symbol on the board

## blackjack
```
python blackjack.py
```
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

- You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount. [Betting not implemented.]
- You need to keep track of the player's total money. [Betting not implemented.]
- You need to alert the player of wins, losses, or busts, etc...
- And most importantly: **You must use OOP and classes in some portion of your game. You can not just use functions in your game.**

## car_game
If you have [`pygame`](https://www.pygame.org) installed:
```
python car_game.py
```
I made this as my capstone project for the Udemy course, following [this tutorial](https://coderslegacy.com/python/python-pygame-tutorial/). (I really want to make games! This was my first time using any sort of game-specific software to do so.)
