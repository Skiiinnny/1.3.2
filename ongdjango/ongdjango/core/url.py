from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import animales, form_animal, contactos, gatos, index, nosotros, perros, plantilapersonal, form_mod_animal


urlpatterns = [
    path('animales', animales, name="animales"),
    path('form_animal', form_animal, name="form_animal"),
    path('contactos', contactos, name="contactos" ),
    path('gatos', gatos, name="gatos"),
    path('', index, name="index"),
    path('nosotros', nosotros, name="nosotros"),
    path('perros', perros, name="perros"),
    path('plantillapersonal', plantilapersonal, name="plantillapersonal"),
    path('form_mod_animal/<id>', form_mod_animal, name="form_mod_animal")

]
