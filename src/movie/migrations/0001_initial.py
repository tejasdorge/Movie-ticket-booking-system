# Generated by Django 4.0.4 on 2022-06-10 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Born', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('genre', models.CharField(default='', max_length=25, null=True)),
                ('release_date', models.DateField()),
                ('language', models.CharField(max_length=50, null=True)),
                ('trailer', models.URLField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_seats', models.IntegerField(blank=True, null=True)),
                ('seat_code', models.CharField(max_length=30, null=True)),
                ('seat_type', models.CharField(choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=200)),
                ('booked_seats', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('no_of_screens', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, null=True)),
                ('language', models.CharField(max_length=50, null=True)),
                ('screen', models.IntegerField(default=1)),
                ('datetime', models.DateTimeField(null=True)),
                ('total_seats', models.IntegerField(default=200)),
                ('movie_shown', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.movie')),
                ('theater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.theater')),
            ],
        ),
    ]
