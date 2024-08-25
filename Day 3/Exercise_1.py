#Task 1
print("Welcome to the roller coaster game")
height = int(input("What is your height in cm? \n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: \n"))
    if age <= 12:
        bill = 5
        print("Your ticket cost is ${bill}")
    elif age <= 18:
        bill = 7
        print("Your ticket cost is ${bill}")

    elif age >= 45 and age <= 55:
        print("Everthing is going to be okay, have a free ride on us!")
    else:
        bill = 12
        print("Your ticket cost is ${bill}")

    want_photo = input("Do you want a photo? Type y for yes and n for no \n")
    if want_photo == "y":
        bill += 3
        print(f"Your new bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride")

#Task 2
print("Odd/Even number checker")
num = int(input("Enter the number: \n"))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is a odd number")
