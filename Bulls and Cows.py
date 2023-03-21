"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukáš Chovan
email: lukas.chovan@seznam.cz
discord: LachY22#8861
"""

import random

number_length = 4
divider = 47 * "-"

secret_number = ""
while len(secret_number) < number_length:
    new_digit = str(random.randint(0, 9))
    if new_digit not in secret_number and not secret_number.startswith("0"):
        secret_number += new_digit


print("Hi there!",
      divider,
      "I´ve generated a random 4 digit number for you.",
      "Let´s play a bulls and cows game",
      divider,
      sep="\n")

number_of_guesses = 0

while True:

    player_guess = input("Please enter your guess: ")
    print(divider)

    if len(player_guess) != number_length:
        print(f"Your guess must be {number_length} digits long!")
        continue
    elif not player_guess.isnumeric():
        print("Please enter only numbers from 0-9!")
        continue
    elif len(player_guess) != len(set(player_guess)):
        print("Guess shouldn´t have repeated digits!")
        continue
    elif player_guess[0] == "0":
        print("Guess can´t start with 0!")
        continue

    # Main game logic
    if player_guess == secret_number:
        number_of_guesses += 1
        if number_of_guesses == 1:
            print(f"Nice, you guessed right number in {number_of_guesses} guess!")
            print(divider)
            print("That´s amazing!")
        else:
            print(f"Correct, you guessed right number in {number_of_guesses} guesses!")
            print(divider)
            if number_of_guesses <= 3:
                print("That´s average.")
            elif number_of_guesses >= 4:
                print("That´s not so good.")

        break

    else:
        number_of_guesses += 1
        bulls = 0
        cows = 0
        for i in range(4):
            if player_guess[i] == secret_number[i]:
                bulls += 1

        for j in range(4):
            if player_guess[j] in secret_number and \
              player_guess[j] != secret_number[j]:
                cows += 1

        if bulls == 1:
            print(f"Bull: {bulls}")
        else:
            print(f"Bulls: {bulls}")

        if cows == 1:
            print(f"Cow: {cows}")
        else:
            print(f"Cows: {cows}")
