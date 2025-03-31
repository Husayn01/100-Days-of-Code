# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("./Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict = {}
for (index, row) in data.iterrows():
    dict[row.letter] = row.code
print(dict)
user_input = input("Enter your name: \n").upper()
user_list = [letter for letter in user_input]
# for item in dict:
#     if item in user_list:
#         print(f"{item}: {dict[item]}")
for letter in user_list:
    for item in dict:
        if letter == item:
            print(f"{letter}: {dict[letter]}")

