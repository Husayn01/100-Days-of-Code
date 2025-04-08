from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
playAgain = True

def ceasar(direction_arg, text_arg, shift_arg):
    new_word = []
    for i in text:
        if i in alphabet:
            if direction == "encode":
                new_index = alphabet.index(i) + shift
            elif direction == "decode":
                new_index = alphabet.index(i) - shift
            new_index %= len(alphabet)
            new_word.append(alphabet[new_index])
        else:
            new_word.append(i)
    print(f"Here is the result: {"".join(new_word)}")
    restart = input("Enter 'yes' to play again \n").lower()
    if restart != "yes":
        playAgain = False

while playAgain:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(direction_arg= direction, text_arg=text, shift_arg=shift)

 