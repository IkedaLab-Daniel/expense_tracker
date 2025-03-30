from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('books/', views.BooksView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
]