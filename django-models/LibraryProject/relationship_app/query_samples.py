from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("Books by Author:", books_by_author)
print("Books in Library:", library_books)
print("Librarian:", librarian.name)
