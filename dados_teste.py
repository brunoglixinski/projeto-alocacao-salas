#trazendo as classes de modelos para instanciar os objetos aqui
from modelos import Sala, Disciplina, Horario

#lista de objetos do tipo sala
lista_salas = [
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True),
    Sala("sala1", 50, True)
]

#aqui sao as materias disponiveis, o professor e a quantidade de alunos na turma
lista_disciplina = [
    Disciplina("Matemática", "Prof. A", 30, True),
    Disciplina("Física", "Prof. B", 25, True),
    Disciplina("Química", "Prof. C", 20, True),
    Disciplina("Matemática", "Prof. A", 30, True),
    Disciplina("Física", "Prof. B", 25, True),
    Disciplina("Química", "Prof. C", 20, True),
    Disciplina("Matemática", "Prof. A", 30, True),
    Disciplina("Física", "Prof. B", 25, True),
    Disciplina("Química", "Prof. C", 20, True),
    Disciplina("Matemática", "Prof. A", 30, True),
    Disciplina("Física", "Prof. B", 25, True),
    Disciplina("Química", "Prof. C", 20, True)
]

#aqui vao os horarios e dias possiveis para alocacao de aulas
lista_horarios = [
    Horario("Segunda-feira", "08:00-10:00"),
    Horario("Terça-feira", "10:00-12:00"),
    Horario("Quarta-feira", "14:00-16:00"),
    Horario("Segunda-feira", "08:00-10:00"),
    Horario("Terça-feira", "10:00-12:00"),
    Horario("Quarta-feira", "14:00-16:00"),
    Horario("Segunda-feira", "08:00-10:00"),
    Horario("Terça-feira", "10:00-12:00"),
    Horario("Quarta-feira", "14:00-16:00"),
    Horario("Segunda-feira", "08:00-10:00"),
    Horario("Terça-feira", "10:00-12:00"),
    Horario("Quarta-feira", "14:00-16:00"),
    Horario("Segunda-feira", "08:00-10:00"),
    Horario("Terça-feira", "10:00-12:00"),
    Horario("Quarta-feira", "14:00-16:00")
]
