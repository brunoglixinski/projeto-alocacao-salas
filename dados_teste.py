#trazendo as classes de modelos para instanciar os objetos aqui
from modelos import Sala, Disciplina, Horario

#lista de objetos do tipo sala
lista_salas = [
    Sala("Sala 101", 30, True),
    Sala("Sala 102", 40, False),
    Sala("Sala 103", 60, True),
    Sala("Sala 104", 25, False),
    Sala("Sala 105", 35, True),
    Sala("Lab Inf 1", 20, True),
    Sala("Lab Inf 2", 20, True),
    Sala("Lab Fis", 15, False),
    Sala("Sala 201", 45, True),
    Sala("Sala 202", 50, False),
    Sala("Sala 203", 30, True),
    Sala("Sala 204", 25, False),
    Sala("Sala 205", 40, True),
    Sala("Anfiteatro", 120, True),
    Sala("Auditório B", 80, True),
    Sala("Sala 301", 30, False),
    Sala("Sala 302", 35, True),
    Sala("Sala 303", 55, False),
    Sala("Sala 304", 25, True),
    Sala("Sala 305", 15, False)
]

#aqui sao as materias disponiveis, o professor, quantidade de alunos na turma e se precisa de projetor
lista_disciplinas = [
    Disciplina("Inteligência Artificial", "Afonso", 45, True),
    Disciplina("Estrutura de Dados", "Beatriz", 35, True),
    Disciplina("Cálculo I", "Carlos", 55, False),
    Disciplina("Cálculo II", "Carlos", 40, False),
    Disciplina("Física Mecânica", "Daniela", 30, False),
    Disciplina("Programação Orientada a Objetos", "Beatriz", 20, True),
    Disciplina("Redes de Computadores", "Eduardo", 28, True),
    Disciplina("Bancos de Dados", "Fernanda", 42, True),
    Disciplina("Engenharia de Software", "Fernanda", 50, True),
    Disciplina("Sistemas Operacionais", "Eduardo", 25, True),
    Disciplina("Compiladores", "Afonso", 18, True),
    Disciplina("Álgebra Linear", "Carlos", 60, False),
    Disciplina("Geometria Analítica", "Roberto", 35, False),
    Disciplina("Teoria da Computação", "Beatriz", 15, False),
    Disciplina("Arquitetura de Computadores", "Eduardo", 30, True),
    Disciplina("Computação Gráfica", "Hugo", 22, True),
    Disciplina("Segurança de Sistemas", "Hugo", 13, True),
    Disciplina("Metodologia Científica", "Ana", 70, True),
    Disciplina("Otimização de Sistemas", "Afonso", 24, False),
    Disciplina("Introdução à Computação", "Ana", 100, True)
]

#aqui vao os horarios e dias possiveis para alocacao de aulas
lista_horarios = [
    # Segunda-Feira
    Horario("Segunda", "08:00-10:00"),
    Horario("Segunda", "10:00-12:00"),
    Horario("Segunda", "13:00-15:00"),
    Horario("Segunda", "15:00-17:00"),
    
    # Terça-Feira
    Horario("Terça", "08:00-10:00"),
    Horario("Terça", "10:00-12:00"),
    Horario("Terça", "13:00-15:00"),
    Horario("Terça", "15:00-17:00"),
    
    # Quarta-Feira
    Horario("Quarta", "08:00-10:00"),
    Horario("Quarta", "10:00-12:00"),
    Horario("Quarta", "13:00-15:00"),
    Horario("Quarta", "15:00-17:00"),
    
    # Quinta-Feira
    Horario("Quinta", "08:00-10:00"),
    Horario("Quinta", "10:00-12:00"),
    Horario("Quinta", "13:00-15:00"),
    Horario("Quinta", "15:00-17:00"),
    
    # Sexta-Feira
    Horario("Sexta", "08:00-10:00"),
    Horario("Sexta", "10:00-12:00"),
    Horario("Sexta", "13:00-15:00"),
    Horario("Sexta", "15:00-17:00")
]
