from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} - ({self.matricula})'

class Exercicio(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=50)
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    carga = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nome} - {self.grupo_muscular}'