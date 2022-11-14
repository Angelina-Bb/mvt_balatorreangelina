from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def fecha_actual(request):
    hoy=datetime.now().strftime("%d/%m/%Y")
    return HttpResponse(hoy)

def vista_familia(request):
    archivo = open(r"C:\Users\angel\Desktop\Python-coderhouse\desafio_django\mvt_balatorreangelina\templates\inicio.html")
    plantilla = Template(archivo.read())
    archivo.close()
    nombre = ['Valeria Balatorre', 'Noah Knazovic', 'Debora Vito']
    edad = ['24', '4', '51']
    hoy = datetime.now().strftime("%d/%m/%Y")
    datos = {'Nombre':nombre, 'Edad':edad, 'Fecha':hoy}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
