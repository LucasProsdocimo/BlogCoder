from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    dni = models.IntegerField(primary_key = True)

    def __str__(self):
        return f'{self.dni} | {self.nombre} {self.apellido}'

class Posteo(models.Model):

    autor = models.CharField(max_length = 40)
    email = models.EmailField()
    fecha = models.DateField(auto_now_add = True)
    titulo = models.CharField(max_length = 40, primary_key = True)
    cuerpo = models.TextField('')

    def __str__(self):
        return f'{self.titulo} | {self.autor}'

class Comentario(models.Model):

    autor = models.CharField(max_length = 40)
    email = models.EmailField()
    cuerpo = models.TextField('')
    fecha = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.autor} | {self.fecha}'