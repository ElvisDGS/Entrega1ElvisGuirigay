from django.shortcuts import render
from django.http import HttpResponse

from AppFinal.models import BoletosReservas
from AppFinal.models import Contactanos
from AppFinal.models import Trabaja

from django.core import serializers

from AppFinal.forms import ReservaFormulario
from AppFinal.forms import ContactoFormulario
from AppFinal.forms import TrabajaFormulario



def buscar(request):
    reserva = request.GET['reserva']
    reservas_todos = BoletosReservas.objects.filter(Nombre = reserva)
    return render(request,'AppFinal/resultadoReserva.html', {'reserva':reserva, 'BoletosReservas':reservas_todos})


def buscarreserva(request):
    return render(request,'AppFinal/busquedaReserva.html')


def inicio(request):
    return render(request,'AppFinal/inicio.html')


def contacto(request):
    if request.method == "POST":
        
        miFormulario2 = ContactoFormulario(request.POST)
        print(miFormulario2)
        
        if miFormulario2.is_valid:
            informacion2 = miFormulario2.cleaned_data
            contactos = Contactanos  (Nombre=informacion2["Nombre"], Correo=informacion2["Correo"], Mensaje=informacion2["Mensaje"])
            contactos.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario2 = ContactoFormulario()
    
    return render(request, "AppFinal/contacto.html", {"miFormulario2": miFormulario2})


def reserva(request):
    if request.method == "POST":
        
        miFormulario = ReservaFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            boletoreserva = BoletosReservas  (Nombre=informacion["Nombre"], Apellido=informacion["Apellido"], Correo=informacion["Correo"], Cantidad_Boletos=informacion["Cantidad_Boletos"])
            boletoreserva.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = ReservaFormulario()
    
    return render(request, "AppFinal/reserva.html", {"miFormulario": miFormulario})


def trabajo(request):
    if request.method == "POST":
        
        miFormulario3 = TrabajaFormulario(request.POST)
        print(miFormulario3)
        
        if miFormulario3.is_valid:
            informacion3 = miFormulario3.cleaned_data
            postulacion = Trabaja  (Nombre=informacion3["Nombre"], Apellido=informacion3["Apellido"], Correo=informacion3["Correo"], URL_Linkedin=informacion3["URL_Linkedin"])
            postulacion.save()
            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario3 = TrabajaFormulario()
    
    return render(request, "AppFinal/trabajo.html", {"miFormulario3": miFormulario3})


def pagina3(request):
    return HttpResponse('Vista de prueba')

def reservaApi(request):
    reserva_todos = BoletosReservas.objects.all()
    return HttpResponse(serializers.serialize('json',reserva_todos))

def contactoApi(request):
    contacto_todos = Contactanos.objects.all()
    return HttpResponse(serializers.serialize('json',contacto_todos))

def trabajoApi(request):
    trabajo_todos = Trabaja.objects.all()
    return HttpResponse(serializers.serialize('json',trabajo_todos))