from django.db import models
from django.core.exceptions import ValidationError
from user.models import CustomUser
user = CustomUser


class Actor(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    Born = models.CharField(max_length=50)

    def get_info(self):
        return self.name + self.Born

    def __str__(self):
        return self.name


class Theater(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=30, null=True)
    no_of_screens = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50, null=True, default="")
    duration = models.IntegerField(null=True)
    genre = models.CharField(max_length=25, null=True, default="")
    release_date = models.DateField()
    language = models.CharField(max_length=50, null=True)
    cast = models.ManyToManyField(Actor, related_name='related')
    popularity_index = models.IntegerField(unique=True, null=True, blank=True)
    trailer = models.URLField(max_length=100, null=True, blank=False)
    theaters = models.ManyToManyField(
        Theater)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Shows(models.Model):
    show_time = models.TimeField(null=True)
    theater = models.ForeignKey(Theater,related_name='theaters', null=True, on_delete=models.CASCADE)
    movie_shown = models.ForeignKey(
        Movie, related_name='movies', null=True, on_delete=models.SET_NULL)
    language = models.CharField(max_length=50, null=True)
    screen = models.IntegerField(default=1)
    date = models.DateField(null=True)
    total_seats = models.IntegerField(default=200)


class Seat(models.Model):
    seat_choice = (
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )

    no_of_seats = models.IntegerField(null=True, blank=True)
    seat_code = models.CharField(max_length=30, null=True, blank=False)
    seat_type = models.CharField(
        max_length=200, choices=seat_choice, blank=False)
    booked_seats = models.CharField(max_length=30, null=True, blank=True)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    booked_by_customer = models.ForeignKey(
        user, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        self.booked_seats = self.seat_code
        objects = Seat.objects.all()
        seats = []
        for obj in objects:
            number = obj.booked_seats.split(',')
            for i in number:
                seats.append(i)
        for i in self.seat_code:
            if i in seats:
                raise ValidationError(
                    'Already Booked')
        seats_split = self.seat_code.split(',')
        test_list = [int(i) for i in seats_split]
        length = len(seats_split)
        self.no_of_seats = int(length)
        seat_no = max(test_list)
        if int(seat_no) > int(self.show.total_seats):
            raise ValidationError(
                f'seat number {seat_no} does not exist, screen has {self.show.total_seats} seats only')
        super(Seat, self).save(*args, **kwargs)
