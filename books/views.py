from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q

from .forms import ReviewForm, RatingForm
from .models import Book, Author, Genre, Rating


class GenreSidebar:
    def get_genres(self):
        return Genre.objects.all()


class BooksView(GenreSidebar, ListView):

    model = Book
    queryset = Book.objects.all()


class BookDetailView(GenreSidebar, DetailView):
    model = Book
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context


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


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                book_id=int(request.POST.get("book")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
