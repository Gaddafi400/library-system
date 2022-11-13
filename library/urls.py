from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path("", views.index, name="home"),
    
    path("books/", views.book_list_search, name="book-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    
    # path("searchbook", views.search, name="book-search"),
    
    path("loanbook", views.LoanBookListView.as_view(), name="loan-list"),
    path("loanbook/<int:pk>/", views.LoanBookView.as_view(), name="loan-book"),
    path('loandelete/<int:pk>/', views.LoanBookDeleteView.as_view(), name='loan-delete'),
    
    path("userprofile/", views.UserProfileListView.as_view(), name="userprofile"),
    path("userprofile/<int:pk>", views.UserProfileUpdateView.as_view(), name="userprofile-update"),
]
