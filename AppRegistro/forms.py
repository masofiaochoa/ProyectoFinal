from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppRegistro.models import Avatar

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    url = forms.URLField(label='Tu página web', required=False, initial='http://')
    descripcion = forms.CharField(label="Descripción",max_length=300, help_text='Máximo de 300 caracteres.')
    
    #extendemos el contenido de el formulario viejo agregando dos campos más
    # last_name: forms.CharField()
    # first_name: forms.CharField()

    class Meta:
        model = User                                           #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'Nombre de usuario', 'email':'Correo Electrónico','last_name': 'Apellido', 'first_name':'Nombre'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)
    url = forms.URLField(label='Tu página web', required=False, initial='http://')
    descripcion = forms.CharField(label="Descripción",max_length=300, help_text='Máximo de 300 caracteres.')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields} 

