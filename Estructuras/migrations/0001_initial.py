# Generated by Django 5.0.6 on 2024-05-12 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoEstructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_est_estruc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LugarEstructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zona', models.TextField()),
                ('name_manza', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tipo_estruc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cruces', models.BooleanField()),
                ('id_est_estruc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estructuras.estadoestructura')),
                ('id_lugar_estruc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estructuras.lugarestructura')),
                ('id_tipo_estruc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estructuras.tipoestructura')),
            ],
        ),
    ]
