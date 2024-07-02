from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404

######################  alumnos
def registros(request):
    # se obtienen todos los registros de la tabla Alumnos
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos': alumnos})

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