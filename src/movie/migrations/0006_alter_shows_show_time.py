# Generated by Django 4.0.4 on 2022-06-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_remove_shows_datetime_shows_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='show_time',
            field=models.TimeField(null=True),
        ),
    ]