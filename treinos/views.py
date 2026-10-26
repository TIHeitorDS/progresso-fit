from django.shortcuts import render
from .models import Aluno, Exercicio

def ficha_aluno(request, matricula):
    aluno = Aluno.objects.get(matricula=matricula)
    exercicios = Exercicio.objects.filter(aluno=aluno)

    context = {
        'aluno': aluno,
        'exercicios': exercicios
    }

    return render(request, 'ficha.html', context)