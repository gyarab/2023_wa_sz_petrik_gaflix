# Generated by Django 5.0.3 on 2024-05-31 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_movie_actor_movie_director_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='director',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
