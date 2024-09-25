line1 = ['o', 'o', 'o']
line2 = ['o', 'o', 'o']
line3 = ['o', 'o', 'o']
lineMap = [line1, line2, line3]

print("Initial map:")
for row in lineMap:
    print(" ".join(row))

print("Hiding your treasure, X marks the spot")
position = input('Where do you want to hide your treasure? \n')

if len(position) != 2 or not position[0].isalpha() or not position[1].isdigit():
    print("Invalid input. Please enter a letter followed by a number (e.g., a1, b2)")
else:
    x = position[0].lower()
    y = int(position[1]) - 1  # Convert to 0-based index

    if x == 'a':
        row_index = 0
    elif x == 'b':
        row_index = 1
    else:
        row_index = 2

    lineMap[y][row_index] = 'X'

    print("Treasure hidden at:", position)
    print("Updated map:")
    for row in lineMap:
        print(" ".join(row))