from wordpy_controller import *
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
    Original code was created in a lab in Intro to CS 1
    
    File desc:
    Main file, run this file
"""


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
