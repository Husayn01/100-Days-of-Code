##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 
# instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, 
# remove the 11 and replace it with a 1. You might need to look up append() and remove().
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or 
# if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. 
# If yes, then use the deal_card() function to add another card to the user_cards List. 
# If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks 
# in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. 
# The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score 
# and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. 
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def playGame():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    isGameOver = False

    def deal_card():
        random_card = random.choice(cards)
        return random_card

    def calculate_score(card):
        if len(card) == 2 and sum(card) == 21:
            return 0
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
        return sum(card)

    def compare_cards(u_score, c_score):
        if c_score > 21 and u_score > 21:
            return "You lose miserably. You went over 21."
        if u_score == c_score:
            return "It is a draw. Better luck next time."
        elif c_score == 0:
            return "You lose. The computer has a Blackjack :("
        elif u_score == 0:
            return "Congratulations. Blackjack, you win!"
        elif u_score > 21:
            return "Oh man. You went over. You lost."
        elif c_score > 21:
            return 'Congrats. You have won!!! computer went over 21.'
        elif user_score > c_score:
            return 'You win!'
        else: 
            return "You lose!"

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards}, Current score: {user_score}")
        print(f"Computer card: {computer_cards}, Current score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            pick_again = input('Would you like to pick another card? Type \'y\' or \'n\' ')
            if pick_again == 'y':
                user_cards.append(deal_card())
            else:
                isGameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your card: {user_cards}, Final score: {user_score}")
    print(f"Computer card: {computer_cards}, Final score: {computer_score}")
    print(compare_cards(u_score=user_score, c_score=computer_score))

while input("Would you like to play a game of blackjack (y/n) ") == 'y':
    playGame()
 