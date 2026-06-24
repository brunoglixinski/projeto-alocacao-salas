# trazendo as classes de modelos para instanciar os objetos aqui
from modelos import Sala, Disciplina, Horario

# lista de objetos do tipo sala, onde vai o nome da sala, a qtde que comporta e se tem projetor
lista_salas = [
    Sala("Sala 101", 35, True),
    Sala("Sala 102", 60, False),
    Sala("Lab Inf 1", 25, True)
]

# aqui sao as materias disponiveis, o professor, quantidade de alunos na turma e se precisa de projetor
lista_disciplinas = {
    
    # CENÁRIO SIMPLES: Poucas matérias, sem restrições severas ou professores repetidos no mesmo bloco
    "simples": [
        Disciplina("Inteligência Artificial", "Afonso", 30, True),
        Disciplina("Estrutura de Dados", "Beatriz", 25, True),
        Disciplina("Cálculo I", "Carlos", 50, False),
        Disciplina("Programação Orientada a Objetos", "Daniela", 20, False),
        Disciplina("Redes de Computadores", "Eduardo", 24, True)
    ],
    
    # CENÁRIO REALISTA: Volume moderado de matérias, alguns professores com mais de uma disciplina
    "realista": [
        Disciplina("Inteligência Artificial", "Afonso", 30, True),
        Disciplina("Compiladores", "Afonso", 22, True),
        Disciplina("Estrutura de Dados", "Beatriz", 35, True),
        Disciplina("Programação Orientada a Objetos", "Beatriz", 20, True),
        Disciplina("Cálculo I", "Carlos", 55, False),
        Disciplina("Cálculo II", "Carlos", 40, False),
        Disciplina("Física Mecânica", "Daniela", 30, False),
        Disciplina("Redes de Computadores", "Eduardo", 25, True),
        Disciplina("Bancos de Dados", "Fernanda", 42, True),
        Disciplina("Engenharia de Software", "Fernanda", 50, True)
    ],

    # CENÁRIO INTERMEDIÁRIO (MEIO-TERMO): Volume alto (29 matérias). 
    # Espaço apertado e professores com restrições de dias, mas MATEMATICAMENTE POSSÍVEL de resolver com 0 conflitos.
    "intermediario": [
        # Bloco de IA e Dados (Afonso e Beatriz diluídos em seus dias permitidos)
        Disciplina("Inteligência Artificial I", "Afonso", 30, True),
        Disciplina("Inteligência Artificial II", "Afonso", 25, True),
        Disciplina("Compiladores", "Afonso", 30, True),
        Disciplina("Sistemas Especialistas", "Afonso", 20, True),
        Disciplina("Estrutura de Dados I", "Beatriz", 35, True),
        Disciplina("Estrutura de Dados II", "Beatriz", 30, True),
        Disciplina("Programação Orientada a Objetos", "Beatriz", 25, True),
        Disciplina("Teoria dos Grafos", "Beatriz", 20, True),

        # Bloco de Exatas (Turmas grandes dependendo fortemente da Sala 102)
        Disciplina("Cálculo I", "Carlos", 55, False),
        Disciplina("Cálculo II", "Carlos", 60, False),
        Disciplina("Cálculo III", "Carlos", 50, False),
        Disciplina("Álgebra Linear", "Carlos", 55, False),
        Disciplina("Física Mecânica", "Daniela", 40, False),
        Disciplina("Eletromagnetismo", "Daniela", 45, False),
        Disciplina("Termodinâmica", "Daniela", 30, False),

        # Bloco de Infraestrutura e Engenharia
        Disciplina("Redes de Computadores I", "Eduardo", 25, True),
        Disciplina("Sistemas Operacionais", "Eduardo", 25, True),
        Disciplina("Arquitetura de Computadores", "Eduardo", 30, True),
        Disciplina("Sistemas Distribuídos", "Eduardo", 20, True),
        Disciplina("Bancos de Dados I", "Fernanda", 35, True),
        Disciplina("Bancos de Dados II", "Fernanda", 30, True),
        Disciplina("Engenharia de Software", "Fernanda", 35, True),
        Disciplina("Mineração de Dados", "Fernanda", 25, True),

        # Matérias com professores que têm janelas muito curtas na semana (Ana, Hugo, Roberto)
        Disciplina("Metodologia Científica", "Ana", 55, False),
        Disciplina("Introdução à Computação", "Ana", 30, True),
        Disciplina("Computação Gráfica", "Hugo", 22, True),
        Disciplina("Processamento de Imagens", "Hugo", 20, True),
        Disciplina("Matemática Discreta", "Roberto", 45, False),
        Disciplina("Geometria Analítica", "Roberto", 50, False)
    ],
    
    # CENÁRIO HARDCORE: Muitas turmas disputando espaço limite. 
    # IMPOSSÍVEL de resolver 100%. Usado para testar o limite de quebra do algoritmo.
    "hardcore": [
        # Engenharia de Software / IA - Bloco 1
        Disciplina("Inteligência Artificial", "Afonso", 35, True),
        Disciplina("Compiladores", "Afonso", 25, True),
        Disciplina("Otimização de Sistemas", "Afonso", 24, False),
        Disciplina("Estrutura de Dados", "Beatriz", 35, True),
        Disciplina("Programação Orientada a Objetos", "Beatriz", 25, True),
        Disciplina("Teoria da Computação", "Beatriz", 20, False),
        Disciplina("Cálculo I", "Carlos", 60, False),
        Disciplina("Cálculo II", "Carlos", 45, False),
        Disciplina("Álgebra Linear", "Carlos", 58, False),
        
        # Redes e Infraestrutura - Bloco 2
        Disciplina("Redes de Computadores I", "Eduardo", 25, True),
        Disciplina("Redes de Computadores II", "Eduardo", 22, True),
        Disciplina("Sistemas Operacionais", "Eduardo", 25, True),
        Disciplina("Arquitetura de Computadores", "Eduardo", 30, True),
        Disciplina("Bancos de Dados I", "Fernanda", 42, True),
        Disciplina("Bancos de Dados II", "Fernanda", 38, True),
        Disciplina("Engenharia de Software", "Fernanda", 55, True),
        
        # Gráfica e Segurança - Bloco 3
        Disciplina("Computação Gráfica", "Hugo", 22, True),
        Disciplina("Segurança de Sistemas", "Hugo", 15, True),
        Disciplina("Processamento de Imagens", "Hugo", 20, True),
        Disciplina("Metodologia Científica", "Ana", 60, True),
        Disciplina("Introdução à Computação", "Ana", 60, True),
        Disciplina("Lógica para Computação", "Ana", 40, False),
        
        # Disciplinas Extras para Lotar a Semana
        Disciplina("Paradigmas de Programação", "Daniela", 30, True),
        Disciplina("Física Mecânica", "Daniela", 32, False),
        Disciplina("Física Eletromagnetismo", "Daniela", 28, False),
        Disciplina("Sistemas Distribuídos", "Eduardo", 24, True),
        Disciplina("Interface Homem-Computador", "Fernanda", 35, False),
        Disciplina("Inteligência Artificial II", "Afonso", 28, True),
        Disciplina("Administração de Sistemas", "Roberto", 30, False),
        Disciplina("Geometria Analítica", "Roberto", 35, False),
        
        # Bloco de TCC e Estágio
        Disciplina("Trabalho de Conclusão de Curso I", "Afonso", 15, True),
        Disciplina("Trabalho de Conclusão de Curso II", "Beatriz", 15, True),
        Disciplina("Estágio Supervisionado", "Fernanda", 20, False),
        Disciplina("Empreendedorismo em TI", "Ana", 45, True),
        Disciplina("Ética e Legislação", "Ana", 50, False),
        
        # Disciplinas Optativas de Tópicos Especiais
        Disciplina("Tópicos em IA (Deep Learning)", "Afonso", 25, True),
        Disciplina("Tópicos em Web (Vue.js)", "Beatriz", 30, True),
        Disciplina("Tópicos em Banco de Dados (NoSQL)", "Fernanda", 35, True),
        Disciplina("Tópicos em Redes (DevOps)", "Eduardo", 20, True),
        Disciplina("Desenvolvimento de Jogos 2D", "Hugo", 25, True),
        
        # Turmas de Engenharia/Outros Cursos que dividem bloco
        Disciplina("Cálculo III", "Carlos", 50, False),
        Disciplina("Estatística Aplicada", "Carlos", 40, False),
        Disciplina("Matemática Discreta", "Roberto", 45, False),
        Disciplina("Química Geral", "Daniela", 30, False),
        Disciplina("Sistemas Embarcados", "Eduardo", 18, True),
        Disciplina("Mineração de Dados", "Fernanda", 30, True),
        Disciplina("Computação em Nuvem", "Eduardo", 25, True),
        Disciplina("Qualidade de Software", "Fernanda", 40, False),
        Disciplina("Criptografia", "Hugo", 20, True),
        Disciplina("Teoria dos Grafos", "Beatriz", 30, False)
    ]
}

# aqui vao os horarios e dias possiveis para alocacao de aulas
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

# restrições de dias dos professores
restricoes_professores = {
    "Afonso": ["Segunda", "Terça", "Sexta"],
    "Beatriz": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Carlos": ["Segunda", "Terça", "Quarta", "Quinta"],
    "Daniela": ["Terça", "Quarta", "Quinta"],
    "Eduardo": ["Segunda", "Quarta", "Sexta"],
    "Fernanda": ["Segunda", "Terça", "Quarta", "Quinta"],
    "Hugo": ["Quinta", "Sexta"],
    "Ana": ["Segunda", "Quarta"],
    "Roberto": ["Terça", "Quinta"]
}


