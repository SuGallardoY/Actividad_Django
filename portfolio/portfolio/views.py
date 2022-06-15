from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def contacto(request):
    doc_externo = open("static/templates/contacto.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def galeria(request):
    doc_externo = open("static/templates/galeria.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def login(request):
    doc_externo = open("static/templates/login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def tienda(request):
    doc_externo = open("static/templates/tienda.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def recover_login(request):
    doc_externo = open("static/templates/recover_login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def register(request):
    doc_externo = open("static/templates/register.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def tracking(request):
    doc_externo = open("static/templates/tracking.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def donacion(request):
    doc_externo = open("static/templates/donacion.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)