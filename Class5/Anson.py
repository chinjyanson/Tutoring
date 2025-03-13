# Project Create a Banking System
# This banking system should be able to add money, take out money and check the balance of the account based on the user's input.

# money = 0
# while True: 
#     user_input = input("Would you like to take out money, enter money, or check your balance? ")
#     if user_input == "take out money":
#         money = money - 50
#     if user_input == "put in money":
#         money = money + 50
#     if user_input == "check balance":
#         print("You have", money, "pounds in your account")


# Extension task: Unique Counter
# Create a program that will count from 1 then 100 then 2 then 99 then 3 then 98 and so on until 100 and 1

# i = 0
# j = 0
# while i < 50: 
#     while j < 100-i:
#         j = j + 1  
#         print(j)
#     i = i + 1


# Extension task 2: 
# I have given you an array: [3, 1, 4, 2, 5, 19, 2, 1]
# I want you to find me the maximum element and the minimum element in the array
max_element = 0
min_element = 10000000000000

arr = [3, 1, 4, 2, 5, 19, 2, 1]

while i < len(arr):
    if arr[i] > max_element:
        max_element = arr[i]
    if arr[i] < min_element:
        min_element = arr[i]
    i = i + 1


# Extension task 3:
# I want you to sort the same array in ascending order
arr = [3, 1, 4]

if arr[0] > arr[1]:
    tmp = arr[0] #temporary tmp variable 
    arr[0] = arr[1]
    arr[1] = tmp
if arr[1] > arr[2]:
    tmp = arr[1]
    arr[1] = arr[2]  
    arr[2] = tmp

input()
print() # functions
[] # arrays



