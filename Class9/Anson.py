# import random

# # Arrays and Strings:
# # What happens if I do this?
# # a = "strings"
# # print(a[2]) # you can index for strings

# # How to use the random module:
# # import random

# # print(random.randint(1, 10)) # returns a random integer between 1 and 10
# # random.choice(["apple", "banana", "cherry"]) # returns a random element from the list
# # random.shuffle(["apple", "banana", "cherry"]) # shuffles the list in place



# # project 1:
# # This project is like a mini password manager. It stores passwords for 5 different websites (like Gmail, Instagram, Roblox, YouTube, and Discord). But there’s a twist — you can only see the saved passwords if you enter the correct master password!
# # How it works:
# # First, the user is asked to enter a password for each site.
# # Then, the program asks for the master password.
# # If the master password is correct, it shows all the saved passwords.
# # If the password is wrong, it says “Access Denied.”


sites = ["Gmail", "Instagram", "Roblox", "YouTube", "Discord"]
passwords = ["", "", "", "", ""]
master_password = "1234"  # This is the master password

i = 0 
while i < len(sites):
    passwords[i] = input("Password for " + sites[i] + "?: ")
    i = i + 1

user_input = input("What is the master password?")
if user_input == master_password:
    print("Access granted!")
    print("Your passwords are:")
    i = 0
    while i < len(sites):
        print(sites[i] + ": " + passwords[i])
        i = i + 1
else:
    print("Access denied!")
    print("You entered the wrong password!")



# project 2:
# make a password generator that generates a random password of a given length. The password length should be 8 characters long.
# You should be able to use 



acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
length_of_acceptable_characters = len(acceptable_characters)
random_password = ""

i = 0
while i < 80: 
    random_number = random.randint(0, length_of_acceptable_characters - 1)
    random_password = random_password + acceptable_characters[random_number]
    i = i + 1

print(random_password)

def generate(input, passwords):
    i = 0
    random_password = ""
    while i < input:
        random_number = random.randint(0, length_of_acceptable_characters - 1)
        random_password = random_password + acceptable_characters[random_number]
        i = i + 1
        passwords.append(random_number)
    return passwords

###################################################################################

import random
acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
length_of_acceptable_characters = len(acceptable_characters)
sites = ["Gmail", "Instagram", "Roblox", "YouTube", "Discord"]
passwords = []
master_password = "123456"
random_number = "" # interesting
num_of_sites = len(sites)
b = 0
while b < num_of_sites:
    passwords = generate(8, passwords)
m_password = input("What is the master password?")
if m_password == master_password:
    print(passwords)
else:
    print("Access denied!")



