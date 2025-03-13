# while loops

# Task1: Print a simple counter that counts from 1 to 10
i = 1 
while i < 10: 
    print(i)
    i = i + 1

# Task2: Print a simple counter that counts from 10 to 1
i = 10
while i > 0:
    print(i)
    i = i - 1

# Task3: Print a simple counter that counts from 1 to 10 but only print the even numbers

i = 10
while i > 0:
    if i % 2 == 0:
        print(i)
    i = i - 1

# Task4: Use the array [1, 2, 3, 4, 5] and print each element in the array

arr = [1, 2, 3, 4, 5]
i = 0
while i < len(arr) + 1:
    print(arr[i])

# Task5: Use the array [1, 2, 3, 4, 5] and print each element in the array but only print the even numbers

arr = [1, 2, 3, 4, 5]
x = 0
while x < len(arr) + 1:
    if arr[x] % 2 == 0:
        print(arr[x])
    x = x + 1

# Project 1: Addition Calculator

loop = 1
total = int(input("Please choose a number: "))
while loop < 10:
    a = int(input("Please choose another number: "))
    total = a + total
    print(total)

# Project 2: Calculation 

loop = 1 
total = float(input("Please choose a number: "))
while loop < 10:
    sign = input("Would you like to add, subtract, multiply or divide? ")
    if sign == "add":
        a = float(input("Please choose another number: "))
        total = a + total
        print(total)
    if sign == "subtract":
        a = float(input("Please choose another number: "))
        total = total - a
        print(total)
    if sign == "multiply":
        a = float(input("Please choose another number: "))
        total = total * a
        print(total)
    if sign == "divide":
        a = float(input("Please choose another number: "))
        total = total / a
        print(total)

