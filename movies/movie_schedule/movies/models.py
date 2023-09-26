from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    genre = models.CharField(max_length=255)
    rating = models.FloatField()
    year_release = models.PositiveIntegerField()
    metacritic_rating = models.FloatField()
    runtime = models.PositiveIntegerField()

    def __str__(self):
        return self.title