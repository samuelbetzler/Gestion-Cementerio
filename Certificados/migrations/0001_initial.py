# Generated by Django 5.0.6 on 2024-05-12 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.tramite')),
            ],
        ),
    ]
