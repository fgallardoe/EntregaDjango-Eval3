from django.shortcuts import render
from django.http import HttpResponse
from .models import Adoptante, Comuna, Regione,Vivienda
import requests
# Create your views here.


def index(request):
    response = requests.get('http://api.ipstack.com/191.126.136.238?access_key=be0dab072e22a4540c3ccc86c8b1210b')
    data = response.json()
    response2 = requests.get('http://indicadoresdeldia.cl/webservice/indicadores.json')
    data2 = response2.json()
    return render(request, 'index.html', {'nombre': "Felipe", 'ip':data['ip'], 'pais': data['country_name'], 'region': data['region_name'], 'lat': data['latitude'], 'long': data['longitude'], 'dolar': data2['moneda']})


def registro(request):
    return render(request, "formulario.html", {'nombre': "Felipe"})


def crear(request):
    nombre = request.POST.get('nombre','')
    rut = request.POST.get('rut',1)
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    fecha = request.POST.get('fecha', '2000-01-01')
    region = request.POST.get('nom_reg','')
    comuna = request.POST.get('nom_comuna','')
    tipo = request.POST.get('tipo-vivienda','')
    adoptante = Adoptante(nombre_full=nombre, rut=rut, email=email, comuna=comuna,region=region, fec_nac=fecha, fono=telefono, tipo_vivienda= tipo)
    adoptante.save()
    return render(request, "recibido.html")


def listar(request):
    return render(request, 'listar.html', {'elementos':Adoptante.objects.all()})


def buscar(request, id):
    postulante = Adoptante.objects.get(pk=id)
    return HttpResponse('rut:' + str(Adoptante.rut) + '<br> Nombre :' + Adoptante.nombre_full  + '<br> email:' + str(Adoptante.email))


def eliminar(request, id):
    adoptante = Adoptante.objects.get(pk=id)
    adoptante.delete()
    return render(request, 'listar.html', {'elementos': Adoptante.objects.all()})


def editar(request, id):
    adoptante =Adoptante.objects.get(pk=id)
    return render(request, 'editar.html',{'adoptante': adoptante})


def edicion(request, id):
    adoptante = Adoptante.objects.get(pk=id)
    nombre = request.POST.get('nombre','')
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    fecha = request.POST.get('fecha', '')
    region = request.POST.get('nom_reg','')
    comuna = request.POST.get('nom_comuna','')
    tipo = request.POST.get('tipo_vivienda','')
    adoptante = Adoptante(nombre_full=nombre, rut=id, email=email, comuna=comuna,region=region, fec_nac=fecha, fono=telefono, tipo_vivienda= tipo)
    adoptante.save()
    return render(request, 'listar.html', {'elementos': Adoptante.objects.all()})



