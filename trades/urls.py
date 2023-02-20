from django.urls import path

from . import views

app_name = 'trades'

urlpatterns = [
    path('<int:pk>/', views.BookListView.as_view(), name='select'),
]