from django.http import HttpResponse
from appfamilia.models import Familiares

# Create your views here.

def listado_familiares(request):
    listado = Familiares.objects.all()
    vista = ""
    for family in listado:
        vista += f"({family.nombre},{family.edad})" + " | "

    return HttpResponse(vista)