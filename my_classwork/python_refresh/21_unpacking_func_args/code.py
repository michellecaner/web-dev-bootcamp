"""Python refresher course - Unpacking Function Arguments Section"""

def multiply(*args): # function has a set of args that will be collected into a tuple of args when it's called
    print(args)
    total = 1 
    for arg in args:          
        total = total * arg   # UGH, this is confusing me

    return total

print(multiply(1, 3, 5)) # a tuple of three arguments



# and here we are destructuring the nums list
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums)) # this splits up the nums variable and assigns 3 to x and 5 to y
                  # without the asterisk, you'll get an error b/c y won't have a value; it'll assign 3 & 5 to x



# this one is more complex
def subtract(x, y):
    return x - y

numbers = {"x": 20, "y": 5} # a dictionary with two keys which we will pass through as a named argument
print(subtract(**numbers))


# and even more complex:
def multiply_again(*args): # function has a set of args that will be collected into a tuple of args when it's called
    total = 1 
    for arg in args:          
        total = total * arg   # UGH, this is confusing me

    return total

# this func collects all the positional args into the args tuple & also require a named arg (operator)
def apply(*args, operator):
    if operator == "*":
        return multiply_again(*args) # adding this asterisk is important - it unpacks the tuple to individ. elements
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="*"))
