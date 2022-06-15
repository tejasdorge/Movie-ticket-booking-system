from rest_framework import serializers
from .models import Movie, Actor, Seat, Shows, Theater


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'genre',
                  'language', 'cast', 'theaters','popularity_index']
        extra_kwargs = {
            "popularity_index":{
                "write_only":True,
            }
        }


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['name', 'Born']


class ShowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shows
        fields =  ['id','show_time', 'language', 'screen',
                  'date', 'total_seats','movie_shown','theater']


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'
        extra_kwargs = {
            "booked_by_customer": {
                "read_only": True,
            },
            "booked_seats":{
            "read_only": True,
            }
        }


class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        fields = '__all__'