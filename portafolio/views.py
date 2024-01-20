from django.shortcuts import render
from portafolio.models import Project


# Create your views here.
def home(request):
    # --> Obtener todos los proyectos de la base de datos
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})