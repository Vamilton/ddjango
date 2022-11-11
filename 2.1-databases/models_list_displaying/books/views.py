from django.shortcuts import render
from .models import Book
import datetime
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)

def get_date(request):
    p_path = datetime.datetime.strptime(request.path[7:-1], '%Y-%m-%d')
    return p_path

def books_date(request, p_path):
    template = 'books/2021-01-02.html'
    all_books = Book.objects.order_by('pub_date')
    books = all_books.filter(pub_date=p_path)
    index = (*all_books,).index(books[0])
    if index != 0:
        previous_page = all_books[index-1].pub_date
    elif index == 0:
        previous_page = None
    if index != len(all_books):
        next_page = all_books[index+1].pub_date
    else:
        next_page = None


    context = {
        'books': books,
        'previous_page': previous_page,
        'next_page': next_page,
    }
    return render(request, template, context)
