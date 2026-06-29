#Bruno Glixinski, Kayra Yokoyama, Erik Felipe e Gabriel Costa
#aqui sao definidas as salas e suas especificidades
class Sala:
    def __init__(self, nome, capacidade, projetor):
        self.nome = nome
        self.capacidade = capacidade
        self.projetor = projetor

#aqui sao definidas as disciplinas, os professores e a capacidade da turma
class Disciplina:
    def __init__(self, nome, prof, capacidade, projetor):
        self.nome = nome
        self.prof = prof
        self.capacidade = capacidade
        self.projetor = projetor

#aqui sao definidos dias e horarios para alocacao de salas
class Horario:
    def __init__(self, dia, horas):
        self.dia = dia
        self.horas = horas

#aqui vai ser armazenado o resultado de cada alocacao
class Alocacao:
    def __init__(self, sala, disciplina, horario):
        self.sala = sala 
        self.disciplina = disciplina
        self.horario = horario
    
    def __str__(self):
        return f"Alocação: {self.disciplina.nome} na {self.sala.nome} no horário {self.horario.dia} {self.horario.horas}"