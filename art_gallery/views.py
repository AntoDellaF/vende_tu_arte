from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import ArtPiece 
from django.contrib.auth import login 
from .forms import CustomAuthenticationForm
from .forms import ArtPieceForm

def home(request):
    return render(request, 'art_gallery/home.html')

def sobre_nosotros(request):
    return render(request, 'art_gallery/sobre_nosotros.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a la página de inicio de sesión u otra página después del registro
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'art_gallery/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirigir a la página de inicio o a la que desees después del inicio de sesión
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'art_gallery/login.html', {'form': form})

def art_pieces(request):
    art_pieces = ArtPiece.objects.all()
    return render(request, 'art_gallery/art_pieces.html', {'art_pieces': art_pieces})

def crear_editar_pieza(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            art_piece = form.save()
            # Puedes agregar lógica adicional o redirigir a otra página después de guardar la obra de arte
            return redirect('art_pieces')
    else:
        form = ArtPieceForm()

    return render(request, 'art_gallery/crear_editar_pieza.html', {'form': form})

