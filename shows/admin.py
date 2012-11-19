from django.contrib import admin
from .models import Show, Episode, Actor, Director, Genre, Network

class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'actor_slug_name': ['actor_name']}

class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'director_slug_name': ['director_name']}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'genre_slug_type': ['genre_type']}

class NetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'network_slug_name': ['network_name']}

class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'show_slug_name': ['show_name']}

class EpisodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'episode_slug_name': ['episode_name']}

admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodAdmin)
