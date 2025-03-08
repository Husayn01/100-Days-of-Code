import random
from data import *
from art import *

print(logo)
score = 0
is_game_over = False

while not is_game_over:
    rand_a = random.randint(0, len(data) - 1)
    rand_b = random.randint(0, len(data) - 1)

    # Ensure rand_b is different from rand_a
    while rand_b == rand_a:
        rand_b = random.randint(0, len(data) - 1)

    # Correct string formatting
    print(f"Compare A: {data[rand_a]['name']}, a {data[rand_a]['description']}, from {data[rand_a]['country']}")
    print(vs)
    print(f"Against B: {data[rand_b]['name']}, a {data[rand_b]['description']}, from {data[rand_b]['country']}")

    guess = input("Who has more followers? Type 'A' or 'B' \n").upper()

    # Correct comparison for highest follower count
    if data[rand_a]["follower_count"] > data[rand_b]["follower_count"]:
        highest_follower = "A"
    else:
        highest_follower = "B"

    if guess == highest_follower:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        is_game_over = True
        print(f"You are wrong! Final score: {score}")

    # Display actual follower counts
    print(f"{data[rand_a]['name']}: {data[rand_a]['follower_count']} followers")
    print(f"{data[rand_b]['name']}: {data[rand_b]['follower_count']} followers")