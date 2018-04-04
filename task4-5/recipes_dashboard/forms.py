from django import forms

class RecipeForm(forms.Form):
	name    = forms.CharField(label='Photo name', max_length=60,
	                            help_text='60 characters maximun')
	tags = forms.CharField(label="Tags")
	image    = forms.ImageField()
