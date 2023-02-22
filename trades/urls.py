from django.urls import path

from . import views

app_name = 'trades'

urlpatterns = [
    path('account/other/<int:pk>/', views.OtherBookListView.as_view(), name='selectother'),
    path('account/<int:pk>/', views.RequestsListView.as_view(), name='requests'),
    path('<int:pk>/', views.BookListView.as_view(), name='select'),
]