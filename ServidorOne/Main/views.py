from django.shortcuts import render
from django.views import generic

# Create your views here.
def IndexView(request):
    template_name = "main/index.html"
    return render(request, template_name)

class AtributionView(generic.TemplateView):
    template_name: str = "terceros/atribucion.html"

class Error404View(generic.TemplateView):
    template_name: str = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name: str = "error/500/500.html"