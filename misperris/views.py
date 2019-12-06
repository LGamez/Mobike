from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .serializers import MascotaSerializer
from .forms import Registro
from .forms import Dueño
from .forms import Estado
from .forms import Login
from .forms import FormPerro
from .models import Adoptante
from .models import Usuario
from .models import Mascota
from rest_framework import viewsets
import sqlite3


def contacto(request):
    form_contacto = Dueño(request.POST or None)

    variables = {
        "form": form_contacto,
    }

    if form_contacto.is_bound and form_contacto.is_valid():
        datos = form_contacto.cleaned_data
        email = datos.get("email")
        run = datos.get("run")
        nombre = datos.get("nombre")
        apellido = datos.get("apellido")
        fecha = datos.get("fecha")
        telefono = datos.get("telefono")
        region = datos.get("region")
        ciudad = datos.get("ciudad")
        tipo = datos.get("tipo")

        db_registrar = Adoptante(email=email, run=run, nombre=nombre, apellido=apellido, fechanacimiento=fecha, telefono=telefono,
                                 region=region, ciudad=ciudad, tipo=tipo)
        db_registrar.save()

        foto = {
            "foto": ""
        }

        messages.success(
            request, 'Tu formulario ha sido enviado correctamente.')
        #messages.error(request,'Ocurrió un error al tratar de enviar formulario.')
        return render(request, "index.html", foto)
        # return HttpResponse(
        #	'Formulario quedo guardado correctamente.'
        #	'<a class="contact100-form-btn" type="submit" href="/home/" >Volver atrás</a>')
    # else:
    #	messages.error(request,'Ocurrió un error al tratar de enviar formulario.')
        # return HttpResponse('<button class="contact100-form-btn" type="submit">Guardar</button>')
    #	return render(request,"index.html", variables)
    return render(request, "index.html", variables)


def home(request):
    return render(request, 'MisPerris.html', {})


def buscar(request):
    form_estado = Estado(request.POST or None)

    variables = {
        "form": form_estado,
    }

    if form_estado.is_valid():
        datos = form_estado.cleaned_data
        estado = datos.get("estado")

        print(estado)
        # db_registrar=Adoptante(email=email,run=run,nombre=nombre,apellido=apellido,fechanacimiento=fecha,telefono=telefono,
        # region=region,ciudad=ciudad,tipo=tipo)
        # db_registrar.save()
    return render(request, "buscador.html", variables)


def mantenedor(request):
    return render(request, 'mantenedor.html', {})


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
