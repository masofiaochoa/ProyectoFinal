from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppRegistro.models import Avatar
from AppRegistro.forms import UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def acerca_de_mi(request):
    return render(request, "AppRegistro/acercademi.html")

# @login_required
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppRegistro/inicio.html" ) #, {"url": avatares[0].imagen.url}
#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return render (request, "AppRegistro/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        print(2)
                        return render (request, "AppRegistro/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppRegistro/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
      print(3)
      return render(request, "AppRegistro/login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppRegistro/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppRegistro/registro.html", {"form": form})



@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid: #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppRegistro/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppRegistro/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
