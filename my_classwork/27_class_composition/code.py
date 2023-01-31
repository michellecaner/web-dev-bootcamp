"""Python refresher course - Class Composition Section"""

class Bookshelf:
    def __init__(self, *books): # *books will allow us to take in a number of books
        self.books = books

    def __str__(self):
        return f"My bookshelf has {len(self.books)} books." # this will give us the quantity



# Book does not necessarily need to inherit from Bookshelf
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This book's title is called {self.name}."

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = Bookshelf(book, book2)

print(shelf) # My bookshelf has 2 books. YEESH.

# Additionally, you can now also access shelf.books which gives you all the books stored on the bookshelf.
print(shelf.books)