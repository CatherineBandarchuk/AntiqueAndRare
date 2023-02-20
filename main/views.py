from django.shortcuts import render 
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
    
    zipcode_search_check = request.GET.get('zipcode_search')
    category_search_check = request.GET.get('category_search')
    
    books = Book.objects.filter(available=True)

    if age_group_filter:
        if age_group_filter!='All':
            books = books.filter(age_group=age_group_filter)

    if query and category_search_check:
        if category == 'title':
            books = books.filter(title__icontains=query)
        elif category == 'author':
            books = books.filter(author__icontains=query)
        elif category == 'language':
            books = books.filter(language__icontains=query)
        elif category == 'genre':
            books = books.filter(genre__icontains=query)
        elif category == 'isbn':
            books = books.filter(isbn__icontains=query)
    
    if zipcode_filter and zipcode_search_check:
        users = CustomUser.objects.filter(zipcode=zipcode_filter)
        books = books.filter(owner_user_id__in=users, available=True)

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