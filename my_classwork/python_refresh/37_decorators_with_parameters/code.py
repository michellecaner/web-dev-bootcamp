"""Python refresher course - Decorators w/ Parameters Section"""

import functools

user = {"username": "Tia", "access_level": "admin"}

def make_secure(access_level): # this is like a factory which is used to create the decorator
    def decorator(func): # this is the decorator now
        @functools.wraps(func)
        def secure_function(*args, **kwargs): 
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"

        return secure_function
    return decorator

@make_secure("admin") # now this gets brackets
def get_admin_password():
    return "1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

# my brain hurts so much :(

print(get_admin_password())
print(get_dashboard_password())
