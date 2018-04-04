from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from populate import *
from . import models
from .forms import RecipeForm
from .models import Recipe


def contenido_texto_plano(request):
    return HttpResponse("Esto es el contenido de texto plano.")

def contenido_html(request):
    return render(request, '../templates/index.html')

def contenido_imagen(request):
    #return render(request, '../templates/otro.html') #tambien se puede retornar una imagen en un html
    valid_image = "static/images/image.png"
    with open(valid_image, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")

def cualquier_contenido(request,text):
    return HttpResponse("Tenemos este texto plano introducido en la url:  %s" % text)

####
def home(request):
    photo_list = Recipe.objects().order_by('-posted')
    context = {
        'photo_list': photo_list,
        'number_of_results': len(photo_list),
    }
    return render(request, "../templates/home.html", context)

def signin(request):
    return render(request, '../templates/login.html')

def signup(request):
    return render(request, '../templates/register.html')


def get_recipe_image(request, id):
    obj = Recipe.objects.get(id=id)
    image = obj.photo_file.read()
    return HttpResponse(image, content_type="image/jpg")

def search_by_tag(request):
    photo_list = []
    number_of_results = 0
    #tag = ''
    if request.method == "POST" :
        tag = request.POST.get('search')
        photo_list = Recipe.objects(tags=tag).order_by('-posted')
    print(tag,photo_list)
    context = {
        'search_tag': tag,
        'photo_list': photo_list,
        'number_of_results': len(photo_list),
    }
    return render(request, "../templates/images_list.html", context)

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def add_recipe(request):
    form = RecipeForm()
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            print("after form")
            #instance = form.cleaned_data
            form_tags=request.POST['tags']
            model_tags = form_tags.split(',')
            instance = Recipe(photo_file=request.FILES['image'], name=request.POST['name'], tags=model_tags)
            print(instance)
            instance.save()
            #return HttpResponseRedirect('../templates/add_recipe.html')
            #return redirect('../templates/add_recipe.html')
    else:
        form = RecipeForm()
        # GET o error
    context = {
		'form': form,
        }
    return render(request, '../templates/add_recipe.html', context)