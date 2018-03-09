from django.db import models

# Create your models here. description = models.CharField(max_length=200)
class Recipe(models.Model):
 	name    = models.CharField(max_length=40)
 	ingredients = models.CharField(max_length=200)
 	description = models.CharField(max_length=500)
