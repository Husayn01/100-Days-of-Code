temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable") 
else:
   print("Cold")

# Write a piece of Python code that prints out the string 'hello world'
# if the value of an integer variable, happy, is strictly greater than 2.
happy = 5
if happy > 2:
   print("Hello world")

# ####
# num = 5
# if num > 2:
#     print(num)
#     num -= 1
# print(num)

###
myNum = 0
while myNum <= 5:
    print(myNum)
    myNum += 1

print("Outside of loop")
print(myNum) 
##output 0,1,2,3,5,"Outside of loop",6


# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))
# #output infinite loop

# num = 10
# while num > 3:
#     num -= 1
#     print(num) 
# #output 9, 8, 7, 6, 5, 4, 3

# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')
# ##Output 10, 9, 8, 7, 'Breaking out of loop','Outside of loop'

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))
#Output 