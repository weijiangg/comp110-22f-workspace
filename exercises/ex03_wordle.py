"""EX03 - Structured Wordle."""
__author__ = "730569555"


def contains_char(word: str, x: str) -> bool:
    """Goes through each letter of the secret word to see if the certain letter in the guess word is found in the secret word. If it found somewhere in the secret word, then it will reture true so later in the the code, it will know to print a yellow box instead of a white box."""
    i: int = 0
    while i < len(word):
        assert len(x) == 1
        if x == word[i]:
            return True
        else:
            i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(secret: str, guess: str) -> str:
    """Goes through each letter of the guess word, if it matches the secret word, it adds a green box, if not then if the contains_char call is turned true then it will add a yellow box to the boxes string and if not then it will add a red box to the string. Lastly it prints the boxes string."""
    assert len(secret) == len(guess)

    i: int = 0
    boxes: str = ""
    while i < len(secret) and i < len(guess):
        if guess[i] == secret[i]:
            boxes += GREEN_BOX
        else:
            if contains_char(guess, secret[i]) is True:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
        i += 1
    return boxes


def input_guess(guess_length: int) -> str:
    """Asks for a word that is the same length as the secret word, if not it will repeat until it is the same length as the secret word."""
    guess: str = input(f"Enter a {guess_length} character word:")
    while len(guess) != int(guess_length):
        guess = input(f" That wasn't {guess_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop. Calls on the input_guess to see if the guess is the correct length and emojified to print the correct boxes for the guess. Repeats for 6 times or until the user guesses correctly."""
    i: int = 1
    secret: str = "codes"
    win: bool = False
    while i < 7 and win is False:
        print(f"=== Turn {i}/6 ===")
        guess_word: str = input_guess(len(secret))
        print(emojified(secret, guess_word))
        if secret == guess_word:
            win = True
        else:
            i += 1
    if win is True:
        print(print(f"You won in {i}/{len(secret) + int(1)} turns!"))        
    else:
        print(f"X/{len(secret) + int(1)} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
