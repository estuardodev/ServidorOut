# Generated by Django 4.2.2 on 2023-06-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_proyectos_alt_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='alt_imagen',
            field=models.CharField(max_length=50, null=True, verbose_name='Alt Imagen'),
        ),
    ]
