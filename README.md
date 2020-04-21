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
Note that these programs are written in Python 3, and you’ll need it to run them.

## guessing_game
**The Challenge:**

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

- If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
- On a player's first turn, if their guess is within 10 of the number, return "WARM!" further than 10 away from the number, return "COLD!"
- On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!" farther from the number than the previous guess, return "COLDER!"
- When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

## tic_tac_toe
**The Assignment:**
Create a Tic Tac Toe game. Here are the requirements:

- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a symbol on the board
