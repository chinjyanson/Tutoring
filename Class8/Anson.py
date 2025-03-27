# Task: Make a function that checks if a number is even or not. If the number is even, return True. If the number is odd, return False.

def is_even(input):
    if input % 2 == 0:
        return True
    else:
        return False

#################################################
# 3 steps
# 1. Ignore the function def
# 2. Read up to down until you see the function -> then go to the function
# 3. Once you see a return in the function, return to where you came from


# if (is_even(2)):
#     print(is_even(3))
# else:
#     print("It is odd")


# Task: make a function that adds ! to the end of a string. For example, if the input is "Hello", the output should be "Hello!".
# def function(string):
#     return string + "!"

# print(function("run away"))
# print(function("Hello"))
# print(function("Ivan"))



# Task: make a function that takes in a name and prints out "Hello, name!"

# def say_hello(name):
#     return "Hello, " + name + "!"

# print(say_hello("Anson"))


# Task: make a fucntion takes in 3 numbers and returns the maximum number 

def max_number(a, b, c):
    if a > b:
        if a > c:
            return a
    elif b > c:
        if b > a:
            return b 
    else: 
        return c

print(max_number(1, 8, 3))
print(max_number(1, 3, 8))
print(max_number(8, 3, 1))