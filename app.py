from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from hill_climbing import subidamontanha
from best_first import bestFirst 
# Importando a lista de salas para poder enviar ao JavaScript
from dados_teste import lista_salas

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def ler_interface():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()
    

@app.get("/alocar/{algoritmo}")
def rodar_alocacao(algoritmo: str, dataset: str = "realista"):
    
    if algoritmo == "hill_climbing":
        resultado_busca, tempo, nos, conflitos = subidamontanha(dataset) # Passa o dataset pra sua função
    else:
        #ALTERADO: Corrigida a passagem necessaria do best first, com nos gerados e expandidos
        resultado_busca, tempo, nos_exp, nos_ger, conflitos = bestFirst(dataset)
        
    # Transforma os objetos em dicionários para o front-end
    grade_formatada = []
    for aloc in resultado_busca:
        if aloc.disciplina is None:
            continue
            
        grade_formatada.append({
            "disciplina": aloc.disciplina.nome,
            "sala": aloc.sala.nome,
            "dia": aloc.horario.dia,
            "horario": aloc.horario.horas,
            "professor": aloc.disciplina.prof
        })

    # ALTERADO: Cria uma lista limpa contendo apenas os nomes das salas cadastradas
    salas_disponiveis = [sala.nome for sala in lista_salas]

    # ALTERADO: adicionei em métricas os nós gerados e expandidos que são cobrados
    return {
        "algoritmo": "Subida na Montanha" if algoritmo == "hill_climbing" else "Best-First Search",
        "metricas": {
            "tempo_execucao_ms": tempo,
            "nos_expandidos": nos_exp,
            "nos_gerados": nos_ger,
            "conflitos_restantes": conflitos
        },
        "grade_alocacao": grade_formatada,
        "salas": salas_disponiveis
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)