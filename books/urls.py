from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksView.as_view()),
    path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('filter/', views.FilterBooksView.as_view(), name='filter'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('author/<str:slug>/', views.AuthorView.as_view(), name='author_detail'),
]