from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

banco_de_dados_fake = []

@app.get("/")
def home():
    return {"status": "Sistema de Tarefas Online"}

@app.get("/tasks")
def listar_tarefas():
    return banco_de_dados_fake

@app.post("/tasks")
def criar_tarefa(titulo: str):
    nova_tarefa = {"id": len(banco_de_dados_fake) + 1, "titulo": titulo}
    banco_de_dados_fake.append(nova_tarefa)
    return nova_tarefa

@app.delete("/tasks/{task_id}")
def excluir_tarefa(task_id: int):
    for tarefa in banco_de_dados_fake:
        if tarefa["id"] == task_id:
            banco_de_dados_fake.remove(tarefa)
            return {"mensagem": "Tarefa removida com sucesso"}
    return {"erro": "Tarefa nao encontrada"}


@app.put("/tasks/{task_id}")
def editar_tarefa(task_id: int, novo_titulo: str):
    for tarefa in banco_de_dados_fake:
        if tarefa["id"] == task_id:
            tarefa["titulo"] = novo_titulo
            return tarefa
    return {"erro": "Tarefa nao encontrada"}