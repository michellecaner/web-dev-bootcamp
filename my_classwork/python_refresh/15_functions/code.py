"""Python refresher course - Functions Section"""

# the most simple function
def hello():
    print("Hello!")

hello() # calling the function



def user_age_in_seconds():
    user_age = int(input("What is your age?" ))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age is seconds is {age_in_seconds}!")

user_age_in_seconds()
