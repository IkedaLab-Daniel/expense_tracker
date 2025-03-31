from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# * Django Rest Framework 🔥
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# * Models 🗂️
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer, UserRoleSerializer

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Expense Tracker APIs!')

# * READ/WRITE @ ALL BOOKS
class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # * GET ✅
    # * POST ✅

# * GET/UPDATE/DELETE
class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# * Admin will assign user to group "editors"
class UserGroupUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAdminUser]