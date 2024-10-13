class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        return f"Title: {self.title}, Author: {self.author}"
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title)
        super().__init__(author)
        self.file_size = file_size

    def details(self):
        return f"{super().details()}, File Size: {self.file_size} MB"
    
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title)
        super().__init__(author)
        self.page_count = page_count

    def details(self):
        return f"{super().details()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.details(self))

my_library = Library()
my_library.add_book()
my_library.list_books()

