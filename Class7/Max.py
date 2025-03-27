

while True:
    user_input = input("Enter a command: ")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if user_input == "add":
        print(add(a, b))
    elif user_input == "sub":
        print(sub(a, b))
    elif user_input == "mul":
        print(mul(a, b))
    elif user_input == "div":
        print(div(a, b))
    else:
        print("Invalid command")