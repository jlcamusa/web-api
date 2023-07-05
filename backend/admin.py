from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Prueba)
admin.site.register(Evaluacion)
admin.site.register(Pregunta)
admin.site.register(Enunciado)
admin.site.register(Alternativa)
admin.site.register(Resultado)
admin.site.register(Completado)