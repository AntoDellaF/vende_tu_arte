from django.urls import path
from .views import home, about_us, register, login, art_pieces, create_edit_art_piece

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('art-pieces/', art_pieces, name='art_pieces'),
    path('create-edit-art-piece/', create_edit_art_piece, name='create_edit_art_piece'),
]