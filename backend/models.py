from django.db import models

TYPES = (
       ('Admin', ('Admin')),
       ('Evaluador', ('Evaluador')),
       ('Visualizador', ('Visualizador')),
   )

TYPES_QUESTION = (
       ('Verdadero/Falso', ('Verdadero/Falso')),
       ('Alternativas', ('Alternativas')),
       ('Semi-Abierta', ('Semi-Abierta')),
       ('Numerica', ('Numerica')),
       ('Matriz', ('Matriz')),
   )

DIFFICULTY = (
       ('baja', ('baja')),
       ('media', ('media')),
       ('alta', ('alta')),
   )

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=40, choices=TYPES)

class Grupo(models.Model):
    nombre = models.CharField(max_length=40)
    cantidadPersonas = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=400)
    imagen = models.CharField(max_length=400)

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='personas')

class Prueba(models.Model):
    nombre = models.CharField(max_length=40)
    cantidadPreguntas = models.PositiveSmallIntegerField(default=0)

class Pregunta(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40, choices=TYPES_QUESTION)
    dificultad = models.CharField(max_length=40, choices=DIFFICULTY)
    tags = models.CharField(max_length=30)
    orden = models.PositiveIntegerField()
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='preguntas')
    
class Evaluacion(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)
    prueba = models.ForeignKey(Prueba, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=40)
    instrucciones = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaCierre = models.DateTimeField(blank=False)
    activa = models.BooleanField()

class Enunciado(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='enunciados')
    contenido = models.TextField()

class Alternativa(models.Model):
    enunciado = models.ForeignKey(Enunciado, on_delete=models.CASCADE, related_name='alternativas')
    correcta = models.BooleanField(blank=False)
    contenido = models.TextField()

class Resultado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='resultados')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='resultados')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='resultados')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='resultados')
    correcta = models.BooleanField()
    dificultad = models.TextField()
    tag = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class Completado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='completado')
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='completado')
    completado = models.IntegerField()  