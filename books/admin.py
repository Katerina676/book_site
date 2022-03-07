from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Genre, Author, Book, Reviews, Rating, RatingStar


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50", heigth="60"')

    get_image.short_description = 'Фотография'


class ReviewInline(admin.TabularInline):

    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'genres', 'url', 'author')
    list_filter = ('genres', 'year')
    search_fields = ('title', 'year')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "cover")
        }),
        (None, {
            "fields": (("year", "author"),)
        })
    )



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = ('name', 'url')


admin.site.register(RatingStar)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('book', 'star')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'parent', 'book', 'id')
    readonly_fields = ('name', 'email')



