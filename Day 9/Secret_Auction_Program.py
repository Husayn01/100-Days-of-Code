bidders_list = {}
bidding_finished = False


def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finished:
    name = input("What is your name: ")
    bid = int(input("Enter your bid: "))
    bidders_list[name] = bid
    txt = input("Are there any other bidders, Type 'yes' or 'no': ")
    if txt == "no":
        bidding_finished = True
        find_highest_bidder(bidders_list)

print(bidders_list)