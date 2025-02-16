num = 10
for num in range(5):
    print(num)
print(num)
#output 5, 4

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
#output 0.o, 1.0, 2.0, 3.0, 4.0, 

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 
#output 0, 'Foo!', 4, 8, 12, 16, 'Foo!'

for letter in 'hola':
    print(letter) 
#output 'h', 'o', 'l', 'a'

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)
#ouput 'Letter # 0 is S', 1

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 