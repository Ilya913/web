from django.contrib.admin.templatetags.admin_list import paginator_number
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    book_list = Book.objects.all()

    per_page = request.GET.get('per_page', 5)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5

    paginator = Paginator(book_list, per_page)

    page_number = request.GET.get('page')

    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'echo/home.html', {'books': books, 'per_page': per_page})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'echo/add_book.html', {'form': form})

def edit_book(request, id_book):
    book = get_object_or_404(Book, id_book=id_book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'echo/edit_book.html', {'form': form})

def delete_book(request, id_book):
    book = get_object_or_404(Book, id_book=id_book)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'echo/delete_book.html', {'book': book})










