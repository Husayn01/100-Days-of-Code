student_scores = [98, 43, 56, 98, 86, 32, 65, 99, 23, 45, 87, 72, 31, 56]

total_score = 0
for score in student_scores:
    total_score += score
print(f"The sum is {total_score}")

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")

sum = 0
for i in range(1, 101):
    sum += i
print(sum)