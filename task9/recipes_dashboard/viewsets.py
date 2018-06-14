from rest_framework_mongoengine import viewsets
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
		queryset =  Recipe.objects.all()
		lookup_field = 'id'
		serializer_class = RecipeSerializer
