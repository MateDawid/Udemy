from django.db import models

class Film(models.Model):
    tytul = models.CharField(max_length=64)
