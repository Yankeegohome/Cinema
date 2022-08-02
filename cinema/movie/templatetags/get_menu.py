from django import template
from movie.models import Category

register = template.Library()


@register.inclusion_tag('tags/get_menu.html')
def show_menu():
    categories = Category.objects.all()
    return {"categories": categories}
