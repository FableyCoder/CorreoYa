from django.shortcuts import render
from .models import PaquetePermit, Etiqueta

def paquetes(request):
    paquete=PaquetePermit.objects.all()
    return render(request,"paquetes/paquetes.html", {'paquete':paquete})

def etiqueta(request, etiqueta_id):
    etiq=Etiqueta.object.get(id=etiqueta_id)
    paquete=PaquetePermit.objects.filter(categories=etiq)
    return render(request, "paquetes/etiquetas.html", {'etiq':etiq, 'paquete':paquete})