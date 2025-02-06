# # Task 0:
# # Here is an array: [1, 2, 3, 4, 5]
# # Print the Length of the array

# arr = [1, 2, 3, 4, 5]
# print(len(arr))

# # Task 1: 
# # Here is an array: ["Max","Adam", "Bob", "Peter"]
# # Print every element in this array

# arr = ["Max","Adam", "Bob", "Peter"]
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])

# # Task 2: 
# # Here is an array: [3, 1, 4, 3, 1, 5]
# # I want you to check if the 3 element in the array is equal to the 4th element in the array
# # Print "Success" if they are equal and "Failure" if they are not

# arr = [3, 1, 4, 3, 1, 5]
# if arr[2] == arr [3]:
#     print("Sucess!")
# else:
#     print("Faliure!")

# # Task 3: 
# # Here is an array: [1, 2, 3, 4, 5]
# # Change the first element in the array to 10

# arr = [1, 2, 3, 4, 5]
# arr [0] = 10

# # Task 4:
# # Here is an array: [1, 2, 3, 4, 5]
# # Add 6 to the end of the array

# arr = [1, 2, 3, 4, 5]
# arr.append(6)

# # Task 5: 
# # Here is an array: [1, 2, 3, 4, 5]
# # Remove the first element in the array

# arr = [1, 2, 3, 4, 5]
# arr.pop(0)




arr = [1,2,3,4,5]           # The array is 1, 2, 3, 4, 5
Number = 0                  # Variable 'Number' is 0
while Number < len(arr):    # While the variable 'Number' is smaller than the length of the array
    print(arr[Number])      # Print the 'Number'th number in the array
    Number = Number + 1


# len(arr) # to access the length of the array
# arr.append(6) # to add 6 to the end of the array
# arr.pop(0) # to remove the first element in the array
# print(arr[0]) # index the 0th element