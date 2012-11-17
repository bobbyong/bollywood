from django.contrib import admin
from .models import Show, Episode, Actor, Director, Genre, Network

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Network)
admin.site.register(Show)
admin.site.register(Episode)
