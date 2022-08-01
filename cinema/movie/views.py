from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F
from .models import *

def get_single(request):
    movie = Movie.objects.all()
    context = {
        "movie": movie,
        "title": 'Название фильма'
    }
    return render(request, template_name='single.html', context=context)


class Home(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фильмы'
        return context


class MovieByCategory(ListView):
    template_name = 'index.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_queryset(self):
        return Movie.objects.filter(category__slug=self.kwargs['url'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['url'])
        return context