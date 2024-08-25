import hangman_art
import hangman_words
import random

print(hangman_art.logo)
random_word = random.choice(hangman_words.word_list)
print(random_word)

display = ["_"] * len(random_word)
print(display)

attempts_left = 6
while attempts_left > 0:
    guessed_letter = input("Guess a letter: \n")
    is_letter_in_words = False

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guessed_letter:
            display[position] = letter
            is_letter_in_words = True

    if not is_letter_in_words:
        attempts_left -= 1
        print(hangman_art.stages[attempts_left])
        print(f"Attempts left: {attempts_left}")
    print(display)

    if "_" not in display:
        print("You win")
        break

if attempts_left == 0:
    print("You lost! The word was:", random_word)