from django.contrib import admin
from .models import Show, Episode, Actor, Director, Genre, Network, Movie, Production_House, MTV

class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'actor_slug_name': ['actor_name']}

class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'director_slug_name': ['director_name']}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'genre_slug_type': ['genre_type']}

class NetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'network_slug_name': ['network_name']}

class Production_HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'production_house_slug_name': ['production_house_name']}

class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'show_slug_name': ['show_name']}

class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'episode_slug_name': ['episode_name']}

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'movie_slug_name': ['movie_name']}

class MTVAdmin(admin.ModelAdmin):
    prepopulated_fields = {'mtv_slug_name': ['mtv_name']}


admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Production_House, Production_HouseAdmin)
admin.site.register(MTV, MTVAdmin)