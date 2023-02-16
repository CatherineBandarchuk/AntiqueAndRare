from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from book.models import Book

@login_required
def index(request):
    books = Book.objects.filter(owner_user_id = request.user)

    return render(request,'bookshelf/index.html', {
        'books': books,
    })