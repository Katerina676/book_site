from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='authors/')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка', upload_to='books_cover/')
    year = models.PositiveSmallIntegerField('Год выпуска')
    genres = models.ForeignKey(Genre, verbose_name='жанры', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, verbose_name='автор', related_name='author', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='книга', related_name='ratings')

    def __str__(self):
        return f"{self.star} - {self.book}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    book = models.ForeignKey(Book, verbose_name='книга', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'