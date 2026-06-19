import numpy as np
from modelos import Disciplina, Sala, Horario, Alocacao
from dados_teste import lista_salas, lista_disciplinas, lista_horarios
from validador import alocacaoValida

def calcularPrioridade(Disciplina):
    score = Disciplina.capacidade

    if Disciplina.projetor:
        score += 50

    return score

def ordenaDisciplinas(lista_disciplinas):
    

def bestFirst():
    lista_alocados = []
    lista_nao_alocados = []

    alocacaoValida()