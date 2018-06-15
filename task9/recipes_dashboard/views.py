from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext
from populate import *
from . import models
from .forms import RecipeForm
from .models import Recipe
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.decorators import login_required
import logging
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import RecipeSerializer


# Task 8 - Get an instance of a logger
logger = logging.getLogger(__name__)

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

def contenido_texto_plano(request):
    return HttpResponse("Esto es el contenido de texto plano.")

def contenido_html(request):
    return render(request, '../templates/index.html')

def contenido_imagen(request):
    #return render(request, '../templates/otro.html') #return a picture inside html
    valid_image = "static/images/image.png"
    with open(valid_image, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")

def cualquier_contenido(request,text):
    return HttpResponse("Tenemos este texto plano introducido en la url:  %s" % text)


def home(request):
    photo_list = Recipe.objects().order_by('-posted')
    context = {
        'photo_list': photo_list,
        'number_of_results': len(photo_list),
    }
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Home page.")
    return render(request, "../templates/home.html", context)


def get_recipe_image(request, id):
    obj = Recipe.objects.get(id=id)
    image = obj.photo_file.read()
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Get recipe.")
    return HttpResponse(image, content_type="image/jpg")

def search_by_tag(request):
    photo_list = []
    number_of_results = 0
    if request.method == "POST" :
        tag = request.POST.get('search')
        photo_list = Recipe.objects(tags=tag).order_by('-posted')
    context = {
        'search_tag': tag,
        'photo_list': photo_list,
        'number_of_results': len(photo_list),
    }
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') +" - search by tag.")
    return render(request, "../templates/images_list.html", context)

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

def save_recipe():
    print("Saved.")


# Task 6 - CRUD
def show_recipe(request, id):
    obj = Recipe.objects.get(id=id)
    if request.method == "GET":
        context = {
            'id': id,
            'name': obj.name,
            'tags': obj.tags,
            'posted': obj.posted,
            'likes_up': obj.likes_up,
            'likes_down': obj.likes_down,
        }
        logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') +" - Show recipe.")
        return render(request, '../templates/show_recipe.html', {'detail': context})

@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form_tags=request.POST['tags']
            model_tags = form_tags.split(',')
            instance = Recipe(photo_file=request.FILES['image'], name=request.POST['name'], tags=model_tags)
            instance.save()
            logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - New recipe added.")
            return redirect('/recipes_dashboard')
        else:
            logger.error(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ' - Something went wrong and we could not add a new recipe.')
    else:
        form = RecipeForm()
    context = {
		'form': form,
        }
    return render(request, '../templates/add_recipe.html', context)

@login_required
def update_recipe(request, id):
    last_form = get_object_or_404(Recipe.objects.only('id', 'name', 'tags', 'photo_file'), id=id)
    if request.method == "POST":
        n_form = RecipeForm(request.POST, request.FILES, last_form)
        if n_form.is_valid():
            post = n_form.saved()
            name = request.POST.get('name')
            tags = request.POST.get('tags')
            image = n_form.saved()
            last_form.name = name
            last_form.tags = tags.split(",")
            last_form.photo_file = image
            last_form.save()
            logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Recipe updated.")
            return redirect('/recipes_dashboard')
        else:
            logger.error(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ' - Something went wrong and we could not update it.')
    return render(request, '../templates/update_recipe.html', {'form': last_form})

@login_required
def delete_recipe(request,id):
    instance = Recipe.objects.get(id=id)
    instance.delete()
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Recipe deleted.")
    return redirect('/recipes_dashboard')


## Task 7 - Likes up and down
@csrf_exempt
def like_up(request, id):
    cat_id = id
    likes = 0
    if cat_id:
        recipe = Recipe.objects.get(id=cat_id)
        if recipe:
            likes = recipe.likes_up
            if likes == None:
                likes = 0
            likes = likes + 1
            recipe.likes_up =  likes
            recipe.save()
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Like up.")
    return HttpResponse(likes)

@csrf_exempt
def like_down(request, id):
    cat_id = id
    likes = 0
    if cat_id:
        recipe = Recipe.objects.get(id=cat_id)
        if recipe:
            likes = recipe.likes_down
            if likes == None:
                likes = 0
            likes = likes + 1
            recipe.likes_down =  likes
            recipe.save()
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Like down.")
    return HttpResponse(likes)


# Task 8
@csrf_exempt
def signin(request):
    user_name = ''
    photo_list = Recipe.objects().order_by('-posted')
    try:
        if request.method == "POST" :
            user_name = request.POST.get('userlogin')
            user_psw = request.POST.get('userpsw')
            u = User.objects.get(username=user_name)
            #p = User.objects.get(password=user_psw)
            context = {
                'photo_list': photo_list,
                'number_of_results': len(photo_list),
                'name': user_name,
            }
        logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Sign in: " + user_name)
        return render(request, "../templates/home.html", context)
    except:
        logger.error(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ' - Username or password is not valid .')
        return render(request, '../templates/login.html')


@csrf_exempt
def signup(request):
    try:
        if request.method == "POST" :
            user_name = request.POST.get('username')
            user_psw = request.POST.get('userpsw')
            user_email = request.POST.get('email')
            user = User.objects.create_user(user_name, user_email, user_psw)
            user.first_name = user_name
            user.save()
        logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - Sign up: " + user_name)
        return render(request, '../templates/login.html')
    except:
        logger.error(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ' - Username or password is not valid .')
        return render(request, '../templates/register.html')

# Task 9
def recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializers.errors, stauts=400)


def recipe(request, id):
	try:
		recipe = Recipe.objects.get(id=id)
	except:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)  # No encontrado

	if request.method == 'GET':
		serializer = RecipeSerializer(recipe)
		return JsonResponse(serializer.data)
	elif request.method =='PUT':
		data = JSONParser().parse(request)
		serializer = RecipeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		recipe.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
