from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField("Категория", max_length=255)
    descripsion = models.TextField("Описание", blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Actor(models.Model):
    name = models.CharField("Имя актера", max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    bio = models.TextField('Биография актера')
    photo = models.ImageField('Изображение', upload_to="actros/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    name = models.CharField('Жанры', max_length=150)
    descripsion = models.TextField("Описание",)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    title = models.CharField("Название фильмa", max_length=255)
    slogan = models.CharField("Слоган", max_length=100, default='')
    descripsion = models.TextField("Описание")
    poster = models.ImageField("Изображение", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField('Страна', max_length=50)
    director = models.ManyToManyField(Actor, verbose_name="Режиссер", related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="film_actor")
    genre = models.ManyToManyField(Genre, verbose_name="Жанры")
    primer = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveSmallIntegerField("Бюджет", default=0, help_text="Указать сумму в долларах")
    money_in_usa = models.PositiveSmallIntegerField("Сборы в США", default=0, help_text="Указать сумму в долларах")
    money_in_world = models.PositiveSmallIntegerField("Сборы в Мире", default=0, help_text="Указать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    is_published = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    title = models.CharField(max_length=150)
    descripsion = models.TextField(blank=True)
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры и фильма"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("Ip адрес", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="Звезда", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=3000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"