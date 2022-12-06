from django.db import models


# Create your models here.

class car(models.Model):
    c_name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
