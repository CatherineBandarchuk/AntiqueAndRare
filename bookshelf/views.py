from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from book.models import Book, AgeGroupCategory
from account.models import CustomUser

@login_required
def index(request):
    query = request.GET.get('q')
    age_group = AgeGroupCategory.objects.all()
    age_group_filter = request.GET.get('age_group')
    category = request.GET.get('category', 'title')
    
    category_search_check = request.GET.get('category_search')
    
    books = Book.objects.filter(owner_user_id = request.user, available=True)

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

    sort_by = request.GET.get('sort', '-added_at')
    if sort_by:
        books = books.order_by(sort_by)

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookshelf/index.html', {'page_obj': page_obj, 'age_group': age_group})