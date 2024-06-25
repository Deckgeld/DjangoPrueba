from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm

# Create your views here.
def registros(request):
    # se obtienen todos los registros de la tabla Alumnos
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista