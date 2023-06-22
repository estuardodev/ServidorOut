from django.shortcuts import render, get_object_or_404
from .models import Articulo
from django.db.models import Q, Sum
from django.views import generic


# Create your functions here.

# Create your views here.
def IndexView(request):
    template_name = "blog/index.html"

    # Obtener registros de DB
    package_articulos = Articulo.objects.filter(status=True).exclude(id=1).order_by('-id')[:30]  # Se obtienen y se ordenan del último al primero
    all_articulos = Articulo.objects.filter(status=True).exclude(id=1).order_by('-id')
    totales_visitas = package_articulos.aggregate(Sum('visits'))['visits__sum']

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        search_articulo = all_articulos.filter(Q(tittle__icontains=search) | Q(tags__icontains=search) | Q(create__icontains=search)).distinct()
        # Renderización si el usuario realizó una búsqueda
        context = {'search': search_articulo, 'totales_visitas': totales_visitas}
        if not search_articulo:
            context = {'search': "No Encontrado", 'totales_visitas': totales_visitas}
        else:
            context = {'search': search_articulo, 'totales_visitas': totales_visitas}
        return render(request, template_name, context)

    # Renderización del template normalmente
    context = {'articulos': package_articulos, 'totales_visitas': totales_visitas}
    return render(request, template_name, context)

def ArticuloView(request, url: str, id: int):
    template_name = "blog/articulo/articulo.html"

    # Verificamos que el id solicitado sea correcto
    articulo_right = get_object_or_404(Articulo, pk=id, status=True)

    # Guardar visita
    articulo = Articulo.objects.get(pk=id)
    articulo.visits += 1
    articulo.save()

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        search_articulo = Articulo.objects.filter(
            Q(tittle__icontains=search) |
            Q(tags__icontains=search) |
            Q(create__icontains=search),
            status=True
        ).distinct()
        context = {'search': search_articulo}

        if not search_articulo:
            context = {'search': "No Encontrado"}
        else:
            context = {'search': search_articulo}
        
    else:
        context = {'articulo': articulo}
    
    return render(request, template_name, context)

def allView(request):
    template_name = "blog/all.html"
    no = 1

    filters = request.GET.get('filter')
    if filters == 'recent':
        articulos = Articulo.objects.filter(status=True).order_by('-date_create')
        context = {'all': articulos, 'no': no, 'recent_active':True} # Retorno del template
    elif filters == 'popular':
        articulos = Articulo.objects.filter(status=True).order_by('-visits')
        context = {'all': articulos, 'no': no, 'popular_active':True} # Retorno del template
    else:
        articulos = Articulo.objects.filter(status=True).order_by('-id')
        context = {'all': articulos, 'no': no, 'all_active':True} # Retorno del template

    return render(request, template_name, context)

class RssView(generic.ListView):
    template_name = 'rss.xml'
    context_object_name = 'data'
    content_type='text/xml'
    def get_queryset(self):
        return Articulo.objects.filter(status=True).exclude(id=1).order_by("-id")[:20]

class Error404View(generic.TemplateView):
    template_name = "error/404/404.html"

class Error500View(generic.TemplateView):
    template_name = "error/500/500.html"
