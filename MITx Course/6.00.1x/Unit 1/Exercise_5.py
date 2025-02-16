def guess_my_number():
    print("Please think of a number between 0 and 100!")
    low = 0
    high = 100
    
    while True:
        guess = (low + high) // 2
        print("Is your secret number {}?".format(guess))
        user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if user_input == 'c':
            print("Game over. Your secret number was: {}".format(guess))
            break
        elif user_input == 'h':
            high = guess
        elif user_input == 'l':
            low = guess
        else:
            print("Sorry, I did not understand your input.")
        if low == high:
            print("Game over. Your secret number was: {}".format(low))
            break
guess_my_number()