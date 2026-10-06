from django.shortcuts import render, redirect
from .models import Post
from django import forms

def inicio(request):
    contexto_inicio = { 'titulo': 'Página de Inicio', 'seccion': 'Principal' }
    return render(request, "posts/inicio.html", contexto_inicio)

def acerca(request):
    contexto_acerca = { 'titulo': 'Acerca de', 'seccion': 'Acerca' }
    return render(request, "posts/acerca.html", contexto_acerca)

def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")

    contexto = {
        'posts':posts,
    }
    return render(request, "posts/lista_posts.html", contexto)
