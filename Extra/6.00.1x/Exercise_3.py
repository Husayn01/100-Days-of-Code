# 1. Convert the following into code that uses a while loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

num = 2
while num in range(11):
    print(num)
    num += 2
print("Goodbye!")

# 2. Convert the following into code that uses a while loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
myNum = 10
while myNum >= 2:
    print(myNum)
    myNum -= 2

# 3. Write a while loop that sums the values 1 through end, inclusive. end 
# is a variable that we define for you. So, for example,
# if we define end to be 6, your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# current = 1
# total = 0
# end = 6
# while current in range(end + 1):
#     total += current
#     current += 1
# print(total)

# 1. Convert the following code into code that uses a for loop.
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

for n in range(2,11,2):
    print(n)
print("Goodbye!")

# 2. Convert the following code into code that uses a for loop.
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
for n in range(10,1,-2):
        print(n)

# 3. Write a for loop that sums the values 1 through end, inclusive. 
# end is a variable that we define for you. So, for example, if we define end to be 6, 
# your code should print out the result:
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

end = 6
total = 0
for i in range(1,end + 1):
     total += i
print(total)