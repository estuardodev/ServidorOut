from django.shortcuts import render
from django.views import generic

# DB
from .models import Portafolio, Habilidades, Certificaciones

# Create your views here.
def IndexView(request):
    template_name = "main/index.html"

    portafolio = Portafolio.objects.get(id=1)
    habilidades = Habilidades.objects.all()
    certificaciones = Certificaciones.objects.all()

    context = {'portafolio': portafolio, 'habilidades': habilidades, 'certificaciones': certificaciones}
    return render(request, template_name, context)

class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"