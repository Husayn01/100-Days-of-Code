print("Welcome of the Tip Calculator")
total_bill = float(input("What is the Total Bill? $"))
percentage_tip = float(input("How much percentage tip do you want to give? "))
no_of_people = int(input("How many people to split the bill? "))
tip = round(percentage_tip / 100, 2) * total_bill
total_with_tip = total_bill + tip
amount_per_person = total_with_tip / no_of_people
print(f"Each person should pay: ${round(amount_per_person, 2)}")