"""Python refresher course - Default Parameter Values Section"""

def add(x, y=8): # setting y with a default parameter
    print(x + y)

add(5) # 5 is x and we don't need to put a value for y since it has a default



def add_another(x, y=8):
    print(x + y)

add(5, 4) # y can be reassigned this way