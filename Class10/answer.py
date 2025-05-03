import random

sites = ["Gmail", "Instagram", "Roblox", "YouTube", "Discord"]
passwords = ["", "", "", "", ""]
master_password = "1234"  # This is the master password

i = 0 
while i < len(sites):
    acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
    length_of_acceptable_characters = len(acceptable_characters)
    random_password = ""

    j = 0
    while j < 80: 
        random_number = random.randint(0, length_of_acceptable_characters - 1)
        random_password = random_password + acceptable_characters[random_number]
        j = j + 1

    passwords[i] = random_password
    i = i + 1

user_input = input("What is the master password?")
if user_input == master_password:
    print("Access granted!")
    print("Your passwords are:")
    i = 0
    while i < len(sites):
        print(sites[i] + ": " + passwords[i])
        i = i + 1