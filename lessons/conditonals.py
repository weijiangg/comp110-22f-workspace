"""An examples of conditonal (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guesssed correctly!!!")
else:
    print("Sorry, you guessed incorrectly:(")

print("Game over.")