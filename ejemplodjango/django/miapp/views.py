from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    respu = "<ul>"
    respu = respu + "<li>elemento1</li>"
    respu = respu + "<li>elemento2</li>"
    respu = respu + "</ul>"

    return  HttpResponse(respu)


def nuevococinero(request):
    return HttpResponse("<p>esta es la pagina nuevo cocinero</p>")

def pedido(request):
    return HttpResponse("<p>esta es la pagina para pedido")

def cliente(request):
    return HttpResponse("<p>esta es la pagina para cliente ")

def factura(request):
    return HttpResponse("<p>esta es la pagina para las facturas ")

def mesero(request):
    return HttpResponse("<p>esta es la pagina para los meseros ")

