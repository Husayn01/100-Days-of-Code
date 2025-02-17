# Now you will implement the function hangman, which takes one parameter - 
# the secretWord the user is to guess. This starts up an interactive game of 
# Hangman between the user and the computer. Be sure you take advantage of the three helper functions, 
# isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) 
# to load the words and pick a random one. Note that the functions loadWords and 
# chooseWord should only be used on your local machine, 
# not in the tutor. When you enter in your solution in the tutor, 
# you only need to give your hangman function.
                                                                                                                                                                                                                   
# Consider using lower() to convert user input to lower case. For example:

# guess = 'A'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
# guessInLowerCase = guess.lower()                                       
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:
                                                                                                                         
# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. 
# Every time a player guesses a letter, the guessed letter must be removed from 
# availableLetters (and if they guess a letter that is not in availableLetters, 
# you should print a message telling them they've already guessed that - so try again!).

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    s = ""
    for letter in alphabet:
        if letter not in lettersGuessed:
            s += letter
    return s
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ["_"] * len(secretWord) 
    for index, letter in enumerate(secretWord):
        if letter in lettersGuessed:
            word[index] = letter 
    return " ".join(word)  
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))