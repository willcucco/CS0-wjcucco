"""
Author: Will Cucco
Date: 10/30/23
CSCI 110
Final Project - Hangman

Steps:
    1. read words from 'words.txt'
    2. choose a word at random
    3. present the user with hangman drawing and underscores to show how long the word is
    4. if the user guesses a letter correctly, reveal that letter in the word. Otherwise, add a component to the hangman
    5. if the user fails to guess the word in the specified amount of tries, print 'YOU LOSE!'. Otherwise, reveal the whole word and print 'NICE JOB!'
    6. ask the user if they want to play again. If yes, keep playing and repeat steps 2-5. If no, end the program/game
"""


import random

def choose_word():
    """Chooses a word at random and prints the amount of underscores equal to the amount of
       letters in the chosen word
    """
    words = open("words.txt", 'r', encoding="utf-8")
    words = words.readlines() # reads the words from the file

    word = random.choice(words) # chooses a random word from the file
    word = word.upper().strip() # makes word uppercase and strip trailing whitespaces

    return word


def main():
    """main function that solves the problem
    """
    word = choose_word()
    guess = '_'*len(word) # prints '_' for how many letters are in the word
    print(guess)
    for i in range(len(word)+5):
        letter = user_guess(word, guess)

    #if letter == True:
    #    ()


def user_guess(word, guess):
    letter = input('Enter a guess: ')
    found = False
    for i in range(len(word)+5):
        if word[i] == letter:
            found = True
            guess[i] = letter

    if found == False:
        return False
    if found == True:
        return True



if __name__ == '__main__':
    main()