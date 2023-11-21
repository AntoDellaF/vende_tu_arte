from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import ArtPiece

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Ingrese su nombre de usuario')
    first_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su nombre')
    last_name = forms.CharField(max_length=30, required=True, help_text='Ingrese su apellido')
    phone = forms.CharField(max_length=15, required=True, help_text='Ingrese su número de teléfono')
    email = forms.EmailField(max_length=254, help_text='Ingrese su dirección de correo electrónico')
    address = forms.CharField(max_length=255, required=True, help_text='Ingrese su dirección')
    city = forms.CharField(max_length=100, required=True, help_text='Ingrese su ciudad')
    postal_code = forms.CharField(max_length=10, required=True, help_text='Ingrese su código postal')

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        min_length=6,
        help_text='La contraseña debe tener al menos 6 caracteres, una mayúscula y una minúscula.'
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        min_length=6
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'phone', 'email', 'address', 'city', 'postal_code')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    

class CustomAuthenticationForm(AuthenticationForm):
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres, una mayúscula, una minúscula y un dígito.')

        return password
    

class ArtPieceForm(forms.ModelForm):
    class Meta:
        model = ArtPiece
        fields = ['title', 'subtitle', 'description', 'author', 'image']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'description': 'Descripción',
            'author': 'Autor',
            'image': 'Imagen',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }