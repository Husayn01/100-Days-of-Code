alphabets = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
my_list = alphabets.split()

should_continue = True

while should_continue:
    direction = input("Type 'Encode' to encrypt, type 'Decode' to decrypt: \n").capitalize()
    text = input("Enter your message: \n").lower()
    user_shift = int(input("Enter shift number: \n"))
    output = ""


    def caesar(txt, shift, direction):
        cipher_text = ""
        new_shift = shift % 26
        for char in txt:
            if char in alphabets:
                position = alphabets.index(char)
                if direction == "Encode":
                    output = "encrypted"
                    new_position = position + new_shift
                elif direction == "Decode":
                    output = "decrypted"
                    new_position = position - new_shift
                else:
                    print(f"{direction} is not a valid input, Try again")
                    return  # Added return to exit the function if direction is invalid
                new_letter = alphabets[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char

        print(f'The {output} text is {cipher_text}')

    caesar(txt=text, shift=user_shift, direction=direction)

    result = input("Type 'yes' to go again, otherwise type 'no': ")
    if result.lower() == 'no':
            should_continue = False
