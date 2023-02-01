"""Python refresher course - @ Syntax for Decorators Section"""
import functools #use this all the time on the inner function of the decorator


user = {"username": "Tia", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func) # functools is a wrapper for func so it keeps the name/documentation of get_admin_password()
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

# the @make_secure can replace this: get_admin_password = make_secure(get_admin_password)
# putting this on top of a function definition prevents the function from being created as is & instead will create it & pass it through the decorator in one go
@make_secure
def get_admin_password():
    return "1234"


# get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
