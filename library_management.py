class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"{self.title} - {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    print("Book is already issued.")
                else:
                    book.is_issued = True
                    print("Book issued successfully.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    def display_books(self):
        print("\n===== LIBRARY BOOKS =====")

        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display()


library = Library()

library.add_book("Python Programming", "John Smith")
library.add_book("Data Science Basics", "David Brown")
library.add_book("Cyber Security", "Robert Wilson")

library.display_books()

library.issue_book("Python Programming")

library.display_books()

library.return_book("Python Programming")

library.display_books()

library.remove_book("Cyber Security")

library.display_books()