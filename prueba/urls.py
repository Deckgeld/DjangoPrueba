"""
URL configuration for prueba project.

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
from inicio import views
from registros import views as registros_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',registros_views.registros, name="Principal"),
    path('formulario/',views.formulario,name="Formulario"),
    
    path('registrar/',registros_views.registrar,name="Registrar"),
    #path('contacto/',registros_views.contacto,name="Contacto"),
    path('comentarios/',registros_views.comentarios,name="Comentarios"),
    path('eliminarComentarioContacto/<int:id>/', registros_views.eliminarComentarioContacto, name="Eliminar"),
    path('consultarComentario/<int:id>/', registros_views.consultarCometarioIndividual, name="Consulta individual"),
    path('EditarComentarioContacto/<int:id>/', registros_views.editarComentarioContacto, name="Editar"),

    path('consultas1', registros_views.consultar1, name="Consultas1"),
    path('consultas2', registros_views.consultar2, name="Consultas2"),
    path('consultas3', registros_views.consultar3, name="Consultas3"),
    path('consultas4', registros_views.consultar4, name="Consultas4"),
    path('consultas5', registros_views.consultar5, name="Consultas5"),
    path('consultas6', registros_views.consultar6, name="Consultas6"),
    path('consultas7', registros_views.consultar7, name="Consultas7"),

    path('subir/',registros_views.archivos,name="Subir"),
    #path('ejemplo/',views.ejemplo,name="ejemplo"),
]

#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que
#almacenan la ubicación de nuestras imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)