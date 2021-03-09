from django.http import HttpResponse
import datetime
def saludo(request): #primera vista 
    return HttpResponse("Hello world")

def despedida(request): #segunda vista
    return HttpResponse("hasta luego")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    <body>
    </html>
    """% fecha_actual
    return HttpResponse (documento)