from django.urls import path
from .views import registrar_ponto, cadastrar_funcionario

urlpatterns = [
    path('', registrar_ponto, name='ponto'),
    path('cadastrar/', cadastrar_funcionario, name='cadastrar'),
]
