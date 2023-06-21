from django.shortcuts import render
from django.views import generic

# DB
from .models import Portafolio, Habilidades, Certificaciones, Proyectos

# Create your views here.
def IndexView(request):
    template_name = "main/index.html"

    try:
        portafolio = Portafolio.objects.get(id=1)
    except:
        portafolio = {"texto_largo": "Objeto no encontrado", "imagen":"Imagen no encontrada"}

    habilidades = Habilidades.objects.all()
    certificaciones = Certificaciones.objects.all()
    proyectos = Proyectos.objects.all()

    context = {'portafolio': portafolio, 'habilidades': habilidades, 'certificaciones': certificaciones, 'proyectos': proyectos}
    return render(request, template_name, context)

class AtributionView(generic.TemplateView):
    template_name = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name = "error/500/500.html"
