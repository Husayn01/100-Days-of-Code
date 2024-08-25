print("Welcome to the treasure island game")
print("Your mission is to find the treasure")
choice1 = input("You are at a crossroad, where do you want to go? \n Type 'left' or 'right'")
if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if choice2 == "wait":
        door = input("Which door do you want to pass through? Type 'red', 'blue' or 'yellow'")
        if door == 'red' or door == 'blue':
            print("Game over, you lost!")
        else:
            print("You won!")
    else:
        print("Game over, you lost!")
else:
    print("Game over, you lost!")