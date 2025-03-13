
# Extension task: Unique Counter
# Create a program that will count from 1 then 100 then 2 then 99 then 3 then 98 and so on until 100 and 1

# i = 0
# while i < 100:
#     i = i + 1  
#     print(i)
#     print(100 - i + 1)

# Extension task 2: 
# I have given you an array: [3, 1, 4, 2, 5, 19, 2, 1]
# I want you to find me the maximum element and the minimum element in the array

arr = [20, 1, 4, 2, 5, 19, 2, 1]
arr_len = len(arr)
num = 1
high_num = arr[0]
small_num = arr[0]
while num < arr_len:
    if arr[num] > high_num:
        high_num = arr[num]
    if arr [num] < small_num:
        small_num = arr[num]
    num = num + 1
print(high_num)
print(small_num)




# Extension task 3:
# I want you to sort the same array in ascending order

arr = [3, 1, 4]
if arr[0] > arr[1]:
    tmp = arr[0]
    arr[0] = arr[1]
    arr[1] = tmp
if arr[1] > arr[2]:
    tmp = arr[1]
    arr[1] = arr[2]
    arr[2] = tmp
