import random
import art
import game_data


def compare(persona_1, persona_2):
    persona_1["value"] = "A"
    persona_2["value"] = "B"
    if persona_1['follower_count'] > persona_2['follower_count']:
        return persona_1["value"]
    else:
        return persona_2["value"]


def game():
    score = 0
    is_game_over = False

    while not is_game_over:
        persona = game_data.data

        # Ensure A and B are different
        A = random.choice(persona)
        B = random.choice(persona)
        while A == B:
            B = random.choice(persona)

        print(art.logo)
        print(f"{A['name']}, a {A['description']} with {A['follower_count']} followers in {A['country']}")
        print(art.vs)
        print(f"{B['name']}, a {B['description']} with {B['follower_count']} followers in {B['country']}")

        guess = input("Who has more followers, 'A' or 'B': \n").upper()

        answer = compare(A, B)

        if guess == answer:
            score += 1
            print(f"Current score: {score}")
            print(f"Correct, you guessed right!")
        else:
            print(f"Wrong, you lost!")
            print(f"Final score: {score}")
            is_game_over = True


game()
