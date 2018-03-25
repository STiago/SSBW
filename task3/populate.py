# populate.py
from recipes_dashboard.models import Recipe
from mongoengine import *

connect('recipes', host='mongodb', port=27017)

photo_file = open('static/images/starters/ensalada.jpg', 'rb')

recipe = Recipe(name="ensalada", tags=['ensalada', 'starters', 'granada'], likes_up=4, photo_file=photo_file)
recipe.save()


for f in Recipe.objects():  # todos los registros
	print(f.name, ' ', f.tags, f.likes_up, ' ')
	archi = f.photo_file
	if (archi):
		im = archi.read()
		g = open('db/'+'desde_bd_'+f.name+'.jpg', 'wb')
		g.write(im)
		g.close()
