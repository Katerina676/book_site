from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q

from .forms import ReviewForm
from .models import Book, Author, Genre


class GenreSidebar:
    def get_genres(self):
        return Genre.objects.all()


class BooksView(GenreSidebar, ListView):

    model = Book
    queryset = Book.objects.all()


class BookDetailView(GenreSidebar, DetailView):
    model = Book
    slug_field = 'url'


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())


class AuthorView(DetailView):

    model = Author
    template_name = 'books/author.html'
    slug_field = "name"


class FilterBooksView(GenreSidebar, ListView):

    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset
