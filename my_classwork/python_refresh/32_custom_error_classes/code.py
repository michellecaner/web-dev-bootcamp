"""Python refresher course - Custom Error Classes Section"""

class TooManyPagesError(ValueError): # inheriting from built in ValueError or Exception Class
    pass

class Book:
    def __init__(self, name: str, page_count: int): # using type hinting
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
          f"<Book Name: {self.name}, Page Count: {self.page_count}, Amount Read: {self.pages_read}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesError("The number of pages doesn't exist.")
        self.pages_read += pages
        print(f"You have read {self.pages_read} out of {self.page_count}.")

python101 = Book("Python 101", 50)

# returns a nice, readable message back to the user
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesError as e:
    print(e)
