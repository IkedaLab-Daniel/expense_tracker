from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('books/', views.BooksView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('books/category/<int:category_id>', views.BookByCategoryView.as_view()),
    path('books/expenses/', views.TotalExpensesView.as_view()),
    # ? User management - Assign Group to User
    path('users/<int:pk>/groups/', views.UserGroupUpdateView.as_view()), 
        # ? PATCH Only. 
        # ? { "groups": ["editors"] }
        # ? if no payload, remove user to all groups
]

# * DJOSER
# * Register: /auth/users/
# * Login: /auth/token/login
# * Logout: /auth/token/logout

# * Assign user to groups: 
# * http://127.0.0.1:8000/api/users/#/groups/ 
# * where # is an int for user's id