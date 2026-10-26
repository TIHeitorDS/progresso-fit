from django.urls import path
from . import views

# treinos/ficha/123/
urlpatterns = [
    path('ficha/<str:matricula>', views.ficha_aluno, name='ficha_aluno')
]