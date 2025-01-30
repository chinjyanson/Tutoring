hidden_number = 2

guess = input("Guess a number: ")
if int(guess) == hidden_number:
    print("You win!")
else:
    print("Try again")