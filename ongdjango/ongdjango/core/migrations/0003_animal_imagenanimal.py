# Generated by Django 3.2.3 on 2021-06-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210618_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='imagenAnimal',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
