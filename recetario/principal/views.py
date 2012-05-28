# Create your views here.
from principal.models import Bebida, Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def sobre(request):
	html = "<html><body>Proyecto</body></html>"
	return HttpResponse(html)
def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':bebidas}, context_instance = RequestContext(request))
def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas}, context_instance = RequestContext(request))
def usuarios(request):
	usuarios = User.objects.all()
	recetas = Receta.objects.all()
	return render_to_response('usuarios.html',{'usuarios':usuarios, 'recetas':recetas})
def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('recetas.html', {'datos':recetas}, context_instance = RequestContext(request))
def detalle_receta(request, id_receta):
	dato = get_object_or_404(Receta, pk = id_receta)
	comentarios = Comentario.objects.filter(receta = dato)
	return render_to_response('receta.html', {'receta':dato, 'comentarios':comentarios}, context_instance = RequestContext(request))
