def prime_number_checker(number):
    is_prime = True
    for i in range(1, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

n = int(input("Enter a number? "))
prime_number_checker(number = n)
