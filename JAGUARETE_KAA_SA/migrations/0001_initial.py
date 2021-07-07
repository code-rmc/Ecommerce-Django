# Generated by Django 3.2.4 on 2021-06-19 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=80)),
                ('imagen', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JAGUARETE_KAA_SA.categoria')),
            ],
        ),
    ]
