print("Welcome to the Tip Calculator")
bill = float(input("What is the total bill? \n"))
tip = int(input("How much tip would you lik to give? 10, 12, or 15? \n"))
People = int(input("How many people to split the bill? \n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / People
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount}")