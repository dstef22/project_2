import re
import csv
import urllib.request
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
