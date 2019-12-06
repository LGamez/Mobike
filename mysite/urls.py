from django.contrib import admin
from django.urls import path, include
from misperris import views
from misperris import views2
from misperris.views2 import Listar
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from misperris.views import MascotaViewSet

app_name = 'misperris'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/contacto/', views.contacto),
    path('home/', views.home),
    path('api/', include(routers.urls)),
    path('login/', views2.buscar_usuario),
    path('recuperar/', views2.recuperar_usuario),

    path('home/buscador/', views2.buscar.as_view()),
    path('buscar/', views2.buscar_perro),
    path('diponible/', views2.Disponible.as_view()),
    path('rescatado/', views2.Rescatado.as_view()),
    path('adoptado/', views2.Adoptado.as_view()),

    path('mantenedor/', Listar.as_view()),
    path('mantenedor/buscar/', views2.buscar_perro_mantenedor),
    path('mantenedor/diponible/', views2.DisponibleM.as_view()),
    path('mantenedor/rescatado/', views2.RescatadoM.as_view()),
    path('mantenedor/adoptado/', views2.AdoptadoM.as_view()),

    path('eliminar/', views2.delete_perro),
    path('consultar/', views2.consultar_perro),
    path('modificar/', views2.modificar_perro),
    path('agregar/', views2.agregar_perro),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
