from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum
# * Django Rest Framework 🔥
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
# * Models 🗂️
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer, UserRoleSerializer

# * Pagination Class
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_description = 'page_size'
    max_page_size = 100

def home(request):
    return HttpResponse('Welcome to Expense Tracker APIs!')

# * READ/WRITE @ ALL BOOKS
class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    ordering_fields = ['title', 'distribution_expense']
    ordering = []
    # * GET ✅
    # * POST ✅

# * GET/UPDATE/DELETE
class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# * GET total expenses
class TotalExpensesView(APIView):
    def get(self, request):
        total_expense = Book.objects.aggregate(total=Sum('distribution_expense'))['total'] or 0
        return Response({"total_expenses": total_expense})

# * Admin will assign user to group "editors"
class UserGroupUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAdminUser]