import re
import csv
import urllib.request
"""
    Final Project 2: Wordpy
        Using code from an old lab I am creating a wordle game with a gui.
        You are able to switch which list the word to guess is pulled from.
        You can restart the game to guess a different word from the list.
        Word lists were made using a separate script I created called word_file_maker.py.
        You can start the game using the executable file provided.

    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22
    
    File desc:
    For project 2, this is an extra file.
    Made to search a website for 5 letter words and 
    make put them into a csv file to use in wordpy.
"""

if __name__ == '__main__':
    with open('wordpy_words_general.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        with urllib.request.urlopen('https://games4esl.com/list-of-5-letter-words/') as response:
            html = response.read()
            words = re.findall('\w[a-z]+', str(html))
            my_words = []

            for word in words:
                if word.isalpha() and len(word) == 5 and word not in my_words:
                    my_words.append(word)

            for word in my_words:
                csvwriter.writerow([word])

    with open('wordpy_words_pokemon.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        with urllib.request.urlopen('https://www.pokemon.com/us/pokedex') as response:
            html = response.read()
            words = re.findall('\w[a-z]+', str(html))
            my_words = []

            for word in words:
                if word.isalpha() and word.islower() and len(word) == 5 and word not in my_words:
                    my_words.append(word)

            for word in my_words:
                csvwriter.writerow([word])
