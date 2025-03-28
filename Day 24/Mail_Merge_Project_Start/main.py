#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDDER = "[name]"
with open("C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 24/Mail_Merge_Project_Start/Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    print(names_list)

with open("C:/Users/Hussaini/Desktop/100-Days-of-Code/Day 24/Mail_Merge_Project_Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names_list:
        new_letter = letter_content.replace(PLACEHOLDDER, name.strip())
        print(new_letter)

        with open(f"./Output/Ready/letter_for_{name.strip()}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)