from django.http import HttpResponse
from django.template import Template, Context
import os

def inicio(request):
    archivo = open(r"C:\Users\angel\Desktop\Python-coderhouse\desafio_django\mvt_balatorreangelina\templates\inicio.html")
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)