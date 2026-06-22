import numpy as np

def alocacaoValida(nova_disciplina, nova_sala, novo_horario, lista_alocados):
    #primeiro testa se tem capacidade e se tem projetor se necessário
    if nova_disciplina.capacidade > nova_sala.capacidade:
        return False
    elif nova_disciplina.projetor == True and nova_sala.projetor == False:
        return False
    
    for alocacao in lista_alocados:
        #verifica de já não tem alguém no horário e na sala
        if novo_horario.dia == alocacao.horario.dia and novo_horario.horas == alocacao.horario.horas:
            if nova_sala.nome == alocacao.sala.nome:
                return False
            #verifica se não bate horários e professor
            if nova_disciplina.prof == alocacao.disciplina.prof:
                return False
        
    return True
            

