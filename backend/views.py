from datetime import date
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *
from .models import *

from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class StatementView(viewsets.ModelViewSet):
    queryset = Enunciado.objects.all()
    serializer_class = StatementSerializer

class AlternativeView(viewsets.ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativeSerializer

class PreguntaView(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializerV2

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PersonaView(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class GrupoView(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GrupoRetrieveSerializer(instance)
        return Response(serializer.data)
    
    def post(self,request, pk=None):
        try:
            new = request.data.get('persona')
            instance = self.get_object()
            instance.personas.add(new)

            return Response({'mensaje': 'Elemento agregado correctamente'})
        except:
            return Response({'mensaje': 'ERROR'})

# class EvaluacionView(viewsets.ModelViewSet):
#     serializer_class = EvaluacionSerializer
#     queryset = Evaluacion.objects.all()

class EvaluacionActivaView(viewsets.ModelViewSet):
    serializer_class = EvaluacionActivaSerializer
    fecha_actual = date.today()
    queryset = Evaluacion.objects.filter(fechaCierre__gt=fecha_actual)

#NEW
# class PruebaListView(viewsets.ModelViewSet):
#     queryset = Prueba.objects.all()
#     serializer_class = PruebaListSerializer

# class PruebaDetailView(viewsets.ModelViewSet):
#     queryset = Prueba.objects.all()
#     serializer_class = PruebaSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'prueba_id'

#     def list(self, request, *args, **kwargs):
#         serializer_class = PruebaListSerializer
#         return super().list(request, *args, **kwargs)
    
class PruebaView(viewsets.ModelViewSet):
    serializer_class = PruebaSerializer
    queryset = Prueba.objects.all()

    def __init__(self, *args, **kwargs):
        super(PruebaView, self).__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list':PruebaListSerializer,
            'create': PruebaListSerializer,
            'retrieve':PruebaSerializer,
            'partial_update':PruebaListSerializer,
            'destroy':PruebaListSerializer,
            'update': PruebaListSerializer
        }

    def get_serializer_class(self, *args, **kwargs):
        kwargs['partial'] = True
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(PruebaView, self).get_serializer_class()
        
# class EvaluacionView(viewsets.ModelViewSet):
#     serializer_class = EvaluacionSerializer
#     queryset = Evaluacion.objects.all().select_related('grupo', 'prueba')

class EvaluacionView(viewsets.ModelViewSet):
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all().select_related('grupo', 'prueba')

    def __init__(self, *args, **kwargs):
        super(EvaluacionView, self).__init__(*args, **kwargs)
        self.serializer_action_classes = {
            'list':EvaluacionListSerializer,
            'create': EvaluacionCreateSerializer,
            'retrieve':EvaluacionSerializer,
            'partial_update':EvaluacionCreateSerializer,
            #'update':serializers.AdminUpdateSerializer,
            #'destroy':serializers.AdminRetrieveSerializer,
        }

    def get_serializer_class(self, *args, **kwargs):
        kwargs['partial'] = True
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(EvaluacionView, self).get_serializer_class()
        
class ResultadoView(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadosSerializer