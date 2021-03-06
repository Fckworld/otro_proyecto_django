from django.db import models


# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50,verbose_name='LA FUCKING DIRECCION') #ESTO SOLO CAMBIA COMO SE MUESTRA AL AGREGAR EN DJANGO ADMIN
    email = models.EmailField(blank=True,null=True) #ESTO PERMITE INGRESAR DATOS EN BLANCO EN ADMIN
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return "Clientexxxx: %s "%(self.nombre)


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
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

class InfoContacto(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre_razon = models.CharField(max_length=255)
    rut = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.IntegerField()
    comuna = models.CharField(max_length=30)
    comentario = models.CharField(max_length=255)
    def __str__(self):
        return " Formulario contacto de: %s "%(self.nombre_razon) #ESTO SOLO SE MUESTRA EN ADMIN

class Speaker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=35)
    abstract = models.TextField(blank=False)
    track = models.ForeignKey(Track, on_delete=models.PROTECT)
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)

    def __str__(self):
        a = self.title
        return a