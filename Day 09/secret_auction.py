bid_dict = {}
restart = True
def func():
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    bid_dict[name] = bid
    print("\n" * 10)

while restart:
    func()
    more_bid =input("Are there any other bidders? Type 'yes or 'no' \n").lower()
    if more_bid != "yes":
        restart = False

key = max(bid_dict, key=bid_dict.get)
value = bid_dict[key]
print(f"The winner is {key} with a bid of ${value}")