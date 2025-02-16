# Write a Python function, square, that takes in one number 
# and returns the square of that number.
# This function takes in one number and returns one number.

def square(x):
    '''
    x: int or float.
    '''
    return x ** 2

# Write a Python function, evalQuadratic(a, b, c, x), 
# that returns the value of the quadratic .
# This function takes in four numbers and returns a single number.
# Code Editor

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return ((a * x**2) + (b * x) + c)