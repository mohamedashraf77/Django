from django.db import models


class IdNumber(models.Model):
    number = models.CharField(max_length=150)

    def __str__(self):
        return self.number


class review(models.Model):
    comment = models.TextField(verbose_name="Description movie")
    movie = models.ForeignKey('movie', on_delete=models.CASCADE, null=True)

class cast(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to= 'movies/profile_picture')
    idnumber = models.OneToOneField(IdNumber, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description movie")
    likes = models.IntegerField()
    watch_count = models.IntegerField()
    rate = models.PositiveIntegerField()
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    panner = models.ImageField(upload_to= 'movies/panner')
    actors = models.ManyToManyField(cast)

    def __str__(self):
        return self.name