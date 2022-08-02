from django import template
from movie.models import Genre

register = template.Library()


@register.inclusion_tag('tags/get_genries.html')
def show_genries():
    movies = Genre.objects.all()
    return {"genre": movies}
