from django.db import models
import random

# Create your models here.

class Product(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField()
    price       = models.DecimalField(max_digits=9, decimal_places=2)
    clicks      = models.IntegerField(default=random.randint(1,30))
    image       = models.ImageField()
    link        = models.CharField(max_length=800)
    datetime    = models.DateTimeField()
    man_tag     = models.BooleanField(default=True)
    woman_tag   = models.BooleanField(default=True)
    geek_tag    = models.BooleanField(default=True)
    kid_tag     = models.BooleanField(default=True)
    pet_tag     = models.BooleanField(default=True)

    def __str__(self):
        return self.name


