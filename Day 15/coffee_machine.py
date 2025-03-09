from data import *

endOfOperation = False

def report():
    """Prints the current resource levels of the coffee machine."""
    for key in resources:
        print(f"{key} : {resources[key]}")

def request_payment():
    """
    Asks the user to input the number of coins inserted and calculates the total money.
    
    Returns:
        float: The total amount of money inserted.
    """
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

def is_resources_sufficient(coffee_type):
    """Checks if there are enough resources to make the selected coffee."""
    menu = MENU[coffee_type]["ingredients"]
    if resources["water"] < menu["water"]:
        print("Sorry, not enough water.")
        return False
    if "milk" in menu and resources["milk"] < menu["milk"]:
        print("Sorry, not enough milk.")
        return False
    if resources["coffee"] < menu["coffee"]:
        print("Sorry, not enough coffee.")
        return False
    return True

while not endOfOperation:
    prompt = input("What would you like? (espresso/latte/cappuccino): \n").lower()

    if prompt == "report":
        report()
    elif prompt in ("espresso", "latte", "cappuccino"):
        coffee_type = prompt

        # Check resources first
        if not is_resources_sufficient(coffee_type):
            continue

        # Request payment after confirming resources
        user_money = request_payment()
        cost = MENU[coffee_type]["cost"]

        # Check if payment covers the cost
        if user_money < cost:
            print(f"Sorry, not enough money. Here's your refund: ${user_money:.2f}")
            continue

        # Process the transaction
        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
        if "milk" in MENU[coffee_type]["ingredients"]:
            resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        resources["money"] += cost
        change = user_money - cost
        print(f"Here is your {coffee_type}. Enjoy!")
        if change > 0:
            print(f"Your change: ${change:.2f}")
        report()
    elif prompt == "off":
        endOfOperation = True
    else:
        print("Invalid Command! Please choose espresso, latte, cappuccino, report, or off.")