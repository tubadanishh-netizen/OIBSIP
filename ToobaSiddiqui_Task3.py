# Random Password Generator
# Oasis Infobyte - Python Programming Internship (Project 2)

import random
import string

print("Random Password Generator")
print()

# Ask how long the password should be
length = int(input("How many characters do you want? "))

# Ask which types of characters to include (y/n)
use_letters = input("Include letters? (y/n): ")
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

# Build the pool of characters to pick from
characters = ""
if use_letters == "y":
    characters = characters + string.ascii_letters   # a-z and A-Z
if use_numbers == "y":
    characters = characters + string.digits          # 0-9
if use_symbols == "y":
    characters = characters + string.punctuation     # !@#$ etc.

# Make sure the user picked at least one type
if characters == "":
    print("You need to choose at least one character type.")
else:
    # Pick random characters one by one until we reach the length
    password = ""
    for i in range(length):
        password = password + random.choice(characters)

    print()
    print("Your password is:", password)
