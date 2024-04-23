"""
URL configuration for AxonIngenieria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
#app con las vistas
from productos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="inicio"),
    path('inicio/', views.index, name="inicio"),
    path('productos/', views.productos, name="productos"),
    path('clientes/', views.clientes, name="clientes"),
    path('contacto/', views.contacto, name="contacto"),
    path('empresa/', views.empresa, name="empresa"),
    path('representacion/', views.representacion, name="representacion"),
    path('servicios/', views.servicios, name="servicios"),
    #path('crear-producto/', views.crear_producto, name="crear_producto"),
    path('producto/', views.producto, name="producto"),
    path('editar-producto', views.editar_producto, name="editar_producto"),
    path('borrar-producto/<int:id>', views.borrar_producto, name="borrar"),
    path('guardar-producto/', views.guardar_producto, name="guardar"),
    path('crear/', views.crear, name="crear"),
    
]



# configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
