from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'footage', 'genres_display', 'director']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'director__name']
    list_filter = ['genre', 'year']

class DirectorAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

class ActorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)