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
import art
from rich.console import Console
console = Console()


with open("words.txt", 'r', encoding="utf-8") as file: # opens words.txt for the program to read
    list_of_words = file.readlines() # reads the file line by line


def main():
    """main function that initializes the game"""
    word = get_word() # stores randomly chosen word to "word" variable
    play_game(word) # goes to the play_game function with the "word" variable
    while input("Would You Like To Play Again? (Yes/No) ").upper() == "YES": # if the user wants to play again
        word = get_word()
        play_game(word)


def get_word():
    """chooses a word at random

    Returns:
        str: the randomly chosen word
    """
    word = random.choice(list_of_words) # chooses a random word from the file
    uppercase_word = word.upper() # makes word uppercase
    return uppercase_word


def play_game(word):
    """main game logic

    Args:
        word (str): randomly chosen word
    """
    word_completion = "_" * (len(word)-1)
    guessed = False
    guessed_letters = []
    tries = 6
    print("Let's play Hangman! Try to guess the car brand.")
    console.print(art.display_hangman(tries), style='bold')
    console.print(word_completion, style="green")
    print("\n")
    if input("Would you like emojis? (Yes/No): ").upper() == "YES":
        if input("Choose the color theme (Matrix/Normal): ").upper() == "MATRIX": # if the user chooses the normal color theme
            while not guessed and tries > 0: # keeps the game going until the user runs out of tries
                guess = input("Guess a letter: ").upper()
                if len(guess) == 1 and guess.isalpha(): # it took me a while to realize that I needed this bit in line 64
                    # because I realized that I was able to guess multiple letters, and it was confusing the program
                    if guess in guessed_letters: # checks if the letter has already been guessed
                        console.print("You've already guessed", guess + " :confused_face:", style="green")
                    elif guess not in word:
                        console.print(guess, "is not correct. :thumbs_down:", style="green")
                        tries -= 1
                        guessed_letters.append(guess)
                    else:
                        console.print("Good job,", guess, "is in the word! :thumbs_up:", style="green")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]  # Pylint suggested that I use enumerate
                        # instead of iterating with range and len. I needed help with enumerate, so I went to youtube for a small part of these next few lines
                        for index in indices: # checks if the guessed letter is in the word
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                else: # if the user enters something other than a letter
                    console.print("Not a valid guess. Try again. :confused_face:", style="green")
                console.print(art.display_hangman(tries), style='bold')
                console.print(word_completion, style="green")
                print("\n")
            if guessed is True: # if the user guessed the word
                console.print("Congrats, you guessed the word! :smile:", style="green")
            else: # if the user ran out of tries
                console.print("GAME OVER. The word was " + word.strip() + ". :disappointed_face:", style="green")
        else: # if the user chooses the normal color theme
            while not guessed and tries > 0: # keeps the game going until the user runs out of tries
                guess = input("Guess a letter: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters: # checks if the letter has already been guessed
                        console.print("You've already guessed", guess + " :confused_face:", style="yellow")
                    elif guess not in word: # if the user guesses a letter that is not in the word
                        console.print(guess, "is not correct. :thumbs_down:", style="red")
                        tries -= 1
                        guessed_letters.append(guess)
                    else:
                        console.print("Good job,", guess, "is in the word! :thumbs_up:", style="green")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices: # checks if the guessed letter is in the word
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                else:
                    console.print("Not a valid guess. Try again. :confused_face:", style="red")
                console.print(art.display_hangman(tries), style='bold')
                console.print(word_completion, style="blue")
                print("\n")
            if guessed is True: # if the user guessed the word
                console.print("Congrats, you guessed the word! :smile:", style="green")
            else: # if the user ran out of tries
                console.print("GAME OVER. The word was " + word.strip() + ". :disappointed_face:", style="red")
    else: # if the user does not want emojis
        if input("Choose the color theme (Matrix/Normal): ").upper() == "MATRIX": # if the user wants the Matrix color theme
            while not guessed and tries > 0: # keeps the game going until the user runs out of tries
                guess = input("Guess a letter: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters: # checks if the letter has already been guessed
                        console.print("You've already guessed", guess, style="green")
                    elif guess not in word: # if the user guesses a letter that is not in the word
                        console.print(guess, "is not correct.", style="green")
                        tries -= 1
                        guessed_letters.append(guess)
                    else: # if the user guesses a letter that is in the word
                        console.print("Good job,", guess, "is in the word!", style="green")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                else: # if the user enters something other than a letter
                    console.print("Not a valid guess. Try again.", style="green")
                console.print(art.display_hangman(tries), style='bold')
                console.print(word_completion, style="green")
                print("\n")
            if guessed is True: # if the user guessed the word
                console.print("Congrats, you guessed the word!", style="green")
            else: # if the user ran out of tries
                console.print("GAME OVER. The word was " + word.strip() + ".", style="green")
        else: # if the user chooses normal color theme
            while not guessed and tries > 0: # keeps the game going until the user runs out of tries
                guess = input("Guess a letter: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters: # checks if the letter has already been guessed
                        console.print("You've already guessed", guess, style="yellow")
                    elif guess not in word: # if the user guesses a letter that is not in the word
                        console.print(guess, "is not correct.", style="red")
                        tries -= 1
                        guessed_letters.append(guess)
                    else: # if the user guesses a letter that is in the word
                        console.print("Good job,", guess, "is in the word!", style="green")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices: # checks if the guessed letter is in the word
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                else: # if the user enters something other than a letter
                    console.print("Not a valid guess. Try again.", style="red")
                console.print(art.display_hangman(tries), style='bold')
                console.print(word_completion, style="blue")
                print("\n")
            if guessed is True: # if the user guessed the word
                console.print("Congrats, you guessed the word!", style="green")
            else: # if the user ran out of tries
                console.print("GAME OVER. The word was " + word.strip() + ".", style="red")


if __name__ == "__main__":
    main()
