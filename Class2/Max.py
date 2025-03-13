# # Project 1: Create a program that will ask the amount of money in your wallet and will say if you are poor if you have less than
# # 100 in your wallet and rich if you have more than 100 in your wallet.
# money = input("How much money do you have?")
# if int(money) <= 100: 
#     print("You are poor.")
# else:
#     print("You are rich.")

# # Project 2: Create a program that will ask the user to input a number and will say if the number is odd or even.
# number = input("Please input a number.")
# if int(number)%2 == 1:
#     print("Your number is an odd number.")
# else:
#     print("Your number is an even number.")

# # Project 3: Create a program that will try to guess my favourite food
# favourite_food = ("pizza")
# user_answer = input("Guess my favourite food!")
# if user_answer == favourite_food:
#     print("Well done! You guessed it!")
# else:
#     print("Sorry, my favourite food is", favourite_food, ", better luck next time!")
# print("Thanks for playing!!")
# print(":)")

# # # Project 4: Create a program that will print what to do in front of a traffic light (red, yellow, green)
# # The input will be what colour the traffic light is
# light_colour = input("What colour is the traffic light?")
# if light_colour == ("red"):
#     print("Stop!")
#     print("Don't move forwards!")
# elif light_colour == ("yellow"):
#     l_clr = input("What colour is the light going to turn?")
#     if l_clr == ("red"):
#         print("Stop!")
#         print("Don't move forwards!")
#     elif l_clr == ("green"):
#         print("Go!")
#         print("Move forward!")
# elif light_colour == ("green"):
#     print("Go!")
#     print("Move forward!")

# Project 5: Have a bank account where a user can put in money and take out money and check their balance

loop = 1
balance = 0
while loop < 10:
    state = input("Would you like to take out money, enter money, or check your balance? ")
    if state == ("take out"):
        out_amount = input("How much would you like to take out?")
        balance = balance - out_amount
        print("You have", balance, "pounds in your account")
        state = ("bob")
    elif state == ("enter"):
        in_amount = input("How much money would you like to enter?")
        balance = balance + in_amount
        print("You have", balance, "pounds in your account")
        state = ("bob")
    elif state == ("check"):
        print("You have", balance, "pounds in your account")
        state = ("bob")