# Sistema de Alocação de Salas

Este projeto foi desenvolvido como parte do Trabalho 1 da disciplina de **Inteligência Artificial (2026)** no curso de Ciência da Computação da **UNIOESTE**. O objetivo é resolver o problema de otimização e satisfação de restrições na alocação de salas, turmas e horários.

## Estrutura do Grupo e Algoritmos

Para fins acadêmicos e comparativos, o problema foi abordado utilizando duas estratégias distintas de busca de Inteligência Artificial:
* **Abordagem 1:** Algoritmo de Busca de Melhor Escolha (*Best-First Search*).
* **Abordagem 2:** Algoritmo de Subida na Montanha (*Hill Climbing*).

Ao final, os dois motores de busca são integrados a uma interface web comum para comparação de performance (tempo de execução, taxa de sucesso de alocação e nós visitados).

---

## Estrutura do Projeto (Módulos)

O software foi modelado de forma modular para garantir a reutilização de código e uma integração limpa com a interface web:

* `modelos.py`: Contém as classes base e definições de estruturas de dados (`Sala`, `Disciplina`, `Horario`, `Alocacao`).
* `dados_teste.py`: Escopo com dados fictícios para testes controlados de alocação.
* `validador.py`: O "juiz" do sistema. Contém as regras e restrições que ambos os algoritmos precisam respeitar.
* `busca_best_first.py`: O motor de busca baseado na estratégia Best-First (em desenvolvimento).

---

## Regras (Restrições)

Para que uma alocação seja considerada válida pelo sistema, ela deve respeitar as seguintes condições:

1.  **Capacidade da Sala:** O número de alunos matriculados na disciplina não pode exceder a capacidade máxima da sala.
2.  **Disponibilidade de Recursos:** Se uma disciplina necessita de recursos específicos (como projetor), ela só pode ser alocada em uma sala que possua o recurso.
3.  **Choque de Sala:** Uma sala não pode receber duas disciplinas diferentes no mesmo dia e horário.
4.  **Choque de Professor:** Um professor não pode ministrar duas aulas diferentes no mesmo dia e horário.

---

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### 2. Instalação das Dependências
Abra o terminal na pasta raiz do projeto e instale o framework web e o servidor HTTP responsáveis por conectar a interface aos algoritmos:

```bash
pip install fastapi uvicorn
```

### 3. Iniciando o Sistema
Com as bibliotecas instaladas, basta inicializar o arquivo principal. No terminal, rode o comando:

```Bash
python app.py
```

💡 Nota para desenvolvimento: Se estiver editando o código e quiser que o servidor aplique as mudanças automaticamente, suba a aplicação utilizando:

```Bash
uvicorn app:app --reload
```

### 4. Acessando a Interface
O servidor iniciará localmente servindo o painel de controle e a grade visual. Abra o navegador de sua preferência e acesse:

👉 http://127.0.0.1:8000

A partir do menu superior da aplicação web, você poderá selecionar os datasets (Cenário Simples, Realista ou Hardcore) e executar as buscas para visualizar e comparar as métricas de otimização e resolução de restrições.
