"""Python refresher course - Type Hinting in Python 3.5+ Section"""

from typing import List # need to import to get Line 13 working / can import tuples, sets, etc...


def list_avg(sequence):
    return sum(sequence) / len(sequence)
  
# this will give an error because you can;t get a sum of 123 or the length - the elements need to be in a string
list_avg(123)



# so, we can use type hints to provide some info
def list_avg_2(sequence: List) -> float: # this tells us the sequence needs to be in a list and to return a float
    return sum(sequence) / len(sequence)

list_avg_2(123) # not sure what the correct answer is though....



# you can use type hints anywhere apparently
class Book2:
    def __init__(self, name: str, page_count: int): # like here
        self.name = name
        self.page_count = page_count



# here's another example of type hinting
class BookShelf:
    def __init__(self, books: List[Book2]): # defines that books should be a LIST of BOOK OBJECTS
        self.books = books

    def __str__(self) -> str: # this signals that we want a string returned
        return f"This bookshelf has {len(self.books)} books."



# and another
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int): # type hints
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str: #more
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book": # hint for returning the Book object you're already in
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int):
        return cls(name, cls.TYPES[1], page_weight)