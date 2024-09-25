import random

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose"
    elif u_score == 0:
        return "You win"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "Opponent went over, you win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    def deal_card():
        random_card = random.choice(cards)
        return random_card


    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"User's card: {user_card}")
        print(f"Computer's card firsthand: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, otherwise type 'n' \n").lower()
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    result = compare(user_score, computer_score)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Opponent's final hand: {computer_card}, final score: {computer_score}")
    print(result)

play_again = input("Do you want to play? \n").lower()
while play_again == "y":
    black_jack()
