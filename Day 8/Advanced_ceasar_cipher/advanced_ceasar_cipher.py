import utils
import nltk
from nltk.corpus import words

print(utils.title)
restart_ceasar_cipher = True

# nltk.download('words')
# word_list = words.words()
# print(f"Total words: {len(word_list)}")
# print(f"First 10 words: {word_list[:10]}")


def ceasar_cipher(message_func, shift_func, command_func):
    text = ""
    global restart_ceasar_cipher
    for char in message_func:
        if not char.isalpha():
            text += char
        else:
            position = utils.alphabet.index(char)
            if command_func == "encode":
                text += utils.alphabet[position + shift_func]
            elif command_func == "decode":
                text += utils.alphabet[position - shift_func]
    if command_func not in ["encode", "decode"]:
        print("Invalid command")
    else:
        result = "encoded" if command_func == "encode" else "decoded"
        print(f"Here's the {result} result: {text}")

    restart = input("Type 'yes' if you want to go again, otherwise type 'no': \n").lower()
    if restart == "no":
        restart_ceasar_cipher = False
        print("Good bye")

while restart_ceasar_cipher:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    message = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    ceasar_cipher(message_func=message, shift_func=shift, command_func=command)

