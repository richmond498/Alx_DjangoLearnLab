---

# Create Operation

````python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book




# 📄 retrieve.md

```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year




### 📄 `update.md`

```markdown
## Update Book Record

### Command
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
````
