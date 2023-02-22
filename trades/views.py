from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

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

    def post(self, request, pk):
        if request.method == "POST":
            requested_book = get_object_or_404(Book, pk=pk)
            offering_book = get_object_or_404(Book, pk=request.POST['mybook'])
            checked = request.POST.getlist('allowchoose')
            option = True if checked else False
            TradeRequest.objects.create(
                requested_book=requested_book,
                offering_book=offering_book,
                option=option
            )
            offering_book.available = False
            offering_book.save()
            return redirect('main:index')


class RequestsListView(generic.ListView, LoginRequiredMixin):
    model = TradeRequest
    context_object_name = 'request_list'
    template_name = 'trades/requests.html'
    paginate_by = 5

    def get_queryset(self):
        return TradeRequest.objects.filter(Q(offering_book__owner_user_id=self.request.user) | Q(requested_book__owner_user_id=self.request.user))

    def post(self, request, pk):
        if 'decline' in request.POST:
            request_record = self.get_queryset()[0]
            offering_book = request_record.offering_book
            TradeRequest.objects.filter(pk=request_record.id).update(status='closed')
            offering_book.available = True
            offering_book.save()
            return redirect('trades:requests', pk)
        elif 'accept' in request.POST:
            request_record = self.get_queryset()[0]
            requested_book = request_record.requested_book
            TradeRequest.objects.filter(pk=request_record.id).update(status='traded')
            requested_book.available = False
            requested_book.save()
            return redirect('trades:requests', pk)



class OtherBookListView(generic.ListView, LoginRequiredMixin):
    model = Book
    success_url = reverse_lazy("main:index")
    context_object_name = 'other_book_list'
    template_name = 'trades/otheroption.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(Q(available=True) & Q(owner_user_id=self.kwargs.get('pk')))

    def post(self, request, pk):
        if request.method == "POST":
            offering_book = get_object_or_404(Book, pk=request.POST['theirbook'])
            trade_request = get_object_or_404(TradeRequest, Q(offering_book__owner_user_id=offering_book.owner_user_id) & Q(requested_book__owner_user_id=request.user))
            requested_book = trade_request.requested_book
            trade_request.status = 'traded'
            offering_book.available = False
            requested_book.available = False
            trade_request.save()
            offering_book.save()
            requested_book.save()
            return redirect('trades:requests', pk)