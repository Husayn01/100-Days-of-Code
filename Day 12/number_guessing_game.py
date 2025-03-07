import random

num = random.randint(1, 100)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

def difficulty_func():
    while True:
        difficulty_level = input("Pick a difficulty level, 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            return 10
        elif difficulty_level == "hard":
            return 5
        else:
            print("Invalid input! Please type 'easy' or 'hard'.")

attempt_left = difficulty_func()
print(f"You have {attempt_left} attempts.")

while attempt_left > 0:
    try:
        guess = int(input("Pick a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if guess == num:
        print("Correct, You win!")
        break
    else:
        attempt_left -= 1
        if guess > num:
            print("Too high.")
        else:
            print("Too low.")

        if attempt_left > 0:
            print(f"Wrong, you have {attempt_left} attempts left.")
        else:
            print(f"You lose! The correct number was {num}.")


