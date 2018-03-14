from django.db import models
from mongoengine import *
import datetime

# Create your models here.
# This is mysql db model
"""class Recipe(models.Model):
 	name    = models.CharField(max_length=40)
 	ingredients = models.CharField(max_length=200)
 	description = models.CharField(max_length=500)
 	posted = models.CharField(max_length=200)
 	likes_up = models.CharField(max_length=500)
 	likes_down = models.CharField(max_length=200)
 	photo = models.CharField(max_length=500)"""

# BD fotos, en servicio mongodb
#connect('mongodb', host='localhost', port=27017)
mongoengine.connect('mongodb',host='localhost:27017')
class Recipe(Document):
	name = StringField(required=True, max_lenght=60)
	posted = DateTimeField(default=datetime.datetime.now)
	ingredients = ListField(StringField())
	likes_up = IntField(min_value=0)
	likes_down = IntField(min_value=0)
	photo_file = ImageField()
