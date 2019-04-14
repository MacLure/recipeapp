from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpeg', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
