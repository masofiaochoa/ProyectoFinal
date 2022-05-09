from django.urls import path
from AppRegistro import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), # no funciona no hay template
    path('acercademi', views.acerca_de_mi, name="acerca_de_mi"),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppRegistro/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
]

# usuario sofi ktN4UqcU
# superuser sofipc asd