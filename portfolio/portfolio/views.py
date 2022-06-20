from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from productos.models import Productos

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def contacto(request):
        doc_externo = open("static/contacto.html")
        plt = Template(doc_externo.read())
        doc_externo.close()
        ctx = Context()
        documento = plt.render(ctx)
        return HttpResponse(documento)

def galeria(request):
    doc_externo = open("static/galeria.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def login(request):
    doc_externo = open("static/login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def tienda(request):
    doc_externo = open("static/tienda.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def recover_login(request):
    doc_externo = open("static/recover_login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def register(request):
    doc_externo = open("static/register.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def tracking(request):
    doc_externo = open("static/tracking.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def donacion(request):
    doc_externo = open("static/donacion.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def donacion2(request):
    return render(request, 'donacion.html')

def login(request):
    return render(request, 'login.html')

def resultado(request):
    ##mensaje = f'se ha logeado el usuario {request.GET{"correo"}}'
    llamadabd = Productos.objects.filter(nombre__icontains = "pelota")
    contexto = {'datos':llamadabd}
    return render(request,"resultado.html", contexto)