from app.schemas import Book

books = []

def get_books():
    return books

def add_book(book: Book):
    books.append(book)
    return book
