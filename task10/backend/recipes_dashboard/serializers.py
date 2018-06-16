# mi_app/serializers.py
# adaptado para mongoengine
from rest_framework_mongoengine import serializers
from .models import Recipe

class RecipeSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Recipe
		fields = '__all__'
