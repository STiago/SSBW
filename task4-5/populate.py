# populate.py
#To run this file use: docker-compose exec web python populate.py
from recipes_dashboard.models import Recipe
from mongoengine import *

connect('recipes', host='mongodb', port=27017)
PATH_TO_IMAGES = 'static/images/'

"""photo_file = open('static/images/starters/ensalada.jpg', 'rb')

recipe = Recipe(name="ensalada", tags=['ensalada', 'starters', 'granada'], likes_up=4, photo_file=photo_file)
recipe.save()

for f in Recipe.objects():  # todos los registros
	print(f.name, ' ', f.tags, f.likes_up, ' ')
	archi = f.photo_file
	if (archi):
		im = archi.read()
		g = open('db/'+'desde_bd_'+f.name+'.jpg', 'wb')
		g.write(im)
		g.close()"""

def add_register(filename, tagslist,l_up, l_down, photo_file):
	photo_file = open(PATH_TO_IMAGES+photo_file, 'rb')
	recipe = Recipe(name=filename, tags=tagslist, likes_up=l_up, likes_down=l_up, photo_file=photo_file)
	recipe.save()

def search_by_tag(tag):
	results = Recipe.objects(tags=tag).order_by('-posted')
	for i in results:
		print(i.name, i.tags, i.likes_up)
	return results# photo_dic

def main():
	print(search_by_tag(['granada']))
	add_register('Atún en escabeche', ['mediterraneo', 'granada'], 15, 3, 'atun.jpg')

if __name__ == "__main__":
    main()
