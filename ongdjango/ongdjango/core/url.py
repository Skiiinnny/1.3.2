from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import animales, form_animal, contactos, gatos, index, nosotros, perros, plantilapersonal, form_mod_animal, form_del_perros, form_del_gatos


urlpatterns = [
    path('animales/<id>', animales, name="animales"),
    path('form_animal', form_animal, name="form_animal"),
    path('contactos', contactos, name="contactos" ),
    path('gatos', gatos, name="gatos"),
    path('', index, name="index"),
    path('nosotros', nosotros, name="nosotros"),
    path('perros', perros, name="perros"),
    path('plantillapersonal', plantilapersonal, name="plantillapersonal"),
    path('form_mod_animal/<id>', form_mod_animal, name="form_mod_animal"),
    path('form_del_perros/<id>', form_del_perros, name="form_del_perros"),
    path('form_del_gatos/<id>', form_del_gatos, name="form_del_gatos")

]
