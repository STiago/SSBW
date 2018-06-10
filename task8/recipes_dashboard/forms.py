from django import forms
from .models import Recipe
from mongoengine import *


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
        tags = data['tags'].split(",")
        return data['image']

    #def saved(self, *args, **kwargs):
    	#super(RecipeForm, self).save(*args, **kwargs)

    #def __init__(self, *args, **kwargs):
        #super(RecipeForm, self).__init__(*args, **kwargs)
