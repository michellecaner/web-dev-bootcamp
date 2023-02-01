"""Python refresher course - Simple Decorators Section"""

# decorators let us easily modify functions

user = {"username": "Tia", "access_level": "guest"}

# this function is not secure and we could easily get the password
def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function(): # no parameters, is the function that checks & calls back/defines the og function
        if user["access_level"] == "admin":
            return func() # og function is get_admin_password
        else:
            return f"No admin permission for {user['username']}"

    return secure_function # this is the decorator / returns the function - NOT THE CALL (no paren)

# make_secure function is called & passed get_admin_password, the function we want to make secure
get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
