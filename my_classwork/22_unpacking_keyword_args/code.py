"""Python refresher course - Unpacking Keyword Arguments Section"""

# kwargs = keyword arguments
def named(**kwargs): # ** collects arguments
    print(kwargs)    # {'name': 'Jo', 'age': 75}

named(name="Jo", age=75) # two keyword arguments that get collected in the kwarg variable & results in a dictionary



# so confusing
def bio(name, age):
    print(name, age)

details = {"name": "Al", "age": 85}

bio(**details) # ** unpacks dictionary
