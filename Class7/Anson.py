# Functions
# Bonus Point

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b


# while True:
#     user_input = input("Enter a command: ")
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     if user_input == "add":
#         print(add(a, b))
#     elif user_input == "sub":
#         print(sub(a, b))
#     elif user_input == "mul":
#         print(mul(a, b))
#     elif user_input == "div":
#         print(div(a, b))
#     else:
#         print("Invalid command")



# make me a random function

def random(a, b):
    return a*2 - b*0.1 # 1*2 - 1.9*0.1 = 1.81

random_number = 1
while True:
    random_number = random(1, 1.9)
    print(random_number) # random_number = 1.81