print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? \n"))
bill = 0
if height >= 120:
    print("You can ride")
    age = int(input("Enter your age: \n"))
    if age > 8:
        bill = 12
        print(f"Your ticket cost ${bill}")
    elif age >= 12:
        bill = 7
        print(f"Your ticket cost ${bill}")
    else:
        bill = 5
        print(f"Your ticket cost ${bill}")
    want_photo = input("Do you wnt  photo? \n").lower
    if want_photo == "yes":
        bill += 3
    print(f"Your ticket now cost ${bill}")
else:
    print("You cant ride")
 
    
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")