print("Welcome to the Password Generator")
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "8", "0"]
symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-"]
password_list = []

letters_input = int(input("How many letters would you like in your password? \n"))
symbols_input = int(input("How many symbols would you like? \n"))
numbers_input = int(input("How many numbers would you like? \n"))

for i in range(0, letters_input):
    random_letters = random.choice(letters)
    password_list.append(random_letters)

for i in range(0, numbers_input):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

for i in range(0, symbols_input):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")