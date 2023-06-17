from django.shortcuts import render, get_object_or_404
from .models import Articulo
from django.db.models import Q, Sum

# Create your views here.
def IndexView(request):
    template_name = "blog/index.html"

    # Obtener registros de DB
    articulos = Articulo.objects.filter(status=True).order_by('-id')  # Se obtienen y se ordenan del último al primero
    articulos_count = articulos.count()  # Se cuenta cuántos artículos hay
    totales_visitas = articulos.aggregate(Sum('visits'))['visits__sum']
    img = Articulo.objects.filter(id=1)  # Imagen de la pestaña
    resta = articulos_count - 6  # Resta para artículos a mostrar

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        articulo1 = articulos.filter(Q(tittle__icontains=search) | Q(tags__icontains=search) | Q(create__icontains=search)).distinct()
        # Renderización si el usuario realizó una búsqueda
        context = {'search': articulo1, 'articulos': articulo1}
        return render(request, template_name, context)

    # Renderización del template normalmente
    context = {'articulos': articulos, 'resta': resta, 'img': img, 'totales_visitas': totales_visitas}
    return render(request, template_name, context)



def ArticuloView(request, url: str, id: int):
    # Verificamos que el id solicitado sea correcto
    articulo_right = get_object_or_404(Articulo, pk=id, status=True)

    template_name = "blog/articulo/articulo.html"

    # Guardar visita
    articulo = Articulo.objects.get(pk=id)
    articulo.visits += 1
    articulo.save()

    # Verificación de si el usuario realiza una búsqueda
    search = request.GET.get('search')
    if search:
        articulo1 = Articulo.objects.filter(
            Q(tittle__icontains=search) |
            Q(tags__icontains=search) |
            Q(create__icontains=search),
            status=True
        ).distinct()
        context = {'search': articulo1}
    else:
        context = {'articulo': articulo}
    
    return render(request, template_name, context)


def allView(request):
    template_name = "blog/all.html"
    # Obtener registros de la base de datos
    articulos = Articulo.objects.filter(status=True).order_by('-id')
    no = 1

    # Retorno del template
    context = {'all': articulos, 'no': no}
    return render(request, template_name, context)
