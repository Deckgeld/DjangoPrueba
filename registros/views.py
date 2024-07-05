from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
import datetime

from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

######################  alumnos
def registros(request):
    # se obtienen todos los registros de la tabla Alumnos
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos': alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

######################  comentarios

#Metodo POST
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request,'registros/comentarios.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

#Vista post 
def contacto(request):
    return render(request,"registros/contacto.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista

#vista get comentarios
def comentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request,"registros/comentarios.html", {'comentarios': comentarios})
    #Indicamos el lugar donde se renderizará el resultado de esta vista

#vista eliminar comentarios
def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminar.html'):
    #se usa get_object_or_404 para obtener el objeto a eliminar
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    
    return render(request, confirmacion, {'comentario': comentario})

#vista editar comentarios
def consultarCometarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    #se usa get_object_or_404 para obtener el objeto a eliminar
    comentario = get_object_or_404(ComentarioContacto, id=id)
    #Referenciamos que el elemento del formulario pertenece al comentario
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    
    return render(request, 'registros/formEditComentario.html', {'comentario': comentario})



######################  consultas
def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(turno__contains='Vesp')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=['Juan', 'Ana'])
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 7, 2)
    fechaFin = datetime.date(2024, 7, 3)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains='10')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})