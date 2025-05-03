# Task 1: Create a program that uses a for loop to print the numbers 1 to 10, but skips the number 5.

for i in range(1, 11):
    if i != 5:
        print(i)

# Task 2: Create a program that finds the maximum number in an array (but without using the max() function).

arr = [1, 6, 1, 8, 1, 9, 1, 94, 3, 795, 368]
max_num = -float('inf')
for i in arr:
    if i > max_num:
        i = max_num
print(max_num)



# Task 3: Create a program that prints the string "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both 3 and 5, from 1 to 100.

for i in range(1, 101):
    if i % 5 and i % 3:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")


# Task 4: Create a program that reverses a string. E.g: "Anson" should become "nosnA".

name = "Bob"
for i in range(len(name)):
    






