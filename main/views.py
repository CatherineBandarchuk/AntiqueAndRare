from django.shortcuts import render, redirect 
from django.core.paginator import Paginator
from django.db.models import Q
from book.models import Book, AgeGroupCategory
from account.models import CustomUser


def index(request):
    query = request.GET.get('q')
    zipcode_filter = request.GET.get('z')
    age_group = AgeGroupCategory.objects.all()
    age_group_filter = request.GET.get('age_group')

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
    elif zipcode_filter:
        users = CustomUser.objects.filter(zipcode=zipcode_filter)
        books = Book.objects.filter(owner_user_id__in=users, available=True)
    elif age_group_filter:
        if age_group_filter!='All':
            books = Book.objects.filter(age_group=age_group_filter, available=True)
    else:
        books = Book.objects.filter(available=True)
    
    sort_by = request.GET.get('sort', '-added_at')
    if sort_by:
        books = books.filter().order_by(sort_by)
    
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj, 'age_group': age_group})

def about(request):
    return render( request, 'main/about.html')

def terms(request):
    return render( request, 'main/terms.html')