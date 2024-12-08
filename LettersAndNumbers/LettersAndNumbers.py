# Zane Mendes
# Date Created: 8-12-2004
# Last Modified: 8-12-2024
# Version 1.0.0
# This is a program that will execute function of a letters and numbers game (countdown)
from WordsToLetters import file_to_dictionary
from random import choice
from itertools import permutations

def initialise():
    dict = file_to_dictionary()

# Functionality
# - Timer
# - Solver (both letters and numbers)

def letters_game():
    board = ""
    while len(board) < 9:
        if input("Vowel or Consonant? (V/C). ").lower() == "v":
            letter = choice(["a", "e", "i", "o", "u"])
        else:
            letter = choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"])
        board += letter
        print(f"'{letter}' was picked. Board now contains '{board}'")

    print("Board has been finalised. Time starts now!")
    print(board)

    sortedAux = sorted(list(board))
    sortedBoard = ""
    for char in sortedAux:
        sortedBoard += char
    
    
