# Love Calculator
# 💪 This is a difficult challenge! 💪
#
# You are going to write a
# function called calculate_love_score() that tests the
# compatibility between two names.  To work out the love
# score between two people:
#
# 1. Take both peoples names and check for the number
# 2. Then check for the number of times the
# letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and
# print it out.
#
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
#
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
#
# Example Input
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]


def calculate_love_score(name1, name2):
    name1.lower()
    name2.lower()
    concat_names = name1 + name2
    num1 = 0
    for letter in true_list:
        num1 += concat_names.count(letter)
    num2 = 0
    for letter in love_list:
        num2 += concat_names.count(letter)
    print(str(num1) + str(num2))

calculate_love_score("Kanye West", "Kim Kardashian")
