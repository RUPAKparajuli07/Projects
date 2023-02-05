from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False
        self.due_date = None

    def borrow(self):
        if self.borrowed:
            print("Book is already borrowed")
        else:
            self.borrowed = True
            self.due_date = datetime.now() + timedelta(days=14)
            print("Book has been borrowed, due date:", self.due_date.strftime("%Y-%m-%d"))

    def return_book(self, return_date):
        if self.borrowed:
            if return_date > self.due_date:
                print("Late return, fine imposed")
            else:
                self.borrowed = False
                self.due_date = None
                print("Book has been returned")
        else:
            print("Book was not borrowed")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("List of books:")
        for i, book in enumerate(self.books):
            print(i+1, book.title)

    def search_book(self, book_code):
        for i, book in enumerate(self.books):
            if i+1 == book_code:
                return book
        return None

library = Library()
book1 = Book("Pride and Prejudice", "Jane Austen", "1000")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1000")
library.add_book(book1)
library.add_book(book2)

while True:
    library.list_books()
    user_input = input("Enter the book code number (or 'q' to quit): ")
    if user_input == 'q':
        break

    try:
        book_code = int(user_input)
        book = library.search_book(book_code)
        if book:
            print("Book found:", book.title)
            if book.borrowed:
                return_date = input("Enter return date (YYYY-MM-DD): ")
                return_date = datetime.strptime(return_date, "%Y-%m-%d")
                book.return_book(return_date)
            else:
                book.borrow()
        else:
            print("Book not found")
    except ValueError:
        print("Invalid input")

    choice = input("Do you want to search for another book? (y/n): ")
    if choice == 'n':
        break
