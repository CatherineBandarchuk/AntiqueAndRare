from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CreateRequestForm

from .models import TradeRequest
from book.models import Book
from django.urls import reverse_lazy


class BookListView(generic.ListView, LoginRequiredMixin):
    model = Book
    success_url = reverse_lazy("main:index")
    context_object_name = 'book_list'
    template_name = 'trades/option.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(available=True, owner_user_id=self.request.user)

    def trade(request, pk):
        requested_book = get_object_or_404(Book, pk=pk)
        bookshelf = Book.objects.filter(owner_user_id=request.user)
        offering_book = bookshelf.filter(pk=request.POST['choice'])

        new_request = TradeRequest(
            requested_book=requested_book,
            offering_book=offering_book,
        )

        new_request.save()
        return render(request, 'bookshelf/templates/bookshelf/index.html')