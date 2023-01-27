"""Python refresher course - Functions Returning Values Section"""

def add(x, y):
    print(x + y)

add(5, 8) # prints out 13
# result = add(5, 8) # adds to 13 • Assigning result of a function call, where the function has no return
# print(result) # functions return a value of None by default - weird



# INSTEAD!
def addition(x, y):
    print (x + y)
    return x + y

addition(5, 8)
answer = addition(5, 8)
print(answer)


