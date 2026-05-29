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

*(Instruções de execução serão adicionadas conforme o desenvolvimento dos motores de busca for concluído).*
