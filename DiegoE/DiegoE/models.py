from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from DiegoE import settings


class Question(models.Model):
    text = models.CharField(max_length=255)  # Texto de la pregunta
    option_a = models.CharField(max_length=255)  # Opción A
    option_b = models.CharField(max_length=255)  # Opción B
    option_c = models.CharField(max_length=255)  # Opción C
    option_d = models.CharField(max_length=255)  # Opción D
    correct_answer = models.CharField(
        max_length=1, 
        choices=[('A', 'Opción A'), ('B', 'Opción B'), ('C', 'Opción C'), ('D', 'Opción D')],
    )  # Respuesta correcta

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    # Cambiar la referencia de 'User' a 'settings.AUTH_USER_MODEL'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con el usuario
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Relación con la pregunta
    answer = models.CharField(max_length=1)  # Respuesta seleccionada por el usuario (A, B, C, D)
    is_correct = models.BooleanField()  # Si la respuesta es correcta o no

    def __str__(self):
        return f"Respuesta de {self.user.username} a la pregunta: {self.question.text}"
    
class Usuario(AbstractUser):
    tipo_usuario = models.CharField(max_length=50)  




class EstadoMisiones(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Eventos(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

    
    from django.db import models

class Misiones(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.ForeignKey('EstadoMisiones', on_delete=models.CASCADE)
    evento = models.ForeignKey('Eventos', on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField()
    fecha_entrega = models.DateTimeField()

    def __str__(self):
        return str(self.nombre)

    

class Roles(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    

    from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.username

