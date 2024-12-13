# Zane Mendes
# Date Created: 8-12-2004
# Last Modified: 8-12-2024
# Version 1.0.0
# This is a program that will execute function of a letters and numbers game (countdown)
from WordsToLetters import file_to_dictionary
from random import choice
from itertools import combinations
from typing import List
import time
from pprint import pprint
def initialise():
    return file_to_dictionary()


# Functionality
# - Timer
# - Solver (both letters and numbers)

def letters_game():
    board = ""
    while len(board) < 9:
        if input("Vowel or Consonant? (V/C). ").lower() == "v":
            letter = choice(["a", "e", "i", "o", "u"])
        else:
            letter = choice(["b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w"])
        board += letter
        print(f"'{letter}' was picked. Board now contains '{board}'")

    print("Board has been finalised. Time starts now!")
    print(board)

    return board
    
    
def find_words(characters, wordDict) -> List[str]:
    wordsByLength = {9:[],
                     8:[],
                     7:[],
                     6:[],
                     5:[],
                     4:[],
                     3:[]
                     }
    characters = sorted(characters)

    for r in range(3, len(characters) + 1):
        for subset in combinations(characters, r):
            key = ''.join(sorted(subset))
            if key in wordDict:
                for word in wordDict[key]:
                    if word not in wordsByLength[len(word)]:
                        wordsByLength[len(word)].append(word)

    return wordsByLength

def display_words(wordsByLength: dict):
    for length in wordsByLength.keys():
        print(f"{length} letter words:")
        words =  wordsByLength[length]
        if len(words) == 0:
            print(f"\tNo {length} letter words")
        else:
            print("\t", end="")
            string = ""
            for word in words:
                string += word + ", "
            string = string[:-2]
            print(string)


if __name__ == "__main__":
    wordDict = initialise()
    f = open("abc.txt", "w")
    for letters in wordDict.keys():
        f.write(f"{letters} : {wordDict[letters]}\n")
    characters = letters_game()
    time.sleep(3)
    display_words(find_words(characters, wordDict))