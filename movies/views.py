from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'
    template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/moviesingle.html'