import math
def is_prime(number):

    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % 2 == 0:
            return False
    return True
print(is_prime(73))
print(is_prime(75))
