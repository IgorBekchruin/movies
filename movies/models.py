from django.urls import reverse
from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория') 
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=200, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')

    def __str__(self):
        return self.name

    

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    tagline = models.CharField(max_length=100, default='', verbose_name='Слоган')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to='media/', verbose_name='Постер')
    year = models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода')
    country = models.CharField(max_length=100, verbose_name='Страна')
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_directors')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor' )
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premier = models.DateField(default=date.today, verbose_name='Мировая премьера')
    budget = models.PositiveIntegerField(default=0, help_text='сумма в долларах', verbose_name='Бюджет')
    fees_in_usa = models.PositiveIntegerField(default=0, help_text='сумма в долларах', verbose_name='Сборы в США')
    fees_in_world = models.PositiveIntegerField(default=0, help_text='сумма в долларах', verbose_name='Сборы в мире')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(default=False, verbose_name='черновик')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})
    

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0, verbose_name='Значение')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'    


class Rating(models.Model):
    ip = models.CharField(max_length=15, verbose_name='IP')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    

class Review(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение")
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'