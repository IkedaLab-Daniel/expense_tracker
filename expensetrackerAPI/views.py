from django.shortcuts import render
from django.http import HttpResponse

# * Django Rest Framework 🔥
from rest_framework import generics

# * Models 🗂️
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Expense Tracker APIs!')

# * READ/WRITE @ ALL BOOKS
class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # * GET ✅
    # * POST ✅

# * GET/UPDATE/DELETE
class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
