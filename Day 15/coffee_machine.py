import menu

resources = menu.resources
is_on = True
profit = 0


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def process_coin():
    print("Please insert coins ")
    total_coins = int(input("How many quarters: ")) * 0.25
    total_coins += int(input("How many dimes: ")) * 0.10
    total_coins += int(input("How many nickles: ")) * 0.05
    total_coins += int(input("How many pennies: ")) * 0.01
    return total_coins


def is_transaction_successful(amount_received, drink_cost):
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    command = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    if command == "off":
        is_on = False
    elif command == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"money: {profit}")
    elif command in ["espresso", "latte", "cappuccino"]:
        drink = menu.MENU[command]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(command, drink["ingredients"])
    else:
        print("Invalid command")
        is_on = False
