from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def get_user_name(self):
        return self.first_name


class Song(models.Model):
    title = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.CharField(max_length=100)
    artist_id = models.CharField(primary_key=True, max_length = 500, unique = True)

    def get_title(self):
        return self.title

    class Meta:
        ordering = ['-artist_id']


class Lyric(models.Model):
    content = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.CharField(primary_key = True, max_length = 5, unique = True)

    def get_lyric(self):
        return self.content