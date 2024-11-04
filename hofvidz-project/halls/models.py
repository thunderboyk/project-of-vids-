from django.db import models

# Create your models here.
class Hall(models.Model):
    title = models.CharField(max_length=240)


# class based views are used when we create a halls object update them or just view the detils of them we use 
class Video(models.Model):
    title = models.CharField(max_length=240)
    url = models.URLField()
    youtube_id = models.CharField(max_length=250)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)