# Create the following Projects:

# Project 1: Create a program that will ask the amount of money in your wallet and will say if you are poor if you have less than
# 100 in your wallet and rich if you have more than 100 in your wallet.





# Project 2: Create a program that will ask the user to input a number and will say if the number is odd or even.






# Project 3: Create a program that will try to guess my favourite food





# Project 4: Create a program that will print what to do in front of a traffic light (red, yellow, green)
# The input will be what colour the traffic light is

input = "money"
input("how much money do you have?")
if input <= 100: 
    print ("you are rich")
else:
    print ("you are poor")

hidden_number=7

guess=input("Guess a number!")
if int(guess) == hidden_number:
    print("you win!")
else:
    print("try again")


favourite_food= "crisps"
if int(guess) == favourite_food:
    print("You win!")
else:
    print("try again!")
