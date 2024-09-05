import math


def paint_calc(height, width, cover):
    calc = (height * width) / cover
    print(math.ceil(calc))

h = int(input("Enter height: "))
w = int(input("Enter width: "))
coverage = int(input("Enter coverage: "))

paint_calc(height=h, width=w, cover=coverage)
