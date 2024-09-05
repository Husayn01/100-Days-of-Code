print("Hello"[0]) #Strings
print(len("Hello world")) #Print character length
print("Hello"[-1]) #Prints last character
print(123 + 234) #Integers
print(123_233)
print(3.142) #Float
print(True) #Boolean
print(type("Hello"), type(1234), type(3.142), type(True))
print(int("123") + int("123")) #Type conversion

name = input("Enter your name")
nameLength = len(name)
print('Number of letters in your name: ' + str(nameLength))

print("+, -, /, *, %, //, **") #Operators 

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi, 2))

score = 0
print(f"Score: {score}")
score += 1
print(f"Updated score: {score}")

