# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s
# in which the letters occur in alphabetical order. For example,
# if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. 
# If you've spent more than a few hours on this problem, 
# we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

# if "s" >= "z":
#     print("Yes")
# else:
#     print("No")


# s = 'azcbobobegghakl'
# Longest_substring = s[0]

# for i in range(len(s) - 2):
#     print(s[i])
#     print(s[i  + 1])
#     if s[i] <= s[i  + 1]:
#         Longest_substring += s[i  + 1]
#         # if Longest_substring[-1] < 
#         print(Longest_substring)
#         print("Yes")
#     else:
#         print("No")


s = 'azcbobobegghakl'  # Example input
longest = s[0]
current = s[0]

for i in range(1, len(s)):
    if s[i] >= current[-1]:
        print(current[-1])
        current += s[i]
        if len(current) > len(longest):
            longest = current
    else:
        if len(current) > len(longest):
            longest = current
        current = s[i]

# Check the last current substring after the loop ends
if len(current) > len(longest):
    longest = current

print("Longest substring in alphabetical order is:", longest)