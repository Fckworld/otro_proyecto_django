from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50,verbose_name='LA FUCKING DIRECCION') #ESTO SOLO CAMBIA COMO SE MUESTRA AL AGREGAR EN DJANGO ADMIN
    email = models.EmailField(blank=True,null=True) #ESTO PERMITE INGRESAR DATOS EN BLANCO EN ADMIN
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return "Clientexxxx: %s "%(self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha =  models.DateField()
    entregado = models.BooleanField()
#DESPUES DE CREAR LOS MODELOS Y CONFIGURAR LA APP EN SETTINGS, PUEDO
#VERIFICAR SI TOD0 ESTA BIEN CON python manage.py check pruebaAPP

#UNA VEZ TOD0 BIEN, PUEDO HACER LA BASE DE DATOS CON LOS MODELOS QUE HICE, HACIENDO UNA MIGRACION
#python manage.py makemigrations -> esto crea el codigo sql, ahora falta utilizarla
#LUEGO CREAR LAS TABLAS EN SQL, CON LA MIGRACION CORRESPONDIENTE (ESTE CASO 0001)
#python manage.py sqlmigrate pruebaApp 0001
#AHORA FALTA METER LAS TABLAS CREADA EN LA BASE DE DATOS CREADA CON ANTERIORIDAD.
#python manage.py migrate