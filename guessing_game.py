from random import randint

# Set the secret number and guesses list
secret_number = randint(1,100)
guesses = []

# Welcome the player
print("""
    Welcome to the Guessing Game!
    
    I'm thinking of a number between 1 and 100. Try to guess what it is.
    
    If your first guess is within 10 of the number, I'll tell you "WARM!"
    If your first guess is further than 10 away from the number, I'll tell you "COLD!"
    
    On all guesses after that, I'll tell you "WARMER!" if your guess is closer than your previous guess, and "COLDER" if it's farther.
""")

while not secret_number in guesses:
    guess = input("Make a guess: ")

    # Convert this to an integer if we can.
    try:
        guess = int(guess)
    except:
        print("Please only enter numbers.")
        continue

    # If guess is correct, player wins!
    if guess == secret_number:
        guesses.append(guess)
        break

    # If guess was not valid, handle that here.
    if guess < 1 or guess > 100:
        print("Guess a number between 1 and 100.")
        continue

    # If this was the first guess, do something different.
    if len(guesses) == 0:
        if secret_number - 10 <= guess <= secret_number + 10:
            print("WARM!")
        else:
            print("COLD!")
    # Otherwise, compare to previous guess.
    else:
        diff = abs(secret_number - guess)
        last_diff = abs(secret_number - guesses[-1])

        if diff < last_diff:
            print("WARMER!")
        elif diff > last_diff:
            print("COLDER!")
        elif diff == last_diff:
            print("SAME!")

    # Add this guess to the guesses
    guesses.append(guess)

print(f"YOU WIN!!! It took you {len(guesses)} { 'guesses' if  len(guesses) > 1 else 'guess' }.")