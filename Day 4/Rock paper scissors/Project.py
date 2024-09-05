import random
import utils

choices = [utils.rock, utils.paper, utils.scissors]
user_input = int(input("What do you choose? Type 0 Rock, 1 for Paper or 2 for Scissors \n"))

if user_input < 0 or user_input > 2:
    print("Invalid choice. Please enter 0, 1, or 2.")
else:
    computer_input = random.randint(0, int(len(choices) - 1))
    computer_choice = choices[computer_input]
    user_choice = choices[user_input]
    print(f"You choose: {user_input} " + user_choice)
    print(f"Computer choose: {computer_input} " + computer_choice)

    if computer_input == user_input:
        print("This is a DRAW!")
    elif (user_input == 0 and computer_input == 2) or \
         (user_input == 1 and computer_input == 0) or \
         (user_input == 2 and computer_input == 1):
        print("You WON!")
    else:
        print("You LOST!")