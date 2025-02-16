import random
word_list = ["camel", "sheep", "horse", "fox", "mouse", "elephant"]

attempt_left = 3
random_word = random.choice(word_list)
print(random_word)
hidden_word = ["_"] * len(random_word)
print(hidden_word)

while "_" in hidden_word:
    guessed_letter = input("Guess a letter: \n").lower()
    for index, letter in enumerate(random_word):
        if guessed_letter == letter:
            hidden_word[index] = letter
        # else:
        #     attempt_left -= 1
    print(attempt_left)
    print(hidden_word)