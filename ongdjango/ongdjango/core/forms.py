from django import forms
from django.forms import ModelForm
from .models import Animal, Especie

class AnimalForm(ModelForm):

    class Meta:
        model = Animal
        fields = ['numChip','nombreAnimal','edadAnimal','generoAnimal','esterilizacion','imagenAnimal','especie']

class AnimalFormMod(ModelForm):
    numChip=forms.IntegerField(disabled=True)
    
    class Meta:
        model = Animal
        fields = ['numChip','nombreAnimal','edadAnimal','generoAnimal','esterilizacion','imagenAnimal','especie']