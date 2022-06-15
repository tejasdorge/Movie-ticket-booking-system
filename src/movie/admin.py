from django.contrib import admin
from .models import Actor, Shows, Movie, Theater, Seat

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Theater)
admin.site.register(Shows)
admin.site.register(Seat)
