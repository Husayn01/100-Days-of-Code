import random
from hangman_art import stages, logo
word_list = ["camel", "sheep", "horse", "fox", "mouse", "elephant"]

attempt_left = 6
random_word = random.choice(word_list)
print(logo)
print(random_word)
hidden_word = ["_"] * len(random_word)
print(hidden_word)
gameOver = False

while not gameOver:
    guessed_letter = input("Guess a letter: \n").lower()
    for index, letter in enumerate(random_word):
        if guessed_letter == letter:
            hidden_word[index] = letter
    print(hidden_word)

    if guessed_letter not in random_word:
        print("Ooops, that letter is not in the word, you lose a life :(")
        attempt_left -= 1
        print(f"You have {attempt_left} attempt left")
        print(stages[attempt_left])

    if attempt_left == 0 or "_" not in hidden_word:
        if attempt_left == 0:
            print(f"Game Over. you lost, The correct word is {random_word}")
        else:
            print(f"Game Over. you won, The correct word is {random_word}")
        gameOver = True