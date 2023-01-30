"""Python refresher course - Lambda Functions Section"""

# this is an unnamed lambda function
lambda x, y: x + y()



# this is a named lambda function that actually prints a statement
add = lambda x, y: x + y

print(add(5, 7))



# and this supposedly is another way of doing the above:
print((lambda x, y: x + y)(5, 7))



# using lambda functions & list comprehension
def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence] # using list comprehension with the double function

print(doubled)



# using lambda functions with map instead of the above
def times_two(y):
    return y * 2

numbers = [11, 13, 15, 19]
# multiplied = [times_two(y) for y in numbers]
multiplied = map(times_two, numbers) # this isn't working like I thought...it's supposed to replicate the line above?

print(multiplied)



# and to confuse myself even more:
digits = [2, 4, 6, 8]
mathing = [(lambda x: x * 2)(x) for x in digits]
mathing = list(map(lambda x: x * 2, digits)) # WOT
