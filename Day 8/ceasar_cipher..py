from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
new_word = []

def encrpyt(direction_arg, text_arg, shift_arg):
    for i in text:
        if i in alphabet:
            new_index = alphabet.index(i) + shift
            new_word.append(alphabet[new_index])
            print(alphabet.index(i) + shift)
    print("".join(new_word))
encrpyt(direction_arg= direction, text_arg=text, shift_arg=shift)

 