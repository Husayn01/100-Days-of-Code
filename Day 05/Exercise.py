# Input students Height
studentHeight = input().split()
for n in range(0, len(studentHeight)):
    studentHeight[n] = int(studentHeight[n])

totalHeight = 0
average = 0
for height in studentHeight:
    totalHeight += height
    average = totalHeight / len(studentHeight)
print(studentHeight)
print(f'Total Height: {totalHeight}')
print(f'Number of Students: {len(studentHeight)}')
print(f'Average Height: {average}')