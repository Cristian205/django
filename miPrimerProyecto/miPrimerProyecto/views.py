from django.http import HttpResponse
import datetime
from django.template import loader, Context, Template
from django.shortcuts import render


def fecha(request):
    fechaActual=datetime.datetime.now()
    documento= """<HTML>
                        <HEAD>
                            <TITLE>Esta es una estructura basica de un documento HTML</TITLE>
                        </HEAD>
                        <BODY>
                            <h1> Usted Ingresó o actualizó esta vista en la fecha %s </h1>
                        </BODY>
                   </HTML>""" % fechaActual
    return HttpResponse(documento) 

def saludar(request):
    doc_externo=open("C:/Users/usuar/Documents/Proyecto_python_1/miPrimerProyecto/miPrimerProyecto/plantillas/SegundaPlantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    cxt=Context()
    documento=plt.render(cxt)
    return HttpResponse(documento)

def tareasEnListadas(request):
    Tareas=["Aprender sobre la internet","Aprender HTML","Aprender CSS","Practicar Python","Aprender Django","Construir mi propia WEB "]
    doc_externo=loader.get_template("SegundaPlantilla.html")
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)

def games(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s/%s/%s a las %s" %(dia, mes ,agno, hora)

    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)

def musica(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s/%s/%s a las %s" %(dia, mes ,agno, hora)

    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)

def tecnologia(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s/%s/%s a las %s" %(dia, mes ,agno, hora)

    doc_externo=loader.get_template("tecnologias.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)
