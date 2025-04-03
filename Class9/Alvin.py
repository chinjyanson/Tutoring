sites = ["gmail", "instagram", "Discord", "youtube"]
passwords = ["1", "2", "3", "4"]
master_password = 1234
i = 0 
while i < len(sites):
    passwords[i] = input("Password for " + sites[i] + "?: ")
    i = i + 1