from termcolor import colored
import random
"""
    Final Project 2: Wordpy
        Using code from an old lab I am creating a wordle game with a gui.
        You are able to switch which list the word to guess is pulled from.
        You can restart the game to guess a different word from the list.
        Word lists were made using a separate script I created called word_file_maker.py.
        
        TODO: I plan on making an executable for this file

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22
    
    File desc:
    Project is based on original code that was created 
    with help in a lab in the class Intro to CS 1

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
