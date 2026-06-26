# Sistema de Alocação de Salas — Inteligência Artificial

Este projeto foi desenvolvido como parte do Trabalho 1 da disciplina de **Inteligência Artificial (2026)** no curso de Ciência da Computação da **UNIOESTE**. O objetivo é resolver o problema de otimização combinatória e satisfação de restrições (CSP) na alocação de salas, turmas e horários acadêmicos.

## 🧠 Algoritmos Implementados

O sistema aborda o problema utilizando duas estratégias distintas de busca em Inteligência Artificial, integradas a uma interface web comum para fins de análise comparativa:

1. **Busca de Melhor Escolha (*Best-First Search*):** Algoritmo de busca construtiva com ordenação heurística estática baseada na criticidade das disciplinas (priorizando turmas com maior número de alunos, necessidade de projetor e restrição de dias do docente)[cite: 29].
2. **Subida na Montanha (*Random Restart Hill Climbing*):** Algoritmo de busca local estocástica com múltiplos reinícios aleatórios e avaliação de vizinhança paralela baseada em mutação e perturbação de estados de alocação[cite: 31].

---

## 🏗️ Estrutura do Projeto (Módulos)

O software segue uma arquitetura modular que separa a interface, as regras de negócio e os motores de busca:

* `modelos.py`: Contém as classes base do domínio (`Sala`, `Disciplina`, `Horario`, `Alocacao`)[cite: 33].
* `dados_teste.py`: Massa de dados dinâmicos estruturada em 4 cenários analíticos com restrições explícitas de calendário para os professores[cite: 30].
* `validador.py`: Concentra o núcleo lógico de regras, atuando como o verificador rígido de restrições para os algoritmos[cite: 35].
* `best_first.py`: Implementação do motor de busca heurística Best-First[cite: 29].
* `hill_climbing.py`: Implementação do motor de busca estocástica Hill Climbing[cite: 31].
* `app.py`: Servidor API construído em FastAPI responsável por gerenciar as requisições assíncronas do cliente e unificar os formatos de saída[cite: 28].
* `index.html`: Interface do usuário responsiva construída em Tailwind CSS, oferecendo uma matriz de visualização paralela filtrada por sala e painel de desempenho em tempo real[cite: 32].

---

## 🎯 Regras e Restrições (CSP)

O sistema valida e penaliza as alocações com base em restrições rígidas (*Hard Constraints*):

1. **Capacidade Física:** A quantidade de alunos matriculados na disciplina não pode exceder a capacidade máxima de assentos da sala alocada[cite: 35].
2. **Disponibilidade de Recursos:** Disciplinas que exigem projetor só podem ser alocadas em salas ou laboratórios equipados com o recurso[cite: 35].
3. **Agenda do Docente:** Uma disciplina só pode ser agendada em um dia da semana em que o professor possui disponibilidade declarada[cite: 35].
4. **Choque de Sala:** Uma sala não pode receber duas disciplinas distintas no mesmo dia e bloco de horário[cite: 35].
5. **Choque de Professor:** Um professor não pode ministrar duas aulas simultâneas em espaços diferentes[cite: 35].

---

## 📊 Cenários de Teste Disponíveis

A aplicação conta com quatro conjuntos de dados no menu de seleção para testes de escalabilidade[cite: 30]:
* **Cenário Simples:** Matriz enxuta ideal para validação inicial de fluxo[cite: 30].
* **Cenário Realista:** Volume moderado que simula a distribuição de um período padrão[cite: 30].
* **Cenário Intermediário:** Alta densidade de turmas (29 disciplinas) altamente restritas, mas matematicamente tratáveis com 0 conflitos[cite: 30].
* **Cenário Hardcore:** Escopo de estresse massivo projetado para saturar os limites físicos do espaço de estados, forçando o descarte ou a geração de penalidades locais para análise limite dos algoritmos[cite: 30].

---

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de possuir o **Python 3.8+** instalado em seu ambiente de execução.

### 2. Instalação de Dependências
Abra o seu terminal na pasta raiz do repositório e instale os pacotes responsáveis por servir o ecossistema:
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
