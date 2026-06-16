import random
import time
from modelos import Sala, Disciplina, Horario, Alocacao

def subidamontanha(dataset):
    print("cenario escolhido:", dataset)
    # Iniciando o cronômetro para simular o tempo de execução
    tempo_inicio = time.time()
    
    salas = [
        Sala(nome="Lab 1", capacidade=30, projetor=True),
        Sala(nome="Lab 3", capacidade=40, projetor=True),
        Sala(nome="Sala 102", capacidade=35, projetor=False), # Corrigido aqui
        Sala(nome="Sala 204", capacidade=50, projetor=True)  # Corrigido aqui
    ]
    
    # Criando instâncias das disciplinas do curso
    disciplinas = [
        Disciplina(nome="Inteligência Artificial", prof="Pedro Miotto", capacidade=38, projetor=True),
        Disciplina(nome="Estrutura de Dados", prof="Seghatti", capacidade=45, projetor=True),
        Disciplina(nome="Compiladores", prof="Marcos", capacidade=25, projetor=False),
        Disciplina(nome="Redes de Computadores", prof="Carlos", capacidade=30, projetor=True),
        Disciplina(nome="Sistemas Operacionais", prof="Fabio", capacidade=28, projetor=True)
    ]
    
    # Definindo os blocos de horários padrão que você estipulou
    horarios_segunda = [
        Horario(dia="Segunda", horas="08:00-10:00"),
        Horario(dia="Segunda", horas="10:00-12:00"),
        Horario(dia="Segunda", horas="13:00-15:00"),
        Horario(dia="Segunda", horas="15:00-17:00")
    ]
    
    horarios_terca = [
        Horario(dia="Terça", horas="08:00-10:00"),
        Horario(dia="Terça", horas="10:00-12:00"),
        Horario(dia="Terça", horas="13:00-15:00"),
        Horario(dia="Terça", horas="15:00-17:00")
    ]

    todos_horarios = horarios_segunda + horarios_terca
    
    # Gerando um estado simulado combinando as instâncias das classes
    melhor_estado = []
    
    # Alocando IA na segunda de manhã
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[0], disciplina=disciplinas[0]))
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[1], disciplina=disciplinas[0]))
    
    # Alocando Estrutura de Dados na terça de manhã
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[4], disciplina=disciplinas[1]))
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[5], disciplina=disciplinas[1]))
    
    # Alocando Redes na segunda de tarde
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[2], disciplina=disciplinas[3]))
    
    # Alocando Compiladores na terça de tarde
    melhor_estado.append(Alocacao(sala=random.choice(salas), horario=todos_horarios[7], disciplina=disciplinas[2]))

    # Adicionando um espaço livre/vago de teste usando a sua lógica estrutural
    melhor_estado.append(Alocacao(sala=salas[0], horario=todos_horarios[3], disciplina=None))

    # Forçando um delay pequeno para simular o custo de processamento do Hill Climbing
    time.sleep(random.uniform(0.05, 0.12))
    
    # Cálculo final das métricas do mock
    tempo_gasto = int((time.time() - tempo_inicio) * 1000)
    total_nos = random.randint(300, 1200)
    conflitos_restantes = 0 # Mude para um número maior que 0 se quiser ver a interface indicar erro
    
    return melhor_estado, tempo_gasto, total_nos, conflitos_restantes