from django.urls import path
from .views import home, sobre_nosotros, registro, login, art_pieces, crear_editar_pieza

urlpatterns = [
    path('', home, name='home'),
    path('sobre_nosotros/', sobre_nosotros, name='sobre_nosotros'),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('art_pieces/', art_pieces, name='art_pieces'),
    path('crear_editar_pieza/', crear_editar_pieza, name='crear_editar_pieza'),
]