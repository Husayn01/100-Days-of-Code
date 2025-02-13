import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("WELCOME TO ROCK, PAPER, SCISSORS GAME !!")
print("Type 1 for Rock")
print("Type 2 for Paper")
print("Type 3 for Scissors")
print()

choices = [rock, paper, scissors]
user_input = int(input("Enter Your Choice (1-3): ")) - 1

if user_input not in [0, 1, 2]:
    print("Invalid choice! Please select 1, 2, or 3.")
else:
    computer_choice = int(random.randint(0,2))
    print("\nYour Choice:")
    print(choices[user_input])

    print("\nComputer's Choice:")
    print(choices[computer_choice])
    if user_input == computer_choice:
        print("\nIt's a tie!")
    elif (user_input == 0 and computer_choice == 2) or \
         (user_input == 1 and computer_choice == 0) or \
         (user_input == 2 and computer_choice == 1):
        print("\nYou Win! 🎉")
    else:
        print("\nComputer Wins! 💻")
