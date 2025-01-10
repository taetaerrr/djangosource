from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title