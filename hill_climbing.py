import random
import copy
import time
from modelos import Alocacao  
#Bruno Glixinski, Kayra Yokoyama, Eric Barbachã e Gabriel Costa

# Importando os dados do arquivo central
from dados_teste import lista_salas, lista_disciplinas, lista_horarios, restricoes_professores

# função de avaliação, conta penalidades aos estados 
def avaliacao(alocacao):
    penalidade = 0

    # penalidades por capacidade, projetor e dias do professor
    for i in range(len(alocacao)):
        sala = alocacao[i][0]
        disciplina = alocacao[i][1]
        horario = alocacao[i][2] # pegando o horario aqui tbm pra validar o dia
        
        if disciplina.capacidade > sala.capacidade: penalidade += 1
        if disciplina.projetor and not sala.projetor: penalidade += 1
        
        # checa se o dia sorteado ta na lista de dias do professor
        dias_permitidos = restricoes_professores.get(disciplina.prof, [])
        if horario.dia not in dias_permitidos:
            penalidade += 10 # peso 10 pra forçar o algoritmo a fugir desse erro

    # penalidades por professor e sala no mesmo horário
    for i in range(len(alocacao)):
        sala_i, disc_i, hor_i = alocacao[i] # Desempacotamento da alocação i
        #vamos comparar a alocação i com todas as alocações j posteriores para evitar comparações repetidas
        for j in range(i + 1, len(alocacao)):
            sala_j, disc_j, hor_j = alocacao[j] # Desempacotamento da alocação j
            
            # mesmo professor no mesmo horário em lugares diferentes
            if disc_i.prof == disc_j.prof and hor_i.dia == hor_j.dia and hor_i.horas == hor_j.horas:
                penalidade += 1
                
            # mesma sala no mesmo horário com disciplinas diferentes
            if sala_i.nome == sala_j.nome and hor_i.dia == hor_j.dia and hor_i.horas == hor_j.horas:
                penalidade += 1

    return penalidade

# Gera vizinho aleatório trocando sala, horário ou disciplina de uma alocação
# porém por mutação, troca quando escolhido um tipo, ou sala e horario, ou discplina
def gerar_vizinho_mutacao(alocacao, disciplinas_ativas):
    #vamos escolher um índice aleatório para modificar a alocação nessa posição
    i = random.randrange(len(alocacao))
    
    # e escolher um tipo de modificação, mudar o horário ou mudar disciplina
    tipo = random.choice(['sala_horario', 'disciplina'])
    
    novo = alocacao.copy()  # cópia rasa da lista, estava usando deepcopy e demorou 40 minutoskkkk
    
    #se o tipo for sala_horario, vamos escolher uma nova sala e um novo horário aleatórios para a alocação i
    if tipo == 'sala_horario':
        nova_sala = random.choice(lista_salas) #uma escolha aleatória de sala
        novo_horario = random.choice(lista_horarios) #uma escolha aleatória de horário
        novo_item = [nova_sala, novo[i][1], novo_horario] #novo item com a nova sala, a mesma disciplina e o novo horário
        novo[i] = novo_item #novo estado, a alocação i é substituida pelo novo item

    else:
        # Escolhe um segundo índice aleatório diferente de i
        j = random.randrange(len(novo))
        while j == i:
            j = random.randrange(len(novo))
        
        # Em vez de sortear uma nova da lista, troca as duas de lugar 
        # Mantém as salas e horários fixos, só permuta qual disciplina vai em cada canto
        disc_i = novo[i][1]
        disc_j = novo[j][1]
        
        novo[i] = [novo[i][0], disc_j, novo[i][2]]
        novo[j] = [novo[j][0], disc_i, novo[j][2]]
    
    return novo

# gerar k vizinhos e retornar o melhor (ou um aleatório entre os melhores)
def gerar_melhor_entre_k(alocacao, disciplinas_ativas, k=10):
    melhor = None #var none que vai receber o nosso melhor entre 10 vizinhos gerados
    melhor_val = float('inf') #inicializamos a melhor avaliação com infinito, para garantir que qualquer vizinho encontrado será melhor
    # usar infinitos para garantir que qualquer vizinho encontrado será melhor
    # qualquer valor real calculado será meno
    #  portanto, o primeiro vizinho avaliado automaticamente substitui esse valor inicial.
    
    for _ in range(k):
        viz = gerar_vizinho_mutacao(alocacao, disciplinas_ativas)
        val = avaliacao(viz)
        if val < melhor_val:
            melhor = viz
            melhor_val = val
    return melhor, melhor_val

# hill climbing com limite de tempo e vizinhos
def hill_climbing_rapido(disciplinas_ativas, max_iter=1000, reinicios=10, k_vizinhos=10):
    melhor_estado_global = None
    melhor_aval_global = float('inf')
    
    total_nos = 0 

    for r in range(reinicios):
        # estado inicial aleatório
        estado_atual = []
        for disc in disciplinas_ativas:
            sala = random.choice(lista_salas)
            horario = random.choice(lista_horarios)
            estado_atual.append([sala, disc, horario])

        aval_atual = avaliacao(estado_atual)
        total_nos += 1 

        for it in range(max_iter):
            vizinho, aval_vizinho = gerar_melhor_entre_k(estado_atual, disciplinas_ativas, k=k_vizinhos)
            total_nos += k_vizinhos 

            if aval_vizinho <= aval_atual:
                estado_atual = vizinho
                aval_atual = aval_vizinho

            if aval_atual == 0:
                break

        if aval_atual < melhor_aval_global:
            melhor_aval_global = aval_atual
            melhor_estado_global = copy.deepcopy(estado_atual)

        if melhor_aval_global == 0:
            break

    return melhor_estado_global, melhor_aval_global, total_nos

def subidamontanha(dataset="realista"):
    print(f"Executando Hill Climbing via API (Dataset: {dataset})...")
    tempoInicio = time.perf_counter()
    
    # Busca no dicionário as disciplinas do cenário atual
    disciplinas_ativas = lista_disciplinas.get(dataset, lista_disciplinas.get("realista", []))
    
    melhor_estado, conflitos, total_nos = hill_climbing_rapido(
        disciplinas_ativas, max_iter=1000, reinicios=10, k_vizinhos=10
    )
    
    lista_alocados = []
    if melhor_estado is not None:
        for item in melhor_estado:
            sala_estado = item[0]
            disc_estado = item[1]
            hor_estado = item[2]
            
            nova_alocacao = Alocacao(sala=sala_estado, disciplina=disc_estado, horario=hor_estado)
            lista_alocados.append(nova_alocacao)
            
        tempo_gasto = round((time.perf_counter() - tempoInicio) * 1000, 3)

    
    return lista_alocados, tempo_gasto, total_nos, conflitos