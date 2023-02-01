"""Python refresher course - Decorating Functions w/ Parameters Section"""

import functools 

user = {"username": "Tia", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs): # so this decorator can be used on other functions and take any arguments
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

# changing things up here and I'm SO lost
def get_password(panel): # he said panel is the decorator???
    if panel == "admin": # wtf is panel???
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))
