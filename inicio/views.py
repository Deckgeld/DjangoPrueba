from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request,"inicio/principal.html")

def contacto(request):
    return  render(request,"inicio/contacto.html")