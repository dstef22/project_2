from PyQt5.QtWidgets import *
from wordpy_view import *
from random import randint
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

    Credit and disclaimer:
    Original code was created in a lab in Intro to CS 1.
    
    File desc:
    This is the controller for the gui.
    This file contains the functions for the gui game to work.
"""


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Setting up controller object
        :param args: passing non-keyword arguments
        :param kwargs: passing keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.guesses = 0
        self.won = False
        self.inputText.setText('. . .')
        self.inputText.setStyleSheet('color: white')
        self.win_output.setStyleSheet('color: white')

        self.files = ['wordpy_words_general.csv', 'wordpy_words_pokemon.csv']
        # Set up secret word
        self.__word_list = []
        with open(self.files[0], 'r') as file:
            self.__word_list = file.readlines()
            self.__word_list = [word.strip() for word in self.__word_list]
            self.__answer = self.__word_list[randint(0, len(self.__word_list) - 1)]

    def keyPressEvent(self, event) -> None:
        """
        Called when a key is pressed, outputs up to 5 letters to gui,
        if the enter key is pressed with 5 letters it computes the guess,
        backspace deletes right most character.
        If user is out of guesses or user won it no longer takes input.
        :param event: Keystroke
        :return: None
        """
        if self.guesses < 6 and not self.won:
            if event.text().isalpha():
                if self.inputText.text() == '. . .':
                    self.inputText.setText(event.text().upper())
                elif len(self.inputText.text()) < 5:
                    self.inputText.setText(self.inputText.text() + event.text().upper())
            elif event.key() == 16777220 and len(self.inputText.text()) == 5:
                if self.inputText.text().lower() in self.__word_list:
                    self.guess(self.inputText.text().lower())
                    self.inputText.setText('. . .')
                    self.guesses += 1
                else:
                    self.win_output.setText(f'{self.inputText.text()} not in word list')
            elif event.key() == 16777219:
                if self.inputText.text() == '. . .':
                    self.inputText.clear()
                if self.win_output.text() != '':
                    self.win_output.clear()
                self.inputText.setText(self.inputText.text()[:-1])

    def guess(self, user_guess) -> None:
        """
        Takes the user's guess and outputs which letters they got right
        :param user_guess: str
        :return: None
        """
        if self.guesses == 0:
            # set first row to each letter
            self.letter_1.setText(user_guess[0].upper())
            self.letter_2.setText(user_guess[1].upper())
            self.letter_3.setText(user_guess[2].upper())
            self.letter_4.setText(user_guess[3].upper())
            self.letter_5.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_1.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_2.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_3.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_4.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_5.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_1.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_2.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_3.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_4.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_5.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_1.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_2.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_3.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_4.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_5.setStyleSheet('color: white')
        elif self.guesses == 1:
            # set first row to each letter
            self.letter_8.setText(user_guess[0].upper())
            self.letter_9.setText(user_guess[1].upper())
            self.letter_10.setText(user_guess[2].upper())
            self.letter_7.setText(user_guess[3].upper())
            self.letter_6.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_8.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_9.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_10.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_7.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_6.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_8.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_9.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_10.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_7.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_6.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_8.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_9.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_10.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_7.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_6.setStyleSheet('color: white')
        elif self.guesses == 2:
            # set first row to each letter
            self.letter_13.setText(user_guess[0].upper())
            self.letter_14.setText(user_guess[1].upper())
            self.letter_15.setText(user_guess[2].upper())
            self.letter_12.setText(user_guess[3].upper())
            self.letter_11.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_13.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_14.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_15.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_12.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_11.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_13.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_14.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_15.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_12.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_11.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_13.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_14.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_15.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_12.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_11.setStyleSheet('color: white')
        elif self.guesses == 3:
            # set first row to each letter
            self.letter_18.setText(user_guess[0].upper())
            self.letter_19.setText(user_guess[1].upper())
            self.letter_20.setText(user_guess[2].upper())
            self.letter_17.setText(user_guess[3].upper())
            self.letter_16.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_18.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_19.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_20.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_17.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_16.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_18.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_19.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_20.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_17.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_16.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_18.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_19.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_20.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_17.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_16.setStyleSheet('color: white')
        elif self.guesses == 4:
            # set first row to each letter
            self.letter_23.setText(user_guess[0].upper())
            self.letter_24.setText(user_guess[1].upper())
            self.letter_25.setText(user_guess[2].upper())
            self.letter_22.setText(user_guess[3].upper())
            self.letter_21.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_23.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_24.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_25.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_21.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_22.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_23.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_24.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_25.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_21.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_22.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_23.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_24.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_25.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_21.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_22.setStyleSheet('color: white')
        elif self.guesses == 5:
            # set first row to each letter
            self.letter_28.setText(user_guess[0].upper())
            self.letter_29.setText(user_guess[1].upper())
            self.letter_30.setText(user_guess[2].upper())
            self.letter_27.setText(user_guess[3].upper())
            self.letter_26.setText(user_guess[4].upper())

            # set each letter to a color, if in the right spot letter is green, if letter in word it's yellow
            for let in range(5):
                if user_guess[let] == self.__answer[let]:
                    if let == 0:
                        self.letter_28.setStyleSheet('background-color: green; color: white')
                    elif let == 1:
                        self.letter_29.setStyleSheet('background-color: green; color: white')
                    elif let == 2:
                        self.letter_30.setStyleSheet('background-color: green; color: white')
                    elif let == 3:
                        self.letter_27.setStyleSheet('background-color: green; color: white')
                    elif let == 4:
                        self.letter_26.setStyleSheet('background-color: green; color: white')
                elif user_guess[let] in self.__answer:
                    if let == 0:
                        self.letter_28.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 1:
                        self.letter_29.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 2:
                        self.letter_30.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 3:
                        self.letter_27.setStyleSheet('background-color: #FDDA0D; color: white')
                    elif let == 4:
                        self.letter_26.setStyleSheet('background-color: #FDDA0D; color: white')
                else:
                    if let == 0:
                        self.letter_28.setStyleSheet('color: white')
                    elif let == 1:
                        self.letter_29.setStyleSheet('color: white')
                    elif let == 2:
                        self.letter_30.setStyleSheet('color: white')
                    elif let == 3:
                        self.letter_27.setStyleSheet('color: white')
                    elif let == 4:
                        self.letter_26.setStyleSheet('color: white')

        # check win condition
        self.check_win(user_guess)

    def check_win(self, user_guess) -> None:
        """
        Checks if the user has won
        :param user_guess: str
        :return: None
        """
        if user_guess == self.__answer:
            if self.guesses == 0:
                self.win_output.setText(f'Solved in 1 guess!')
            else:
                self.win_output.setText(f'Solved in {self.guesses + 1} guesses!')
            self.win_output.setStyleSheet('color: green')
            self.won = True
        elif self.guesses == 5:
            self.win_output.setText(f"The word was '{self.__answer.upper()}'")
            self.win_output.setStyleSheet('color: #FDDA0D')
