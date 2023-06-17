# Generated by Django 4.2.2 on 2023-06-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=360, null=True)),
                ('tags', models.CharField(max_length=400, null=True)),
                ('url', models.CharField(max_length=500)),
                ('priority', models.FloatField(default=0.5)),
                ('content', models.TextField(max_length=5000)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('create', models.DateField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('alt_image', models.CharField(max_length=150, null=True)),
                ('autor', models.CharField(default='Estuardo Ramírez', max_length=200)),
                ('visits', models.IntegerField(default=0, null=True, verbose_name='Total Visitas')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'db_table': 'Articulo',
            },
        ),
    ]