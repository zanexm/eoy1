# Zane Mendes
# Date Created: 8-12-2004
# Last Modified: 8-12-2024
# Version 1.0.0
# This program will convert words into letter forms of a seperate chained hash table. THis will be used to populate the words section for the letters and numbers game.

from pprint import pprint

def convert_to_letters(word: str) -> str:
    """Converts a word to the alphabetical organisation of the word, ie. cat becomes act

    Args:
        word (str): word to be provided from the dictionary

    Returns:
        str: string organisation of the word
    """
    letterLst = sorted(list(word))
    letterStr = ""
    for char in letterLst:
        letterStr += char
    
    return letterStr

def file_to_dictionary() -> dict:
    """Creates a dictionary in the form of letters:[words formed from letters]. This function returns the dictionary. Words are obtained from 20k.txt

    Returns:
        dict: dictionary containing letters:list of words
    """

    file20k = open("LettersAndNumbers/20k.txt" , "r")
    dict = {} # set up as letters:[list of words]
    for word in file20k.readlines(-1):
        word = word.strip("\n")
        letters = convert_to_letters(word)
        if letters not in dict.keys():
            dict[letters] = [word]
        else:
            dict[letters].append(word)
    
    return dict
