from .forms import AnimalForm
from django.shortcuts import render, redirect
from .models import Animal

from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def animales(request, id):
    animal = Animal.objects.all().filter(numChip=id)
    datos = {
        'animal': animal
    }
    return render(request, 'core/plantillaperosnal.html', datos)


def form_animal(request):
    datos = {
        'form': AnimalForm()
    }
    if request.method == 'POST':
        formulario = AnimalForm(request.POST, request.FILES)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados de manera correcta"
        else:
            formulario = AnimalForm()
            datos['mensaje'] = "Error"
        
    return render(request, 'core/form_animal.html', datos)  
    


def contactos(request):
    return render(request, 'core/contactos.html')


def gatos(request):
    animal = Animal.objects.all().filter(especie=1)
    datos = {
        'animal': animal
    }
    return render(request, 'core/gatos.html', datos)


def nosotros(request):
    return render(request, 'core/nosotros.html')


def perros(request):
    animal = Animal.objects.all().filter(especie=2)
    datos = {
        'animal': animal
    }
    return render(request, 'core/perros.html', datos)


def plantilapersonal(request):
    return render(request, 'core/plantillaperosnal.html')


def form_mod_animal(request, id):
    animal = Animal.objects.get(numChip=id)
    datos = {
        'form': AnimalForm(instance=animal)
    }
    if request.method == 'POST':
        formulario = AnimalForm(request.POST, request.FILES, instance=animal )
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados de manera correcta"
        else:
            datos['mensaje'] = "Error"
    return render(request, 'core/form_mod_animal.html', datos)


def form_del_perros(request, id):
    animal = Animal.objects.get(numChip=id)
    animal.delete()
    return redirect(to="perros")


def form_del_gatos(request, id):
    animal = Animal.objects.get(numChip=id)
    animal.delete()
    return redirect(to="gatos")
