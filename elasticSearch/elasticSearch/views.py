from django.http import HttpResponse
import datetime

def saludo(request): #primera vista

    documento = """<html>
    <body>
    <h1>Hola alumnos esta es nuestra primera paguina con django</h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>Fecha y hora actuales %s</h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual = 18 
    periodo = agno - 2020
    edadFutura = edadActual+ periodo
    documento = "<html><body><h2>en el año %s tendras %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(documento)
