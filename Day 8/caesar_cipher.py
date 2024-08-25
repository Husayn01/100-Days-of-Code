title = """                                                   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                       
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(title)
restart_ceasar_cipher = True


def ceasar_cipher(message_func, shift_func, command_func):
    text = ""
    global restart_ceasar_cipher
    for char in message_func:
        if not char.isalpha():
            text += char
        else:
            position = alphabet.index(char)
            if command_func == "encode":
                text += alphabet[position + shift_func]
            elif command_func == "decode":
                text += alphabet[position - shift_func]
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

