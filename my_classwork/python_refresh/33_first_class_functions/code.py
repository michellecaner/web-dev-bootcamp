"""Python refresher course - First Class Functions Section"""

# these are functions that are just variables that you can pass to other functions??? WTF.

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator): # takes any # of arguments & collects into a tuple and mandatory keyword arg param
    return operator(*values) # then it takes the operator function with the values as individual args - WOT

# WACKADOO
result = calculate(20, 4, operator=divide)
# we pass in our number of values arguments first with 20 being the dividend and 4 being the divider
# however, if you put in more numbers, it will throw you an error
# then set our operator to the divide function value (not the actual function)
print(result)



# let's get even more confused
# this function uses two parameters to find another parameter
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")
  
friends = [
  {"name": "Flo Rida", "age": 40},
  {"name": "June Bug", "age": 30},
  {"name": "Ben Dover", "age": 40}
]

# first, we have to run a function that returns a name
def get_friend_name(friend):
    return friend["name"]

# calling the search function and passing in friends variable as a sequence
# search will iterate over friends list and look for "Di Hard" aka the expected value
# get_friend_name aka the finder function will extract the names
print(search(friends, "Di Hard", get_friend_name))
 