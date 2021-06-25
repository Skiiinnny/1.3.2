from django.db import models

# Create your models here.
class Especie(models.Model):
    idEspecie = models.IntegerField(primary_key=True, verbose_name='Id de especie')
    nombreEspecie = models.CharField(max_length=50, verbose_name='Nombre de la especie')
    
    def __str__(self):
        return self.nombreEspecie

class Animal(models.Model):
    numChip = models.CharField(max_length=50, primary_key=True, verbose_name='Numero de chip')
    nombreAnimal = models.CharField(max_length=50, verbose_name='Nombre animal')
    edadAnimal = models.CharField(max_length=50, blank=True, verbose_name='Edad animal')
    generoAnimal = models.CharField(max_length=50, verbose_name='Genero animal')
    esterilizacion = models.BooleanField(verbose_name='Esterilizacion')
    imagenAnimal = models.ImageField(null=True, blank=True, verbose_name="Imagen")
    especie =models.ForeignKey(Especie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreAnimal
    
    class Meta :
        db_table = "core_Animal"