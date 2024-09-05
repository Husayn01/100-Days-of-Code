totalNum = 0
for n in range(1, 101):
    totalNum += n
print(totalNum)

target = int(input('Enter your target number: \n'))
num = 0
for n in range(1, target + 1, 2):
    num += n
print(num)