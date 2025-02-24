# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here
# For example,

# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

def closest_power(base, num):
    exp = 0
    while base ** exp < num:
        exp += 1
    if exp == 0:
        return 0
    lower_value = base ** (exp - 1)
    higher_value = base ** exp
    if abs(higher_value - num) < abs(num - lower_value):
        return exp
    else:
        return exp - 1
print(closest_power(4,1))