from random import randint

question: str = input("What is your yes/no question")
response: int = randint(0, 2)

if response == 0:
    print("Yes,def")
else:
    if response == 1:
        print("Ask again later")
    else:
        print("My sources say no")