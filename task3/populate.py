# populate.py
from models import Recipe
from mongoengine import *

conect('recipes', host='mongodb', port=27017)

photo_file = open('logo.png', 'rb')

recipe = Recipe(name="albaicin", ingredients=['albaicin', 'granada'], likes_up=2, photo_file=photo_file)
recipe.save()

#...

for f in Recipes.objects():  # todos los registros
	print(f.name, ' ', f.ingredients, f.likes_up, ' ')
	#archi = f.photo_file
	#if (archi):
		#im = archi.read()
		#g = open('desde_bd_'+f.name+'.jpg', wb)
		#g.write(im)
		#g.close()
