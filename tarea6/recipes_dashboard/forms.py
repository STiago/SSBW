from django import forms
from .models import Recipe
from mongoengine import *

#from django.forms import ModelForm
#from mongodbforms import DocumentForm


class RecipeForm(forms.Form):
    name    = forms.CharField(label='Photo name', max_length=60,
                                help_text='60 characters maximun')
    tags = forms.CharField(label="Tags")
    image    = forms.ImageField()

    class Meta:
        model = Recipe
        fields = ('name', 'tags', 'image',)

    def saved(self):
        data = self.cleaned_data
        print("jaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", data, type(data))
        tags = data['tags'].split(",")
        #recipe = RecipeForm()
        #recipe.name=data['name']
        #recipe.tags=tags
        #recipe.image=data['image']
        #recipe = Recipe(name=data['name'], tags=tags, photo_file=data['image'])#data['tags'], photo_file=data['image'])
        #recipe.save()
        return data['image']

    #def saved(self, *args, **kwargs):
    	#super(RecipeForm, self).save(*args, **kwargs)

    #def __init__(self, *args, **kwargs):
        #super(RecipeForm, self).__init__(*args, **kwargs)

    #def saved(self, request, recipe):
        #recipe.tags = self.cleaned_data['tags']
        #recipe.image = self.cleaned_data['image']
        #recipe.name = self.cleaned_data['name']
        #recipe.save()
