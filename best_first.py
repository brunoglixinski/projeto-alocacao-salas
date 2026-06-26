import numpy as np
import time
from modelos import Disciplina, Sala, Horario, Alocacao
from dados_teste import lista_salas, lista_disciplinas, lista_horarios, restricoes_professores
from validador import alocacaoValida

def calcularPrioridade(Disciplina):
    # atribui como primeiro valor de prioridade a quantidade de alunos da turma
    score = Disciplina.capacidade

    # se a sala precisar de projetor, a prioridade de alocacao aumenta
    if Disciplina.projetor:
        score += 50

    # Quanto menos dias disponíveis o professor tem, mais difícil é alocar a disciplina.
    maxDias = 5
    diasDisponiveis = len(restricoes_professores.get(Disciplina.prof, ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]))
    score += (maxDias - diasDisponiveis) * 30 # Até +90 pts se o professor tiver muitas restrições

    return score

def ordenaDisciplinas(lista_disciplinas):
    i = 0
    j = 0

    # Loop que controla quantas passagens são necessárias pra ordenar a lista
    for j in range(len(lista_disciplinas)):
        #Loop que controla o bubble sort de fato, dupla a dupla
        for i in range(len(lista_disciplinas) - 1):
            if calcularPrioridade(lista_disciplinas[i]) < calcularPrioridade(lista_disciplinas[i+1]):
                lista_disciplinas[i], lista_disciplinas[i+1] = lista_disciplinas[i+1], lista_disciplinas[i]

    return lista_disciplinas


def bestFirst(dataset="realista"):
    # ALTERADO: Usando perf_counter para precisão máxima do processador
    tempoInicio = time.perf_counter()
    nosGerados = 0
    nosExpandidos = 0

    # Captura o array de disciplinas dinamicamente de acordo com o cenário escolhido
    disciplinas_escolhidas = lista_disciplinas.get(dataset, lista_disciplinas["realista"])

    # Ordena apenas as disciplinas do cenário atual
    ordenadas = ordenaDisciplinas(disciplinas_escolhidas)

    lista_alocados = []
    lista_nao_alocados = []

    # Evita alocar turmas pequenas em salas gigantes de primeira!
    salas_ordenadas = sorted(lista_salas, key=lambda s: s.capacidade)

    # Loop principal percorre cada disciplina da lista ordenada
    for disciplina in ordenadas:

        # Cada disciplina que começa a processar conta como 1 noExpandido
        nosExpandidos += 1
        alocou = False

        for horario in lista_horarios:
            for sala in salas_ordenadas:
                # Cada combinação Sala + Horário testada conta como 1 noGerado
                nosGerados += 1

                if alocacaoValida(disciplina, sala, horario, lista_alocados):
                    # 1. cria o objeto de Alocação usando a classe do modelos.py
                    nova_alocacao = Alocacao(sala, disciplina, horario)
                    
                    # 2. guarda na lista de sucesso
                    lista_alocados.append(nova_alocacao)
                    
                    # 3. sinaliza que deu certo e quebra o loop do horario
                    alocou = True
                    break

            # 4. quando a alocacao da sala der certo, fazemos o break no loop de fora
            if alocou:
                break

        # Se saiu dos loops e a variável continuar False, vai para os não alocados
        if not alocou:
            lista_nao_alocados.append(disciplina)

    # Cálculo final de tempo mantendo 3 casas decimais (float)
    # Subtraímos os tempos (em segundos), multiplicamos por 1000 e arredondamos para 3 casas
    tempo_gasto = round((time.perf_counter() - tempoInicio) * 1000, 3)
    
    conflitos_restantes = len(lista_nao_alocados)

    return lista_alocados, tempo_gasto, nosExpandidos, nosGerados, conflitos_restantes