# How it works:
# First, the user is asked to enter a password for each site.
# Then, the program asks for the master password.
# If the master password is correct, it shows all the saved passwords.
# If the password is wrong, it says “Access Denied.”



sites = ["Gmail", "Instagram", "Roblox", "YouTube", "Discord"]
passwords = []
master_password = "123456"
passwords.append(input("Password for " + sites[0] + "?"))
passwords.append(input("Password for " + sites[1] + "?"))
passwords.append(input("Password for " + sites[2] + "?"))
passwords.append(input("Password for " + sites[3] + "?"))
passwords.append(input("Password for " + sites[4] + "?"))
m_password = input("What is the master password?")
if m_password == master_password:
    print(passwords)
else:
    print("Access denied!")







# project 2:
# make a password generator that generates a random password of a given length. The password length should be 8 characters long.

length = int(input("How long do you want your password to be?"))
acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
length_of_acceptable_characters = len(acceptable_characters)
random_password = ""
i = 0
while i < length - 1: 
    random_number = random.randint(0, length_of_acceptable_characters - 1)
    random_password = random_password + acceptable_characters[random_number]
    i = i + 1
print(random_password)