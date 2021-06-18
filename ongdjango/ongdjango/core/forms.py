from django import forms
from django.forms import ModelForm
from .models import Animal

class AnimalForm(ModelForm):

    class Meta:
        model = Animal
        fields = ['numChip','nombreAnimal','edadAnimal','generoAnimal','esterilizacion','especie']
