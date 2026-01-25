from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

from django.shortcuts import render
from django.db.models import Q
from .models import Book
from .forms import BookForm


def book_list(request):
    query = request.GET.get("q", "")

    # Safe ORM filtering (parameterized by Django)
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )

    return render(request, "bookshelf/book_list.html", {"books": books})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # Input validation
            form.save()
    else:
        form = BookForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("relationship_app.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


@permission_required("relationship_app.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "books/create_book.html")


@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "books/edit_book.html", {"book": book})


@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("book_list")
