from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

operations_dict = {
    '+': add,
    '-': subtract, 
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    do_continue = True
    num1 = int(input("What is the first number: \n"))

    while do_continue:
        operator = input("'Pick an operation: (+, -, *, /)\n")
        num2 = int(input("What is the next number: \n"))
        func = 0
        result = operations_dict[operator](n1=num1, n2=num2 )
        print(f"{num1} {operator} {num2} = {result} ")

        continued = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'q' to exit\n")

        if continued == "y":
            num1 = result
        elif continued == 'q':
            do_continue = False
        elif continued == 'n':
            do_continue = False
            calculator()

calculator()
