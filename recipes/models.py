from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField(blank=True, null-True)
    instructions = models.TextField(blank=True, null-True)
