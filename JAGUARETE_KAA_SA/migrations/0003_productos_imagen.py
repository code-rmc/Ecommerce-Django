# Generated by Django 3.2.4 on 2021-06-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAGUARETE_KAA_SA', '0002_remove_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default='independiente-2021', upload_to=''),
        ),
    ]