"""EX02 - one shot wordle."""

__author__ = "730569555"

secret = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input("What is your 6-letter guess? ")

x = 0
boxes: str = ""

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")

while x < len(guess):
    if guess[x] == secret[x]:
        boxes += GREEN_BOX
    else:
        character_exists = False
        x2 = 0
        while character_exists is False and x2 < len(guess):
            if guess[x] == secret[x2]:
                boxes += YELLOW_BOX
                character_exists = True
            else:
                if x2 == (len(guess) - int(1)):
                    boxes += WHITE_BOX
                    x2 = x2 + 1
                else:
                    x2 = x2 + 1
    x = x + 1

print(boxes)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
