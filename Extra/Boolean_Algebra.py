#De Morgan's law:
numbers = list(range(1, 21))
filtered_numbers = [x for x in numbers if (x % 3 != 0 and x % 5 != 0)]
print(filtered_numbers)

#Absorption Law
numbers = list(range(1, 21))
filtered_numbers = [x for x in numbers if x % 2 == 0 or (x % 2 == 0 and x > 10)]
print(filtered_numbers)
