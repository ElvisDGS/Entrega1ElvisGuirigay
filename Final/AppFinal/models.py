from django.db import models

class BoletosReservas(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Cantidad_Boletos= models.IntegerField()


class Contactanos(models.Model):
    Nombre = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Mensaje= models.CharField(max_length=200)


class Trabaja(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.EmailField()
    URL_Linkedin= models.URLField()