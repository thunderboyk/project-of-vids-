from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hall(models.Model):
    title = models.CharField(max_length=240)
    user =  models.ForeignKey( User ,on_delete= models.CASCADE)


# class based views are used when we create a halls object update them or just view the detils of them we use 
class Video(models.Model):
    title = models.CharField(max_length=240)
    url = models.URLField()
    youtube_id = models.CharField(max_length=250)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)