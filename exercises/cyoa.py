"""A coinflip guessing game where you have to choose heads or tails and see how many you can guess in a row correctly."""
__author__ = "730569555"

from random import randint

points: int
player: str
game_continue: bool = True
HAT_EMOJI: str = "\U0001F920"
SPIRAL_EYES: str = "\U0001F635"
SAD_EMOJI: str = "\U00002639"
CAT_EMOJI: str = "\U0001F63C"
HEART_EMOJI: str = "\U00002764"


def greet() -> None:
    """Greets player and asks for name."""
    global player
    player = input("What is your name? ")
    print(f"Hello {player}, in this game you will filp a coin and see how many you can guess in a row correctly!{HAT_EMOJI} ")


def procedure() -> None:
    """The main function that the game is played from. Asks the player to guess heads or tails then calls on flip function to flip a coin. Give the player a points or ends the game whether or not if the players guessed correctly."""
    global points
    global game_continue
    procedure_continue: bool = True
    if procedure_continue is True:
        guess: str = input("Do you think the coin will land of heads or tails? ")
    while guess != "tails" and guess != "heads":
        guess = input(f"{player} please respond with heads or tails!{SPIRAL_EYES} ")
    if procedure_continue is True:
        toss: int = 0
        toss = flip(1)
        if toss == 0 and guess == "tails":
            print(f"It landed on tails, you guessed correctly!{CAT_EMOJI} ")
            points += 1
            print(f"Congratulations {player}, you gained 1 adventure points!")
            procedure_continue = False
            print(f"You now have {points} adventure points! ")
        if toss == 0 and guess == "heads":
            print(f"It landed on tails, you guessed wrong.{SAD_EMOJI} ")
            game_continue = False
            procedure_continue = False
        if toss == 1 and guess == "heads":
            print(f"It landed on heads, you guessed correctly!{CAT_EMOJI} ")
            print(f"Congratulations {player}, you gained 1 adventure points!")
            points += 1
            procedure_continue = False
            print(f"You now have {points} adventure points! ")
        if toss == 1 and guess == "tails":
            print(f"It landed on heads, you guessed wrong.{SAD_EMOJI} ")
            game_continue = False
            procedure_continue = False


def flip(x: int) -> int:
    """Randomly choose 0 or 1 to be used as a coin flipping function."""
    i: int = 0
    if x == 1:
        i = randint(0, 1)
        return i


def choice_three() -> None:
    """Choice 3 response that explains the game."""
    print("In this game you will guess whether the coin will land on heads or tails. \nIf you correctly guess the coinflip, you will get 1 adventure point. \nTry to see how many adventure points you can get without guessing wrong! ")
    choice_three_continue: str = input("Respond with 1 if you're ready to play! ")
    while choice_three_continue != "1":
        choice_three_continue = input("Respond with 1 if you're ready to play! ")
    if choice_three_continue == "1":
        procedure()


def choice_two(x: int) -> int:
    """If the player responsed with 2, it will tell them how many points they currently have."""
    if x == 2:
        print(f"You have {points} adventure points. ")
        choice_two_continue: str = ""
        choice_two_continue = input("Respond with 1 if you're ready to play! ")
        while choice_two_continue != "1":
            choice_two_continue = input("Respond with 1 if you're ready to play! ")
        return int(2)


def choice_four() -> None:
    """Choice 4 that ends the game and says goodbye message."""
    print(f"You ended with {points} adventure points! ")
    print(f"Game over! Thanks for playing {player}!{HEART_EMOJI} ")
    quit()
    

def main() -> None:
    """Starting point of the game, asks the player four options that they can choose from. Loops until the player loses or quits."""
    global player
    global points
    global game_continue
    points = 0
    greet()
    while game_continue is True:
        choice: str = input("Respond with 1 to guess a coinflip! \nRespond with 2 see how many adventure points you have. \nRespond with 3 to read the instructions. \nRespond with 4 to exit the game. ")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            choice = input(f"Please responds with 1, 2, 3, or 4!{SPIRAL_EYES}")
        if choice == "1":
            procedure()
        if choice == "2":
            if choice_two(2) == 2:
                procedure()
        if choice == "3":
            choice_three()
        if choice == "4":
            choice_four()
    print(f"You ended with {points} adventure points! ")
    print(f"Game over!{SAD_EMOJI} \nThanks for playing {player}!{HEART_EMOJI} ")


if __name__ == "__main__":
    main()