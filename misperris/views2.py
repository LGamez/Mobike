import sqlite3

from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404 , get_list_or_404
#import pylint

from .forms import Dueño, Estado, FormPerro, Login, Registro ,EstadoP, check
from .models import Adoptante, Perros, Cliente ,Estado

import uuid

def consultar_perro(request):
	if request.POST:
		codigo1=request.POST.get('codigo')
		note=get_object_or_404(Perros,codigo=codigo1)
		data = {
			"codigo" : note.codigo,
			"nombre": note.nombre,
			"raza": note.raza,
			"estado": note.estado,
			"descripcion": note.descripcion,
			"foto": note.foto
		}
		
	return render(request,"modificar.html", data)

def modificar_perro(request):
	if request.POST:
		codigo=request.POST['codigo']
		cliente=get_object_or_404(Perros, codigo=codigo)
		cliente.nombre=request.POST['nombre']
		cliente.raza=request.POST['raza']
		cliente.descripcion =request.POST['descripcion']
		cliente.estado=request.POST['estado']
		cliente.foto=request.FILES['foto']
		cliente.save()
		return HttpResponseRedirect('/mantenedor/')
	return render(request, 'modificar.html',{})

def delete_perro(request):
	if request.POST:
		codigo1=request.POST.get('codigo')
		note=get_object_or_404(Perros,codigo=codigo1).delete()
		return HttpResponseRedirect('/mantenedor/')
	else:
		return HttpResponse('no')
	return HttpResponse('?')

def buscar_usuario(request, id=None):
	form=Login(request.POST or None)

	variables = {
		"form":form,
	}

	if form.is_valid():
		datos = form.cleaned_data
		nombre=datos.get("usuario")	
		contraseña=datos.get("contraseña")

		usuario = get_object_or_404(Cliente, nombre=nombre,contraseña=contraseña)

		if usuario.descripcion =='1':
			messages.success(request,usuario.nombre)
			return redirect('/mantenedor/')
		elif usuario.descripcion =='2':
			messages.success(request,usuario.nombre)
			return redirect('/home/')
		else:
			return HttpResponseRedirect('/login/')
	else:
		messages.error(request,'Ocurrió un error al tratar de enviar formulario.')
		return render(request,"login.html", variables)
	return render(request,"login.html", variables)

def recuperar_usuario(request):
	if request.POST:
		nombre=request.POST['nombre']
		contraseña=request.POST['pass']
		contraseña2=request.POST['pass2']

		usuario = get_object_or_404(Cliente, nombre=nombre)

		if contraseña==contraseña2:
			usuario.contraseña=contraseña
			usuario.save()
		
		mensaje = {
			"mensaje1":'Quedo guardado correctamente',
		}
		return render(request,"recuperar.html", mensaje)
	return render(request,"recuperar.html",{})
		#return HttpResponseRedirect('/login/')
	#return render(request,"recuperar.html", variables)

def agregar_perro(request):
	if request.POST:
		codigo=uuid.uuid1()
		nombre=request.POST.get('nombre')
		raza=request.POST.get('raza')
		descripcion =request.POST.get('descripcion')
		estado=request.POST.get('estado')
		foto=request.FILES['foto']

		db_registrar=Perros(codigo=codigo,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado,foto=foto)
		db_registrar.save()
		return HttpResponseRedirect('/mantenedor/')
	else:
		return HttpResponse('no')
	return HttpResponse('?')

def buscar_perro(request):
	if request.POST:
		estado=request.POST.get('estadobuscar')
		print(estado)
		if estado=='Disponible':
			return HttpResponseRedirect('/diponible/')
		elif estado=='Rescatado':
			return HttpResponseRedirect('/rescatado/')
		elif estado=='Adoptado':	
			return HttpResponseRedirect('/adoptado/')
	else:
		return render(request,"buscador.html",{})
	return render(request, 'buscador.html',{})

class buscar(ListView):
	template_name='perros_list1.html'
	model = Perros

class Disponible(ListView):
	template_name='perros_list1.html'
	
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Disponible')
		except:
			return HttpResponseRedirect('/mantenedor/')

class Rescatado(ListView):
	template_name='perros_list1.html'
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Rescatado')
		except:
			return HttpResponseRedirect('/mantenedor/')

class Adoptado(ListView):
	template_name='perros_list1.html'
	
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Adoptado')
		except:
			return HttpResponseRedirect('/mantenedor/')

def buscar_perro_mantenedor(request):
	if request.POST:
		estado=request.POST.get('estadobuscar')
		print(estado)
		if estado=='Disponible':
			return HttpResponseRedirect('/mantenedor/diponible/')
		elif estado=='Rescatado':
			return HttpResponseRedirect('/mantenedor/rescatado/')
		elif estado=='Adoptado':	
			return HttpResponseRedirect('/mantenedor/adoptado/')
	else:
		return render(request,"mantenedor.html",{})
	return render(request, 'mantenedor.html',{})
	
class Listar(ListView):
	template_name='perros_list.html'
	model = Perros

class DisponibleM(ListView):
	template_name='perros_list.html'
	
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Disponible')			
		except:
			return HttpResponseRedirect('/mantenedor/')

class RescatadoM(ListView):
	template_name='perros_list.html'
	
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Rescatado')
		except:
			return HttpResponseRedirect('/mantenedor/')

class AdoptadoM(ListView):
	template_name='perros_list.html'
	
	def get_queryset(self):
		try:
			return get_list_or_404(Perros, estado='Adoptado')
		except:
			return HttpResponseRedirect('/mantenedor/')