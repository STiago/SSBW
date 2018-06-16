from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin

# APIS desde clases viewsets
from rest_framework import routers
from .viewsets import RecipeViewSet

router = routers.DefaultRouter()
router.register('recipe', RecipeViewSet, 'recipe')

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url('contenido_html/$', views.contenido_html, name='contenido_html'),
  #url(r'^test/$', views.test, name='test'),
  url('un_texto_plano/$', views.contenido_texto_plano, name='contenido_texto_plano'),
  url('una_imagen/$', views.contenido_imagen, name='contenido_imagen'),
  path('este_texto_plano/<text>', views.cualquier_contenido, name='cualquier_contenido'),
  url('signin', views.signin, name="signin"),
  url('signup', views.signup, name="signup"),
  path('search_by_tag',views.search_by_tag,name='search_by_tag'),
  path('get_recipe_image/<id>',views.get_recipe_image,name='get_recipe_image'),
  url(r'^show_recipe/(?P<id>[0-9a-f]+)/$',views.show_recipe,name='show_recipe'),
  path('add_recipe',views.add_recipe,name='add_recipe'),
  path('update_recipe',views.update_recipe,name='update_recipe'),
  url(r'^update_recipe/(?P<id>[0-9a-f]+)/$',views.update_recipe,name='update_recipe'),
  url(r'^delete_recipe/(?P<id>[0-9a-f]+)/$',views.delete_recipe,name='delete_recipe'),
  url(r'^like_up/(?P<id>[0-9a-f]+)/$', views.like_up, name='like_up'),
  url(r'^like_down/(?P<id>[0-9a-f]+)/$', views.like_down, name='like_down'),
  path('save_recipe', views.save_recipe, name='save_recipe'),
  path('accounts/', include('allauth.urls')),
  path('', views.Home.as_view(), name='home'),
  path('recipes/', views.recipes),    # GET lista todos, POST añade
  path('recipe/<id>/', views.recipe), # GET lista, PUT modifica, DELETE borra
  url('api/', include(router.urls)),
]
