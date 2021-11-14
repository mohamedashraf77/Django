from django.db import models


class cast(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()

class movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description movie")
    likes = models.IntegerField()
    watch_count = models.IntegerField()
    rate = models.PositiveIntegerField()
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
