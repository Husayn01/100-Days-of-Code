scores = input().split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])

highestScore = 0
for score in scores:
    if score > highestScore:
        highestScore = score
print(f'Highest Score: {highestScore}')
