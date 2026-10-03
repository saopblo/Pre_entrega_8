from django.shortcuts import render


def inicio(request):
    contexto_inicio = { 'titulo': 'Página de Inicio', 'seccion': 'Principal' }
    return render(request, "posts/inicio.html", contexto_inicio)

def acerca(request):
    contexto_acerca = { 'titulo': 'Acerca de', 'seccion': 'Acerca' }
    return render(request, "posts/acerca.html", contexto_acerca)


