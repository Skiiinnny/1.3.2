# Generated by Django 3.2.3 on 2021-06-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_animal_imagenanimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagenAnimal',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
