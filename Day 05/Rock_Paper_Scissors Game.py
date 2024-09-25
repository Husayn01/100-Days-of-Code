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
choiceList = [rock, paper, scissors]
user_choice = int(input('''What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n'''))

if user_choice >=3 or user_choice < 0:
    print("Invalid input. Please enter a number between 0 and 2")
else:
    computer_choice = random.randint(0, 2)
    print(f'Your Choice:\n{choiceList[user_choice]}')
    print(f'Computer\'s Choice:\n{choiceList[computer_choice]}')
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif computer_choice < user_choice:
        print("You win")
    elif user_choice == computer_choice:
        print("It's a Draw!")
    else:
        print("You lose!")
