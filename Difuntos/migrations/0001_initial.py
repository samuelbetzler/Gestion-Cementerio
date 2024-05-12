# Generated by Django 5.0.6 on 2024-05-12 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CausaMuerte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cau_mue', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Difunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_difu', models.TextField()),
                ('lastn_difu', models.TextField()),
                ('fch_naci_difu', models.DateField()),
                ('fch_muerte_difu', models.DateField()),
                ('code_acta_difu', models.CharField(max_length=5)),
                ('id_cau_mue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Difuntos.causamuerte')),
            ],
        ),
    ]