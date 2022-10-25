"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730569555"

five_letter: str = input("Enter a 5-character word: ")
if len(five_letter) != 5:
    print("Error: Word must contain 5 characters")
    exit()

one_letter: str = input("Enter a single character: ")
if len(one_letter) != 1:
    print("Error: Word must contain 1 character")
    exit()

print("Searching for", end=" ")
print(one_letter, end=" ")
print("in", end=" ")
print(five_letter)

count = 0

if one_letter == five_letter[0]:
    print(one_letter, end=" ")
    print("found at index 0")
    count += 1

if one_letter == five_letter[1]:
    print(one_letter, end=" ")
    print("found at index 1")
    count += 1

if one_letter == five_letter[2]:
    print(one_letter, end=" ")
    print("found at index 2")
    count += 1

if one_letter == five_letter[3]:
    print(one_letter, end=" ")
    print("found at index 3")
    count += 1

if one_letter == five_letter[4]:
    print(one_letter, end=" ")
    print("found at index 4")
    count += 1

if count == 0:
    print("No instances of", end=" ")
    print(one_letter, end=" ")
    print("found in", end=" ")
    print(five_letter)
else:
    if count == 1:
        print("1 instance of", end=" ")
        print(one_letter, end=" ")
        print("found in", end=" ")
        print(five_letter)
    else:
        print(count, end=" ")
        print("instances of", end=" ")
        print(one_letter, end=" ")
        print("found in", end=" ")
        print(five_letter)