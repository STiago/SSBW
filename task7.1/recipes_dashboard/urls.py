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
  path('get_recipe_image/<id>',views.get_recipe_image,name='get_recipe_image'),
  url(r'^show_recipe/(?P<id>[0-9a-f]+)/$',views.show_recipe,name='show_recipe'),
  path('add_recipe',views.add_recipe,name='add_recipe'),
  path('update_recipe',views.update_recipe,name='update_recipe'),
  url(r'^update_recipe/(?P<id>[0-9a-f]+)/$',views.update_recipe,name='update_recipe'),
  url(r'^delete_recipe/(?P<id>[0-9a-f]+)/$',views.delete_recipe,name='delete_recipe'),
  url(r'^like_category/$', views.like_category, name='like_category'),
  path('like_category', views.like_category, name='like_category'),
  path('save_recipe', views.save_recipe, name='save_recipe'),
  #path('update_recipe/(?P<id>[0-9a-f]+)/$',views.update_recipe,name='update_recipe')
]
