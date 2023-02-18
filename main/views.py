from django.shortcuts import render, redirect 
from django.core.paginator import Paginator
from django.db.models import Q
from book.models import Book
from account.models import CustomUser


def index(request):
    query = request.GET.get('q')
    category = request.GET.get('category', 'title')
    if query:
        if category == 'title':
            books = Book.objects.filter(title__icontains=query, available=True)
        elif category == 'author':
            books = Book.objects.filter(author__icontains=query, available=True)
        elif category == 'language':
            books = Book.objects.filter(language__icontains=query, available=True)
        elif category == 'genre':
            books = Book.objects.filter(genre__icontains=query, available=True)
        elif category == 'isbn':
            books = Book.objects.filter(isbn__icontains=query, available=True)
        else:
            books = Book.objects.none()
    else:
        zipcode = request.GET.get('z')
        if zipcode:
            users = CustomUser.objects.filter(zipcode=zipcode)
            books = Book.objects.filter(owner_user_id__in=users, available=True)
        else:
            books = Book.objects.filter(available=True)
    
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj})

def about(request):
    return render( request, 'main/about.html')