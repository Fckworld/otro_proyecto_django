# Generated by Django 4.0.4 on 2022-06-18 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50, verbose_name='LA FUCKING DIRECCION')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='InfoContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_razon', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('comuna', models.CharField(max_length=30)),
                ('comentario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('seccion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('abstract', models.TextField()),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruebaApp.speaker')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruebaApp.track')),
            ],
        ),
    ]
