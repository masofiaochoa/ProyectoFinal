from django.urls import path
from AppRegistro import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    # path('', views.blogList.as_view(), name=""),
    # path('', views.lista_blog.as_view(), name="home"),
    # path('<slug:slug>/', views.detalle_blog.as_view(), name='detalleBlog'),
    path('acercademi', views.acerca_de_mi, name="acerca_de_mi"),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppRegistro/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),

    path('blogs/list', views.blogList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.blogDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.blogCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.blogUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.blogDelete.as_view(), name='Delete'),
]

# usuario nuevo ktN4UqcU
# superuser sofipc asd
# https://djangocentral.com/building-a-blog-application-with-django/