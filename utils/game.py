"""
The class that contains the "Hangman" game related functions and attributes.
The overall flow control of the game is provided by calling the StartGame() function.
The game starts automatically when you create the class as an object and call the StartGame() function.
"""

import random
import time
from typing import Counter, List, Union



class Hangman:
    
    possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        self.life: int = 5
        self.turn_count: int = 0
        self.error_count: int = 0
        self.word_to_find: List[str] = []
        self.well_guessed_letter: List[str] = []
        self.bad_guessed_letter: List[str] = []
        self.correctly_guessed_letters: str = ""

    def findtoWord(self):
        """
        The function that will choice word from possible_words list,randomly. And it converts to letter list as a word_to_find.
        :param self => possible_words: it will be used for choosing word, randomly.
        :return: A List that has letter from selected possible_words's member.
        """
        selected_word = random.choice(self.possible_words)
        self.word_to_find = list(selected_word)

    def createLetter(self):
        """
        The function that will hide the word's letter as a "_" and upload to correctly_guessed_letter
        :param self => word_to_find: it will be used for calculating range in choosed word.
        :return: A list that has hidden letter as a "_". 
        """
        for _ in range(len(self.word_to_find)):
            self.correctly_guessed_letters += "_"

    def play(self):
        """
        The function that it will ask the outside user for letter. It will check if this letter is in the list we created as "word_to_find". 
        It will call TrueMove() if the letter is present in the list, WrongMove() if false. 
        Increments the turn_count each time the play function is called. 
        And finally, it will send information messages to the user.
        :param self
        """
        converted_value = ""
        entered_value = input("Let's Guess! Please enter letter! = ")
        # check entered value. if it's not true format, ask to user again
        while True:
            if entered_value.isalpha():
                converted_value = entered_value.lower()
                break
            else:
                entered_value = input("Please enter (A-z) letter!!!=")

        # check the move. if it's true move,call TrueMove func. if it's not true, call WrongMove
        if converted_value in self.word_to_find:
            # call true move func
            self.trueMove(converted_value)
        else:
            #call wrong move func
            self.wrongMove(converted_value)

        # increase round number by 1
        self.turn_count += 1 

        # print current situation
        print(f"{self.well_guessed_letter} is your well guess")
        print(f"{self.bad_guessed_letter} is your bad guess.")
        print(f"{self.life} is your current life. You done {self.turn_count}. You made {self.error_count} wrong guess.")

    def startGame(self):
        """
        The function that will follow the general flow of the game. 
        By checking the life value in each cycle, it will continue or end the game if the necessary condition is met.  
        :param self.life: 
        :param self.correctly_guessed_letter:
        """

        self.findtoWord()
        self.createLetter()
        self.startingAnimation()

        while True:
            if self.life > 0:                             
                if "_" in self.correctly_guessed_letters:   
                    self.play()
                else:
                    self.wellPlayed()                       
                    break
            elif self.life == 0:
                self.gameOver()
                break

    def gameOver(self) -> bool:
        """
        The function is called when that user's life is over. A message is sent to the user that the game is over.
        : param self:
        : return: A boolean that it's true, if program called this function. 
        """
        print("Game is Over")
        return True

    def wellPlayed(self):
        """
        The function is called when all letters are guessed correctly, which successfully sends the game over message.
        Shares parameters with the user.
        : param self.word_to_find: used for show trying to quess word to user  
        : param self.turn_count: used for reach number of round
        : param self.error_count: used for how many mistakes to made
        """
        print("You win")
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    def wrongMove(self, letter):
        """
        The function is called when that user makes a wrong guess. Decreases the user's health by one. And increments the error value by one.
        : param self.life: When user make a wrong quess, reducing life value by 1. 
        : param self.error_count:  When user make a wrong quess, increase error_count value by 1.  
        """
        print("Upps... Not correct")
        # Add guessed letter to bad_guessed_letter
        self.bad_guessed_letter.append(letter)
        # reduce lives by 1
        if self.life != 0:
            self.life -= 1
        
        self.error_count += 1

    def trueMove(self, letter):
        """
        The function is called when that user guesses correctly. It notifies the user that the correct guess has been made. 
        It takes the guessed letter as a parameter and adds it to the list of correctly guessed letters.
        : param self.life: When user make a wrong quess, reducing life value by 1. 
        : param self.error_count:  When user make a wrong quess, increase error_count value by 1.  
        """
        print("Perfect. You guess correctly")
        # add guessed letter to well_guessed_letter
        self.well_guessed_letter.append(letter)

        # Find location for well quessed letter
        locations = self.findLetterLocation(letter)

        # Change _ to Well Letter 
        list_letter = list(self.correctly_guessed_letters)
        for elem in locations:
            list_letter[elem] = letter
        
        self.correctly_guessed_letters = ''.join(list_letter)
            
        # Print correctly_guessed_letter
        print(f"{self.correctly_guessed_letters}")

    @staticmethod
    def startingAnimation():
        """
        The function two is called as animation at the start of the game. 
        It counts down from 3 and sends the user the message that the game has started.
        : param self
        """
        print("3...")
        time.sleep(0.3)
        print("2...")
        time.sleep(0.3)
        print("1...")
        time.sleep(0.3)
        print("...Game Started...")
        return ""


    def findLetterLocation(self,well_letter):
        """
        The function searches for the letter it takes as a parameter in which index the searched word is in. 
        If there is parameters one or more in word_to_find, it returns the list of indexes.
        : param self.word_to_find: A List that used for searching letter
        : param well_letter: A char that is searching in which index it is in the list.
        : return location_list: A List that has a index of searching letter
        """
        counter = 0
        location_list = []
        for elem in self.word_to_find:
            if well_letter == elem:
                location_list.append(counter)
            counter += 1
        
        return location_list

    