from django.db import models


class Accounts(models.Model):
    name = models.CharField(max-length=120)
    email = models.CharField(max-length=120)
    password = models.CharField(max-length=120)
