# Generated by Django 5.0.6 on 2024-07-06 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_producto_caracteristicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(blank=True, max_length=40, verbose_name='Habitacion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.CharField(blank=True, max_length=40, verbose_name='Servicio'),
        ),
    ]