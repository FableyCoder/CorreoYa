from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Reviews

# Create your views here.
def opinion(request):
    opiniones=Reviews.objects.all()
    paginador=Paginator(opiniones,4)

    numero_pag=request.GET.get("page")
    pag_obj=paginador.get_page(numero_pag)
    return render(request, "opiniones/foro.html",{"pag_obj": pag_obj})