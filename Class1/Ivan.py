hidden_number = 7

guess = input("Guess a number")
if int(guess) == hidden_number:
    print("You win!")
else:
    print("try again")