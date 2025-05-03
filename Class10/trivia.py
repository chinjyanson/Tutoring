# Katy : 1 
# Max : 10
# Serene : 0.5 

# import random

# score = random.randint(1, 10)
# print(score)

import random

def generate(input,passwords):
    i = 0
    acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
    length_of_acceptable_characters = len(acceptable_characters)
    random_password = ""
    while i < input:
        random_number = random.randint(0, length_of_acceptable_characters - 1)
        random_password = random_password + acceptable_characters[random_number]
        i = i + 1
        passwords.append(random_number)
    return 


#####################################################################################

passwords = []
generate(8,passswords)
print(passwords)




