from django.conf.urls import url
from django.urls import path
from . import views

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
  path('get_recipe_image/<id>',views.get_recipe_image,name='get_recipe_image')
]
