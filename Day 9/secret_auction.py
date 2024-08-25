print("Welcome to the secret auction program")

bid_dict = {}
highest_bid = 0
bid_again = True
while bid_again:
    name_input = input("What is your name? \n").lower()
    bid = int(input("What is your bid: \n"))
    bid_dict[name_input] = bid
    bid_again_input = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    print("\n" * 100)

    if bid_again_input == "no":
        winner = ""
        for bidder in bid_dict:
            if bid_dict[bidder] > highest_bid:
                highest_bid = bid_dict[bidder]
                winner = bidder
        print(f"{winner} made the highest bid: {highest_bid}")
        bid_again = False


