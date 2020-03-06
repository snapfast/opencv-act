from django.db import models


# image experiment
class Image(models.Model):
    """docstring for Image"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    imageref = models.FileField(upload_to="images/")

    def __str__(self):
        return self.title


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
