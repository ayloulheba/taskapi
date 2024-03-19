from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
