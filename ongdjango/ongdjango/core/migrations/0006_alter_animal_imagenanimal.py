# Generated by Django 3.2.3 on 2021-06-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_animal_imagenanimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='imagenAnimal',
            field=models.ImageField(blank=True, null=True, upload_to='Animal'),
        ),
    ]
