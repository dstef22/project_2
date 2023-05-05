from termcolor import colored
import random
"""
    Final Project 2: Wordpy
        Using code from an old lab I am creating a wordle game with a gui.
        TODO: I plan on making an executable for this file,
        and I plan on making a way to switch between which file the word comes from,
        and I plan on showing which letters have benn guessed already.
        and I plan on making a way to restart the game in the gui.

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22
    
    File desc:
    Original code from a lab I did in Intro to CS 1.

    THIS FILE IS NOT MEANT TO BE RUN!
"""


random_words = ["ghoul", "boxes", "could", "bushy", "water", "happy", "yours", "bowls", "lolly", "color", "jelly", "stars", "ready", "ferns", "pluck", "lamia", "doors", "sheer", "dunce", "words", "snake", "truce", "sword", "bored", "gourd", "cutie", "truck"]

random_word = random_words[random.randint(0, len(random_words) - 1)]

random_list = list(random_word)

print(f"{'-'*20}\n{'WORDLE':^20}\n{'-'*20}")

for guess in range(6):
    user_guess = input(f"Enter guess #{guess + 1}: ")
    
    user_list = list(user_guess)
    
    # coloring
    for c in range(5):
        if user_list[c] == random_list[c]: # same spot same character
            user_list[c] = colored(user_list[c], "green", attrs=["reverse", "bold"])
        elif user_list[c] in random_list: # check to see if the character is somewhere else in the random word
            user_list[c] = colored(user_list[c], "yellow", attrs=["reverse", "bold"])
        else:
            user_list[c] = colored(user_list[c], "red", attrs=["reverse", "bold"])
        # print(user_list[c], end='') ''''another way to print''''
    # print()''''another way to print''''
    print(f"{' '*23}{''.join(user_list)}")
    
    # check if win
    
    if user_guess == random_word:
        print(f"You guessed the word in {guess + 1} tries!")
        # print(f"Your final guess was {''.join(user_list)}")
        break

print(f"Your final guess was {''.join(user_list)}")
