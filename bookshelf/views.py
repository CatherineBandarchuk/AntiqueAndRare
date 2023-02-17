from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from book.models import Book

@login_required
def index(request):
    books = Book.objects.filter(owner_user_id = request.user)
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookshelf/index.html', {'page_obj': page_obj})