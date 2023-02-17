from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import NewBookForm

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'book/detail.html', {
        'book': book
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            #book.owner_user_id = request.user
            book.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = NewBookForm()

    return render(request, 'book/form.html', {
        'form': form,
        'title': 'New Book',
    })

@login_required
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk, owner_user_id=request.user)
    book.delete()
    print("delete")
    return redirect('bookshelf:index')