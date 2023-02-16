from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.delete, name='delete'),
]