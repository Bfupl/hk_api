from django.db import models

# Create your models here.

class Hooker(models.Model):
    name = models.CharField(max_length=40)
    price = models.PositiveIntegerField()
    image = models.ImageField()