class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def info(self):
        return f"{self.name} by {self.author}"
    
    def __repr__(self):
        return self.name


class LibraryBook(Book):
    
    def __init__(self, name, author, inventory):
        super().__init__(name, author)
        self.inventory = inventory


class Library(LibraryBook):

    def __init__(self, book):
        self.borrowers = []
        self.book = book

    def borrow(self, name):
        self.book.inventory -= 1
        self.borrowers.append(name)
