from django.db import models

class MiUser(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    email = models.EmailField()
    telefono = models.CharField()
    edad = models.IntegerField()
    es_admin = models.BooleanField(default = False)