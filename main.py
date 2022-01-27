import utils
"""
It contains the program in which the game is presented to the user. 
It creates an object by inheriting from the Hangman class and the game is started automatically by calling the StartGame() function.

"""
from utils.game import Hangman

hangman = Hangman()

hangman.StartGame()