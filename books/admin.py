from django.contrib import admin

from .models import Genre, Author, Book, Reviews, Rating, RatingStar


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
