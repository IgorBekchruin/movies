from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import *
from django.shortcuts import redirect


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'
    template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    slug_field = 'url'
    template_name = 'movies/moviesingle.html'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

    def get():
        pass