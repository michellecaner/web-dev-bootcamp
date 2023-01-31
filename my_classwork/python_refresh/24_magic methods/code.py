"""Python refresher course - Magic Methods Section"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"A person named {self.name} is {self.age} years old."

    # returns a more information-rich, or official, string representation of an object.
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)

print(bob) # this will print out a representation of the object but a magic string will change that! See lines 8 & 9
