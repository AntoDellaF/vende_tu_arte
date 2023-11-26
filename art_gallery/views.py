from django.shortcuts import render, redirect,  get_object_or_404
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
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'art_gallery/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            return redirect('art_pieces')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'art_gallery/login.html', {'form': form})

def art_pieces(request):
    obras = ArtPiece.objects.all()
    return render(request, 'art_pieces.html', {'obras': obras})

def detalle_obra(request, obra_id):
    obra = get_object_or_404(ArtPiece, id=obra_id)
    return render(request, 'detalle_obra.html', {'obra': obra})

def crear_editar_pieza(request):
    if request.method == 'POST':
        form = ArtPieceForm(request.POST, request.FILES)
        if form.is_valid():
            art_piece = form.save()
           
            return redirect('art_pieces')
    else:
        form = ArtPieceForm()

    return render(request, 'art_gallery/crear_editar_pieza.html', {'form': form})

def comprar_obra(request, obra_id):
   #formulario y redirigir al pago?
    return redirect('detalle_obra', obra_id=obra_id)

