"""Python refresher course - Dictionary Comprehensions Section"""

# this is a list of tuples
users = [
    (0, "Don", "password"),
    (1, "Dex", "pw"),
    (2, "Deb", "pword"),
    (3, "Dan", "passw")
]

# we want to create a mapping of user names to user information
username_mapping = {user[1]: user for user in users}
#                   ^ this is the key value pair that will be put in your dictionary
#                   ^ it gets the user name and associates it with the entire user tuple
#                     ...and the for loop iterates over the list
print(username_mapping) # or print(username_mapping["Don"] to get one user's tuple of info)
