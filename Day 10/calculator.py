operators = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 / n2,
}
num1 = int(input("What is the first number? \n"))
operation = input("Pick an operation: \n")
num2 = int(input("What is the next number? \n"))
start_again = True

if operation in operators:
    result = operators[operation](num1, num2)
    print(f"The result is: {result}")
    while start_again:
        should_continue_input = input("Type 'y' to continue\nType 'n' to start a new calculation \n").lower()
        if should_continue_input == "y":
            operation = input("Pick an operation: \n")
            if operation in operators:
                new_result = operators[operation](result, int(input("What is the next number? \n")))
                result = new_result
                print(f"The result is: {new_result}")
            else:
                print("Invalid operation!")
        else:
            start_again = False
else:
    print("Invalid operation!")
