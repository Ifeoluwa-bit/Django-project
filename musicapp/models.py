from django.db import models
import uuid

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price =  models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    # artiste_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    def __str__(self):
        return self.title
    
    
class Lyric(models.Model):
   song = models.ForeignKey(Song, on_delete=models.CASCADE)
   content = models.TextField(max_length=5000)
#    song_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
   
   def __str__(self):
        return self.song_id