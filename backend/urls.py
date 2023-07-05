from django.urls import path, include
from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'groups', views.GrupoView)
router.register(r'tests', views.PruebaView, basename='tests')
router.register(r'evaluations', views.EvaluacionView)
router.register(r'active', views.EvaluacionActivaView)
router.register(r'users', views.UsuarioView)
router.register(r'persons', views.PersonaView)
router.register(r'questions', views.PreguntaView)
router.register(r'alternatives', views.AlternativeView)
router.register(r'statements', views.StatementView)
router.register(r'results', views.ResultadoView)
router.register(r'complete', views.CompletadoView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    #path('api/v1/tests/', views.PruebaListView.as_view(), name='prueba_list'),
    #path('api/v1/tests/<int:prueba_id>/', views.PruebaDetailView.as_view(), name='prueba_detail')
]