import random
hangmanpics = ['''
  +---+
  |   |
      |
      |
      
      |
      | 
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Word bank of animals
word_str = 'ant baboon badger bat bear beaver camel cat clam cobra cougar ' \
           'coyote crow deer dog donkey duck eagle ferret fox frog goat ' \
           'goose hawk lion lizard llama mole monkey moose mouse mule newt ' \
           'otter owl panda parrot pigeon python rabbit ram rat raven ' \
           'rhino salmon seal shark sheep skunk sloth snake spider ' \
           'stork swan tiger toad trout turkey turtle weasel whale wolf ' \
           'wombat zebra'

words_list = word_str.split()
print(words_list)

random_word = random.choice(words_list)
print(random_word)
secret_word = []

for _ in random_word:
    secret_word += "_"
print(secret_word)

gameover = False
hangmanpics.reverse()
lives = len(hangmanpics) - 1
print(lives)
while not gameover:
    guessed_letter = input("Guess a letter: \n").lower()
    for position in range(len(secret_word)):
        letter = random_word[position]
        if letter == guessed_letter:
            secret_word[position] = letter
    if guessed_letter not in secret_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            break
        print(f"{hangmanpics[lives]}")
    print(secret_word)

    if "_" not in secret_word:
        gameover = True
        print("You won")

