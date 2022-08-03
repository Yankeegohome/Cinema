from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.views.generic.base import View

from .models import *
from .forms import ReviewForm

# def get_single(request):
#     movie = Movie.objects.all()
#     context = {
#         "movie": movie,
#         "title": 'Название фильма'
#     }
#     return render(request, template_name='single.html', context=context)


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
        return Movie.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class MovieByGenre(ListView):
    template_name = 'index.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_queryset(self):
        return Movie.objects.filter(genre__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Фильмы по жанрам" + str(Genre.objects.get(slug=self.kwargs['slug']))
        return context


class GetMovie(DetailView):
    model = Movie
    template_name = 'single.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()

        return redirect(movie.get_absolute_url())