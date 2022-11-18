from django.db import models

class Episode(models.Model):
    title = models.CharField(max_length = 200)
    pub_date= models.DateTimeField()
    link = models.URLField()
    image = models.URLField('href')
    episode_name = models.CharField(max_length = 200)
    guid = models.CharField(max_length =100)

    def __str__(self) ->str:
        return f"{self.episode_name}: {self.title} "

class Content(models.Model):
    title = models.CharField(max_length = 200)
    pub_date= models.DateTimeField()
    link = models.URLField()
    image = models.URLField('href')
    content_name = models.CharField(max_length = 200)
    guid = models.CharField(max_length =100)

    def __str__(self) ->str:
        return f"{self.content_name}: {self.title} "

# Create your models here.
