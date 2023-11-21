from django.shortcuts import render
from .models import ArtPiece 

def home(request):
    return render(request, 'art_gallery/home.html')

def sobre_nosotros(request):
    return render(request, 'art_gallery/sobre_nosotros.html')

def registro(request):
    # Implementar la lógica de registro de usuarios
    return render(request, 'art_gallery/registro.html')

def login(request):
    # Implementar la lógica de inicio de sesión
    return render(request, 'art_gallery/login.html')

def art_pieces(request):
    art_pieces = ArtPiece.objects.all()
    return render(request, 'art_gallery/art_pieces.html', {'art_pieces': art_pieces})

def rear_editar_pieza(request):
    # Implementar la lógica de creación o edición de obras de arte
    return render(request, 'art_gallery/crear_editar_pieza.html')

