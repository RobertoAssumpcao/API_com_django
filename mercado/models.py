from statistics import quantiles
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 30)
    quantidade = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name