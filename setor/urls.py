from django.urls import path
from . import views
urlpatterns = [
 path('', views.home_view, name='home'),
 path('/produtos/', views.listar_produtos_view, name='listar_produtos'),
 # as demais rotas (listar, detalhes, criar, editar, excluir) entram aqui
]