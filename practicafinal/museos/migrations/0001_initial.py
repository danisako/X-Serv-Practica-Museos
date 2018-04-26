# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('usuario', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('usuario', models.CharField(max_length=32)),
                ('museo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('horario', models.TimeField()),
                ('direccion', models.TextField()),
                ('enlace', models.URLField()),
                ('accesibilidad', models.PositiveSmallIntegerField()),
                ('equipamiento', models.TextField()),
                ('transporte', models.TextField()),
                ('nombrevia', models.CharField(max_length=64)),
                ('clasevia', models.CharField(max_length=32)),
                ('tiponum', models.CharField(max_length=1)),
                ('numero', models.IntegerField()),
                ('planta', models.CharField(max_length=16)),
                ('orientacion', models.TextField()),
                ('localidad', models.CharField(max_length=8)),
                ('provincia', models.CharField(max_length=8)),
                ('codigopostal', models.IntegerField()),
                ('barrio', models.CharField(max_length=32)),
                ('distrito', models.CharField(max_length=16)),
                ('coordx', models.IntegerField()),
                ('coordy', models.IntegerField()),
                ('latitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('longitud', models.DecimalField(decimal_places=18, max_digits=20)),
                ('telefono', models.IntegerField()),
                ('comentarios', models.ForeignKey(to='museos.Comentario')),
            ],
        ),
    ]
