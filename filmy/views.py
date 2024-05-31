from django.shortcuts import render
from .models import Movie, Genre, Actor, Director

def movies(request):
    context = {"movies" : Movie.objects.all().order_by('name')}
    return render(request,'filmy/movies.html', context )