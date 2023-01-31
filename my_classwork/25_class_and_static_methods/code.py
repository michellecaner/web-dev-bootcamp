"""Python refresher course - Class Method & Static Method Section"""

# What do the heck do we use these for?

# Instance Methods are used for most things like when you want to produce an action that used the data inside the object you created and if you want to modify some data inside self/the object

# Class Methods are used as factories

# Static Methods are placed inside of a class b/c you feel it belongs there as you organize code



# Instance Method
class ClassTest:
    def instance_method(self): 
        print(f"Called instance_method of {self}")

test = ClassTest() # instance methods need the Class (or object) to call on them

# there are two options to call this method
test.instance_method()
# or
ClassTest.instance_method(test)
# either returns the print statement and the representation of the ClassTest object



# Class Method
class AnotherClassTest:
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}") #cls is equivalent to the class itself aka AnotherClassTest

# Static Method
    @staticmethod
    def static_method():
        print("Called static method.")

AnotherClassTest.class_method() # b/c it's not an instance method, you don't need the object to call on it



# Factories
class Book:
    TYPES = ("hardcover", "paperback") # variables aka class properties / accessed by print(Book.TYPES)

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self): # repr method used to recreate the object as a REPRESENTATION
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100) # Book.TYPES[0] automatically sets to hardcover b/c of indexing

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight) # Like above, cls IS Book - preferred use re: inheritance

book = Book.hardcover("The Chronicles of Narnia", 1500) # no need to enter type, it's automatically done w/ @classmethod
light = Book.paperback("Zen and the Art of Archery", 1000)

print(book)
print(light)

# In the example above, we're creating a factory because we want to create a new book object and avoid passing in the "hardcover" string because we only want to create new book objects that are hardcover or paperback.

