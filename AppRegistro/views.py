from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppRegistro.models import Avatar, blogsModel
from AppRegistro.forms import UserRegisterForm, UserEditForm

from django.views import generic

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

# Blog
# class lista_blog(generic.ListView):
#      queryset = blogsModel.objects.order_by('-created_on')
#     template_name = 'inicio.html'

# class detalle_blog(generic.DetailView):
#     model = blogsModel
#     template_name = 'detalle_blog.html'

class blogList(ListView): 
      model = blogsModel 
      template_name = "AppRegistro/blogsModel_list.html"

class blogDetalle(DetailView):
      model = blogsModel
      template_name = "AppRegistro/blogsModel_detalle.html"

class blogCreacion(CreateView):
      model = blogsModel
      success_url = "/AppRegistro/blogs/list"
      fields = ['titulo', 'slug','cuerpo']

class blogUpdate(UpdateView):
      model = blogsModel
      success_url = "/AppRegistro/blogs/list"
      fields  = ['titulo', 'cuerpo']

class blogDelete(DeleteView):
      model = blogsModel
      success_url = "/AppRegistro/blogs/list"

# acerca_de_mi view
def acerca_de_mi(request):
    return render(request, "AppRegistro/acercademi.html")

# @login_required
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppRegistro/inicio.html" ) #, {"url": avatares[0].imagen.url}

# LOGIN
def login_request(request):

      if request.method == "POST":
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
      usuario = request.user
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid: 
                  informacion = miFormulario.cleaned_data

                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppRegistro/inicio.html") 
      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      return render(request, "AppRegistro/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
