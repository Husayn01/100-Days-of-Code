# Write an iterative function iterPower(base, exp) that calculates the exponential 
# by simply using successive multiplication. For example, iterPower(base, exp) 
# should compute  by multiplying base times itself exp times. Write such a function below.
# This function should take in two values - base can be a float or an integer; 
# exp will be an integer  0. It should return one numerical value. 
# Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    for i in range(exp):
        result *= base
    return result

print(iterPower(2, 3))

# Write a function recurPower(base, exp) which computes  by recursively calling itself 
# to solve a smaller version of the same problem, and then multiplying the result 
# by base to solve the initial problem.
# This function should take in two values - base can be a float or an 
# integer; exp will be an integer . It should return one numerical value. 
# Your code must be recursive - use of the ** operator or looping constructs is not allowed.


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1) 
    

# The greatest common divisor of two positive integers is the largest integer 
# that divides each of them without remainder. For example,

# gcd(2, 12) = 2
# gcd(6, 12) = 6

# Write an iterative function, gcdIter(a, b), that implements this idea. 
# One easy way to do this is to begin with a test value equal to the smaller 
# of the two input arguments, and iteratively reduce this test value by 1 
# until you either reach a case where the test divides both a and b without 
# remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smallest = 0
    if a < b:
        smallest = a
    else:
        smallest = b
    while smallest > 0:
        if a % smallest == 0 and b % smallest == 0:
            return smallest
        smallest -= 1
print(gcdIter(12, 24))

