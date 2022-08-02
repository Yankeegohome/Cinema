from django import template
from movie.models import Movie

register = template.Library()


@register.inclusion_tag('tags/show_last_movies.html')
def show_movies():
    movies = Movie.objects.all().order_by("-year")[0:5]
    return {"movies": movies}