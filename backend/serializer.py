from rest_framework import serializers
from .models import *

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enunciado
        fields = '__all__'

class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = '__all__'

class PreguntaSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
        extra_kwargs = {'personas': {'write_only': True}}

class PersonasGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','apellido','email')

class GrupoRetrieveSerializer(serializers.ModelSerializer):
    personas = PersonasGrupoSerializer(many=True)

    class Meta:
        model = Grupo
        fields = ('nombre','personas')

# class PruebaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prueba
#         fields = '__all__'

class EvaluacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'  

class EvaluacionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('id','nombre','fechaCreacion','fechaCierre') 

class EvaluacionActivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('id','nombre','fechaCreacion','fechaCierre') 

#NEW

class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id','contenido', 'correcta']

class EnunciadoSerializer(serializers.ModelSerializer):
    alternativas = AlternativaSerializer(many=True)
    class Meta:
        model = Enunciado
        fields  = ['id','pregunta', 'alternativas','contenido']

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['alternativas'] = [
    #         alternativa for alternativa in representation['alternativas'] if alternativa['correcta'] == True
    #     ]
    #     return representation
    
class PreguntaSerializer(serializers.ModelSerializer):
    enunciados = EnunciadoSerializer(many=True)
    class Meta:
        model = Pregunta
        fields = ['id', 'orden', 'enunciados', 'tipo']

class PruebaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True)
    class Meta:
        model = Prueba
        fields = ['nombre', 'preguntas']

class PruebaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        # fields = ['id','nombre','cantidadPreguntas']
        fields = '__all__'

class PruebaSerializerEvaluate(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = ['id','nombre']

class GrupoSerializerEvaluate(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id','nombre']

class EvaluacionSerializer(serializers.ModelSerializer):
    prueba = PruebaSerializerEvaluate()
    grupo = GrupoSerializerEvaluate()
    class Meta:
        model = Evaluacion
        fields = [ 'nombre','fechaCreacion','fechaCierre','activa', 'grupo', 'prueba']