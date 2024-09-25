import random

print("Welcome to the number guessing game")

random_num = random.randint(1, 100)
difficulty_input = input("Choose difficulty: 'easy' or 'hard': \n").lower()
is_game_over = False

# Function to determine the number of attempts based on difficulty
def check_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        return "Invalid input"

# Get the number of attempts based on the difficulty
attempts_left = check_difficulty(difficulty_input)
print(f"Attempts left: {attempts_left}")

# Function to play the game
def play_game(attempts_left):
    guessed_num = int(input("Guess the number: \n"))
    if guessed_num == random_num:
        print("You win!")
        return True
    else:
        attempts_left -= 1
        if guessed_num > random_num:
            print("Your guess is too high.")
        elif guessed_num < random_num:
            print("Your guess is too low.")
        print(f"Attempts left: {attempts_left}")
        return attempts_left

# Game loop
while not is_game_over:
    result = play_game(attempts_left)
    if result is True:  # If the player wins
        is_game_over = True
    else:
        attempts_left = result  # Update the attempts left
        if attempts_left == 0:  # If no attempts are left, end the game
            print("You've run out of attempts. Game over!")
            is_game_over = True
